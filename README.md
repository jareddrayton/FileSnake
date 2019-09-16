## FilePot (CAUTION: Still in Alpha)

FilePot is a tool for renaming and organising TV Show/Anime files to match the TVDB and  [Plex naming conventions](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/). Episode and Season information is retrieved using the TVDB's [Official API](https://api.thetvdb.com/swagger) and is used to map onto the source files.

**Important Note** 

An API key from the TVDB is currently needed in order to work with the TVDB API.

**Limitations** 

1. Only show data from the TVDB is supported at the moment.
2. There is no support for handling multi episode file e.g. . 
3. There is no support for the renaming of specials.

## Usecases

#### Scenario 1 

Show Name Episode 1.mkv	--> Season 01\Show Name - S01E01.mkv
Show Name Episode 2.mkv	--> Season 01\Show Name - S01E02.mkv
Show Name Episode 3.mkv	--> Season 01\Show Name - S01E03.mkv
Show Name Episode 4.mkv	--> Season 02\Show Name - S02E01.mkv
Show Name Episode 5.mkv	--> Season 02\Show Name - S02E02.mkv
Show Name Episode 6.mkv	--> Season 02\Show Name - S02E03.mkv

**Assumptions** 
* The entire series is contained in one folder.
* When the source files are sorted in natural sort order with some type of incremental numbering naming.
* There are no other files in the folder.

---
#### Scenario 2 (Not Implemented)

Episodes are in a correct season directory structure but have a global incremental numbering rather than local to the season.

1.1  1.1
1.2  1.2 
1.3  1.3
2.4  2.1
2.5  2.2 
2.6  2.3

Assumptions


Limitations


---
#### Scenario 3 (Not Implemented)

Episodes correctly match TVDB listing but. (Reverse of Scenario 1) 

1.1  1
1.2  2
1.3  3
2.1  4
2.2  5
2.3  6

Assumptions

---
#### Scenario 4 (Not Implemented)

Rename files

Add show name etc, rip info.

----------------------------------------------------------------------------------------------