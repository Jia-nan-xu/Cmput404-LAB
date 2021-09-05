import requests                         #this line is used to  import requests
import urllib

print(requests.__version__)             #used to print requests veersion

r = requests.get('http://google.com/')  #use the reequests to get the google website
print(r.text)                           #print the text of the website we get 

git_url = "https://raw.githubusercontent.com/ZacOrz/Cmput404/main/q2.py"  #this  is the raw url from github

r_git = urllib.request.urlretrieve(git_url, "q2.py")    #download the  file from github
git_txt  = requests.get(git_url)                        #geet the code and print it
print(git_txt.text)
