import requests


# def status():
x = requests.get('https://jira.surecomp.com/')
 
   
if x.status_code == 200:
        print ('jira up')
else:
        print ('Boo!')
               