#!/user/bin/env python3
import socket, time, sys
from multiprocessing import Process


#defeine global address and buff size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#TO-DO: get_remote_ip() method
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip


#TO-DO: handle_request() method
def handle_request(addr, conn):
    print("Connected by", addr)

    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()


def main():

#TO-DO: esatablish localhost, extern_gost (google), port, buffer size
    extern_host = 'www.google.com'
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:

    #TO-DO: bind, and set to listen mode
        print("Starting proxy serve")
        #allow reused addresses, bind and set to listening mode
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
        ##TO-DO: accept incoming connections from proxy_start, print indormation about connection

            #connect proxy_start
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                #TO-DO: get remote IP from google, connect procy_end to it
                print("Connecting to Google")
                remote_ip = get_remote_ip(extern_host)

                #connect proxy_end
                proxy_end.connect((remote_ip, port))

                #send data
                send_full_data = conn.recv(BUFFER_SIZE)
                print(f"Sending received data {send_full_data} to Google")
                proxy_end.sendall(send_full_data)

                #remember to shut down!
                proxy_end.shutdown(socket.SHUT_WR) #shutdown is different from close()

                data = proxy_end.recv(BUFFER_SIZE)
                print(f"Sending received data {data} to client")
                #send data back
                conn.send(data)
                #now for the multiprocessing...

                #TO-DO: allow for multiple connections with a Process daemon
                #make sure to set target = handle_request when creating the Process
                p = Process(target = handle_request, args = (addr, conn))
                p.daemon = True
                p.start()
                print("Started process", p)



            #TO-DO:close the connection!!
            conn.close()

if __name__ == "__main__":
    main()