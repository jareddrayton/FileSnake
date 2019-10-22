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
                    default="Kateikyoushi Hitman Reborn",
                    help="Directory containing files to be renamed",
                    metavar='')

parser.add_argument("-id", "--showid",
                    type=str,
                    help="Provide the TVDB show ID",
                    metavar='')


generate_test_data.usecase1_test("Kateikyoushi Hitman Reborn", 203)

# Variables

args = parser.parse_args()

# Possible flag variables

append_episode_names = True

change_source_path = True # Unused

captial_sande = True # Unused

###########################################################################

def source_path(source):

    source = args.source.strip(' " \\ . ')

    source = Path(source)
    
    # Check that the directory exists and exit the program if it doesn't
    if source.exists() == False:
        print('Directory does not exist.')
        print('Program terminated.')
        exit()

    return source.name, source.resolve()

series_name, source_directory = source_path(args.source)

###########################################################################
# request a token from the TVDB
headers={'Content-type':'application/json', 'Accept':'application/json'}
r = requests.post('https://api.thetvdb.com/login', data = '{"apikey":"I7KOIY59UWQL3JPS"}', headers=headers)
token = r.json()['token']

###########################################################################

def series_search():
    # Search the TVDB using the given directory name and return 
    
    print("Searching the TVDB for " + '"' + series_name + '"....')
    headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
    search_results = requests.get('https://api.thetvdb.com/search/series?name=' + requests.utils.quote(series_name), headers=headers)
    #print(search_results.json())
    
    print("")
    if search_results.status_code == 404:
        print("No results found for " + series_name)
        print('Program terminated.')
        exit()
    elif search_results.status_code == 200:
        # List the search results
        print("Option - Series Name - Show ID")
        for i in range(len(search_results.json()['data'])):
            print(i, search_results.json()['data'][i]["seriesName"], search_results.json()['data'][i]["id"])

    print()
    print("Select an option.")
    choice = int(input())

    return search_results.json()['data'][choice]["seriesName"], str(search_results.json()['data'][choice]["id"])

series_name, series_id = series_search()

###########################################################################

def create_file_hierarchy():
    # return a dictionary describing seasons and episode hierarchy for series_id

    file_hierarchy = {}
    episode_names = []

    # Find the number of seasons for show
    headers={'Content-type':'application/json', 'Authorization':'Bearer ' + token}
    b = requests.get('https://api.thetvdb.com/series/' + series_id + '/episodes/summary', headers=headers)
    seasons = b.json()['data']['airedSeasons']
    print(seasons)
    
    # removes the specials season folder if present
    if seasons.count("0") > 0:
        seasons.remove("0")

    # Loop over the seasons starting from Season 1, missing out the specials season
    for i in range(1, len(seasons)+1):
        episodes = requests.get('https://api.thetvdb.com/series/' + series_id + '/episodes/query?airedSeason='+ str(i), headers=headers)
        file_hierarchy[str(i)] = len(episodes.json()['data'])
        
        for i in range(len(episodes.json()['data'])):
            episode_names.append(episodes.json()['data'][i]["episodeName"])

    return file_hierarchy, episode_names 

file_hierarchy, episode_names = create_file_hierarchy()

###########################################################################

def usecase1():
    pass

###########################################################################

# Search the source directory for files and directories and then sort by natural order
for root, dirs, files in os.walk(source_directory):
    files = natsorted(files)

############################################################################

# Calculate the total episodes in the target show
print("Seasons and Episode Hierarchy")
print("")
total_episodes = 0
for k, v in file_hierarchy.items():
    print("Season", k, "Episodes", v)
    total_episodes += v

# Check that the number of video files in source matches that of the target show
if len(files) == total_episodes:
    print()
    print("Total Source files:", len(files))
    print("Total Target files:", total_episodes)
    print()
    print("The total number of target files matches the total number of episodes in the chosen series.")
else:
    print()
    print("Total Source files:", len(files))
    print("Total Target files:", total_episodes)
    print()
    print("The total number of target files does not match the total number of episodes in the chosen series.")

############################################################################

# Make a list of all the new filenames and list of seasons
new_names = []
seasons = []
for k, v in file_hierarchy.items():
    for i in range(1, v+1):
        new_names.append(series_name + " - s{:0>2}".format(k) + "e{:0>2}".format(i) )
        seasons.append("Season {:0>2}//".format(k))


# Append episode names to filename and file extension
if append_episode_names == True:
    for i in range(len(files)):
        p = Path(files[i])
        new_names[i] = new_names[i] + " - " + episode_names[i].translate({ord(i): None for i in '?*."/\\[]:;|,'}) + p.suffix
else:
    for i in range(len(files)):
        p = Path(files[i])
        new_names[i] = new_names[i] + p.suffix




# Preview the changes
for i in range(len(files)):
    print(source_directory / files[i])
    print(source_directory / seasons[i] / new_names[i])
    print()

# Confirm the file changes
print()
print("Would you like to proceed with these file changes? y/n")
response = input()

# Proceed with renaming the files
if response == "y" or response == "Y":

    # create empty season folders
    for k, v in file_hierarchy.items():
        season_path = source_directory / "Season {:0>2}".format(k)
        os.mkdir(season_path)
    
    # Perform the renaming using path objects
    for i in range(len(files)):
        src = source_directory / files[i]
        dst = source_directory / seasons[i] / new_names[i]
        os.rename(src, dst)
    
    print()
    print("Operation completed")

else:
    print()
    print("Operation aborted")
