from arachni import *
import time


#URL = input("Please insert the URL of the Web Application :")
url = raw_input('Please insert the URL of the Web Application :')

f = open("id.txt", "w+")
f.write(url)
f.close()

execfile("PythonApp.py") #get scan ID

f = open("id.txt", "r")
readFile = f.readlines()
getID = 'd3a9e39d51e3f39cfbd58c7bd657dc4b'

while(1):
    if(client.get_report(getID, 'xml') == "None"):
        print("Scanning In Progress .....")
        time.sleep(10)
    else:
        print(client.get_status(getID))
        print(client.get_report(getID, 'xml'))
        f.close()
        break
