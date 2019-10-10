## FilePot (CAUTION: Still in Alpha)

FilePot is a tool for renaming and reorganising TV Show and Anime files to match the [TVDB](https://www.thetvdb.com/) episode data, and follow [Plex](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/) naming conventions. Episode and Season information is retrieved using the TVDB's [Official API](https://api.thetvdb.com/swagger).

**Important Note** 

For FilePot to work, an API key from the TVDB is currently needed in to access the TVDB API.

**Limitations** 

1. Only episode data from the TVDB is supported at the moment.
2. There is no support for handling multi episode files e.g. . 
3. There is no support for handling renaming of specials.
4. There is no support for handling seperate subtitle file renaming.

## Usecases

Here are some of the most common usecases that FilePot may help you address. 

#### Scenario 1 

All episodes of a series are present, however they are not sorted into seasons and have a global numbering system.

Show Name Episode 1.mkv	----> \Season 01\Show Name - S01E01.mkv  
Show Name Episode 2.mkv	----> \Season 01\Show Name - S01E02.mkv  
Show Name Episode 3.mkv	----> \Season 01\Show Name - S01E03.mkv  
Show Name Episode 4.mkv	----> \Season 02\Show Name - S02E01.mkv  
Show Name Episode 5.mkv	----> \Season 02\Show Name - S02E02.mkv  
Show Name Episode 6.mkv	----> \Season 02\Show Name - S02E03.mkv  

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

**Assumptions** 



---
#### Scenario 3 (Not Implemented)

Episodes correctly match TVDB listing but. (Reverse of Scenario 1) 

1.1  1
1.2  2
1.3  3
2.1  4
2.2  5
2.3  6

**Assumptions** 

---
#### Scenario 4 (Not Implemented)

Rename files

Add show name etc, rip info.

----------------------------------------------------------------------------------------------

## Tools