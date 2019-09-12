import os
import requests
import json
from natsort import natsorted

# detect the current working directory
path = os.getcwd()
print("Current working directory:", path)


# manually provide show ID
show_id = "252322"
# manually provide show Name
show_name = "Hunter X Hunter"


# request a token from the TVDB
headers={'Content-type':'application/json', 'Accept':'application/json'}
r = requests.post('https://api.thetvdb.com/login', data = '{"apikey":"I7KOIY59UWQL3JPS"}', headers=headers)
token = r.json()['token']


# Create a dictionary with season as key and number of episode as data.
def create_file_hierarchy():
    
    file_hierarchy = {}
    
    # Find the number of seasons for show
    headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
    b = requests.get('https://api.thetvdb.com/series/252322/episodes/summary', headers=headers)
    seasons = b.json()['data']['airedSeasons']

    # Loop over the seasons starting from Season 1, missing out the specials season
    for i in range(1, len(seasons)):
        episodes = requests.get('https://api.thetvdb.com/series/252322/episodes/query?airedSeason='+ str(i), headers=headers)
        file_hierarchy[str(i)] = len(episodes.json()['data'])

    return file_hierarchy

file_hierarchy = create_file_hierarchy()


# Search the source directory for files and directories and then sort by natural order
for root, dirs, files in os.walk("Test//."):
    files = natsorted(files)


# Calculate the total episodes in the target show
total_episodes = 0
for k, v in file_hierarchy.items():
    print("Season", k, "Episodes", v)
    total_episodes += v


# Check that the number of video files in source matches that of the target show
if len(files) == total_episodes:
    print("Success")
else:
    print("The is a file count missmatch")


# Make a list of all the new filenames and list of seasons
new_names = []
seasons = []
for k, v in file_hierarchy.items():
    for i in range(1, v+1):
        new_names.append(show_name + " s{:0>2}".format(k) + "e{:0>2}".format(i) + ".mkv")
        seasons.append("Season{:0>2}//".format(k))
print()
print("Total Source files:", len(files), "Total Target files:", len(new_names))


# Preview the changes
for i in range(len(files)):    
    print("Test//" + files[i], "Test//" + seasons[i] + new_names[i])


# Confirm the file changes
print()
print("Would you like to Proceed? y/n")
response = input()


# Proceed with renaming the files
if response == "y" or "Y":

    # create season folders
    for k, v in file_hierarchy.items():
        os.mkdir("Test//Season{:0>2}//".format(k))
    
    for i in range(len(files)):
        src = "Test//" + files[i]
        dst = "Test//" + seasons[i] + new_names[i]    
        os.rename(src, dst)
    print()
    print("Renaming completed")

else:
    print()
    print("Renaming aborted")
