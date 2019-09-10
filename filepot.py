import os
import requests
import json
from natsort import natsorted

# detect the current working directory
path = os.getcwd()

show_id = ""

headers={'Content-type':'application/json', 'Accept':'application/json'}

r = requests.post('https://api.thetvdb.com/login', data = '{"apikey":"I7KOIY59UWQL3JPS"}', headers=headers)

print(r.json())
print(type(r.json()))

token = r.json()['token']
print(token)

# get seasons

#curl -X GET --header 'Accept: application/json' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjgyMzE0NjksImlkIjoiRmlsZVBvdCIsIm9yaWdfaWF0IjoxNTY4MTQ1MDY5fQ.WAA5Q913bv5TfvWF9o1ShnP5UyooB1YYM-zTJeNg0YrWSl1Wx6WEJlRebWGuyd4JobCvrXj3MMIJcJPadhCPdV3AOVdVbeBQrl0ZHCZ9Ea2KD5ebgcFF1UBuUM5rU1gGo3vs8WQsJmQapdwyCf7ITs3J2GRASE8E3bdmkz-rzDSgXPMC-zPf4DZBvA9Ru5mn_8CmJXNxK73omNDrsnu0LMfcvKZMczproWYK9aQpMfvq40z-yn61TlE7Ybb3stQxWKAgFR6-4FftJUW-SKRbtAbIZAhpJ_wHbh0ahQjN0nU-L7ejDULb0qyvod5kY19AQcfrDZwjEjnPN02qBnHwkg' 'https://api.thetvdb.com/series/252322/episodes/summary'
headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}

b = requests.get('https://api.thetvdb.com/series/252322/episodes/summary', headers=headers)
print(b.json())

print(b.json()['data']['airedSeasons'])

for root, dirs, files in os.walk("Test//."):
    #print(files)
    #print(natsorted(files))
    
    files = natsorted(files)
    
    #print(files)
    
    #for filename in files:
        
        #print(filename)
