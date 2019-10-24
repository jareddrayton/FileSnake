## FileSnake (CAUTION: Still in Alpha)

FileSnake is a tool for renaming and reorganising TV Show and Anime files to match the [TVDB](https://www.thetvdb.com/) episode data, and follow [Plex](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/) naming conventions. Episode and Season information is retrieved using the TVDB's [Official API](https://api.thetvdb.com/swagger).

**Important Note** 

For FileSnake to work, an API key from the TVDB is currently needed in to access the TVDB API.

**Limitations** 

1. Only episode data from the TVDB is supported at the moment.
2. There is no support for handling multi episode files e.g. . 
3. There is no support for handling renaming of specials.
4. There is no support for handling seperate subtitle file renaming.

## Usecases

Here are the two common usecases that FileSnake has been written to help address. 

#### Usecase 1 

All episodes of a series are present, however, they have an absolute numbering system and are not sorted into seasons.

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
#### Usecase 2 (Not Implemented)

All episodes of a series are present and episodes are in a correct season directory structure, however, they have an absolute numbering system.

\Season 01\Show Name Episode 1.mkv	----> \Season 01\Show Name - S01E01.mkv  
\Season 01\Show Name Episode 2.mkv	----> \Season 01\Show Name - S01E02.mkv  
\Season 01\Show Name Episode 3.mkv	----> \Season 01\Show Name - S01E03.mkv  
\Season 02\Show Name Episode 4.mkv	----> \Season 02\Show Name - S02E01.mkv  
\Season 02\Show Name Episode 5.mkv	----> \Season 02\Show Name - S02E02.mkv  
\Season 02\Show Name Episode 6.mkv	----> \Season 02\Show Name - S02E03.mkv  

**Assumptions** 


----------------------------------------------------------------------------------------------

## Tools

As well as the above two usecase some limited standard bulk rename utilities are included.

Add or remove series name, media info etc.