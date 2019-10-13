import argparse
import os
import requests
import json

import generate_test_data

from pathlib import Path
from natsort import natsorted


parser = argparse.ArgumentParser()

parser.add_argument("-src", "--source",
                    type=str,
                    default='Hunter X Hunter',
                    help="File path of the source folder containing files",
                    metavar='')

parser.add_argument("-id", "--showid",
                    type=str,
                    default='252322',
                    help="Provide the TVDB show ID",
                    metavar='')


# variables

args = parser.parse_args()

print(args.source)

source = args.source.strip('" \\ .')
print(source)


show_id = args.showid

append_episode_names = True

#manually provide show Name
show_name = "Hunter X Hunter"

###########################################################################
# Generate test data

generate_test_data.usecase1_test(source)

source = Path(source)

###########################################################################
# Print the current working directory
print("Current working directory:", Path.cwd())


###########################################################################
# request a token from the TVDB
headers={'Content-type':'application/json', 'Accept':'application/json'}
r = requests.post('https://api.thetvdb.com/login', data = '{"apikey":"I7KOIY59UWQL3JPS"}', headers=headers)
token = r.json()['token']


###########################################################################

def series_search():
    # try and find the name from the directory name
    # if show id is not provided, search for 
    
    headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
    search_results = requests.get('https://api.thetvdb.com/search/series?name=' + requests.utils.quote(args.source), headers=headers)
    print(search_results.json())
    
    for i in range(len(search_results.json()['data'])):
        print(search_results.json()['data'][i]["seriesName"], search_results.json()['data'][i]["id"]) 

series_search()

###########################################################################

# Create a dictionary with season as key and number of episodes as value.
def create_file_hierarchy():
    
    file_hierarchy = {}
    episode_names = []

    # Find the number of seasons for show
    headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
    b = requests.get('https://api.thetvdb.com/series/252322/episodes/summary', headers=headers)
    seasons = b.json()['data']['airedSeasons']

    # Loop over the seasons starting from Season 1, missing out the specials season
    for i in range(1, len(seasons)):
        episodes = requests.get('https://api.thetvdb.com/series/252322/episodes/query?airedSeason='+ str(i), headers=headers)
        file_hierarchy[str(i)] = len(episodes.json()['data'])
        
        for i in range(len(episodes.json()['data'])):
            episode_names.append(episodes.json()['data'][i]["episodeName"].strip('?*."/\\[]:;|,'))

    return file_hierarchy, episode_names 

file_hierarchy, episode_names = create_file_hierarchy()




def usecase1():
    pass




# Search the source directory for files and directories and then sort by natural order
for root, dirs, files in os.walk(source):
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
        new_names.append(show_name + " s{:0>2}".format(k) + "e{:0>2}".format(i) )
        seasons.append("Season{:0>2}//".format(k))


# Append episode names to filename and file extension
if append_episode_names == True:
    for i in range(len(files)):    
        new_names[i] = new_names[i] + " - " + episode_names[i] + ".mkv"  
else:
    for i in range(len(files)):    
        new_names[i] = new_names[i] + ".mkv"


print()
print("Total Source files:", len(files))
print("Total Target files:", len(new_names))
print()


# Preview the changes
for i in range(len(files)):
    print(Path.cwd() / source / files[i], Path.cwd() / source / seasons[i] / new_names[i])


# Confirm the file changes
print()
print("Would you like to Proceed? y/n")
response = input()

# Proceed with renaming the files
if response == "y" or "Y":

    # create empty season folders
    for k, v in file_hierarchy.items():
        season_path = Path.cwd() / source / "Season{:0>2}".format(k)
        os.mkdir(season_path)
    
    for i in range(len(files)):
        src = Path.cwd() / source / files[i]
        dst = Path.cwd() / source / seasons[i] / new_names[i]
        os.rename(src, dst)
    
    print()
    print("Operation completed")

else:
    print()
    print("Operation aborted")
