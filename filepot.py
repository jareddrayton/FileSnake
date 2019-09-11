import os
import requests
import json
from natsort import natsorted

# detect the current working directory
path = os.getcwd()
print("Current working directory:", path)

# manually provide show ID
show_id = "252322"

show_name = "Hunter X Hunter"

# request token stuff
headers={'Content-type':'application/json', 'Accept':'application/json'}
r = requests.post('https://api.thetvdb.com/login', data = '{"apikey":"I7KOIY59UWQL3JPS"}', headers=headers)
#print(r.json())
# Extract the token from the returned json data
token = r.json()['token']
#print(token)

# get seasons
headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
b = requests.get('https://api.thetvdb.com/series/252322/episodes/summary', headers=headers)
seasons = b.json()['data']['airedSeasons']

# get episodes total
file_hierarchy = {}
# Loop over seasons starting from Season 1, missing out the specials season
for i in range(1, len(seasons)):
    episodes = requests.get('https://api.thetvdb.com/series/252322/episodes/query?airedSeason='+ str(i), headers=headers)
    #print(episodes.json()['data'])
    print(len(episodes.json()['data']))
    file_hierarchy[str(i)] = len(episodes.json()['data'])

print(file_hierarchy)

#print(episodes.json()['data']['airedSeasons'])


for root, dirs, files in os.walk("Test//."):
    #print(files)
    files = natsorted(files)
    #print(files)
    
    print("Total source files:", len(files))
    
    #for filename in files:
        #print(filename)

total_episodes = 0

for k, v in file_hierarchy.items():
    print("Season", k, "Episodes", v)
    total_episodes += v


if len(files) == total_episodes:
    print("Success")
else:
    print("Error: File count missmatch")


new_names = []

for k, v in file_hierarchy.items():
    for i in range(1, v+1):
        new_names.append(show_name + " s0" + k + "e" + str(i) + ".mkv")

print(len(files))
print(len(new_names))

for i in range(len(files)):
    print(files[i], new_names[i])
    src = "Test//" + files[i]
    dst = "Test//" + new_names[i]
    
    os.rename(src, dst) 

#for filename in os.listdir("xyz"): 
    #dst ="Hostel" + str(i) + ".jpg"
    #src ='xyz'+ filename 
    #dst ='xyz'+ dst 
          
    # rename() function will 
    # rename all the files 
    #os.rename(src, dst) 
    #i += 1