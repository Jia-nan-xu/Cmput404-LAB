import requests                         #this line is used to  import requests

print(requests.__version__)             #used to print requests veersion

r = requests.get('http://google.com/')  #use the reequests to get the google website
print(r.text)                           #print the text of the website we get 
