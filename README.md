# ASCIITabsConverter

ASCII Guitar Tabs converts Guitar ASCII tabs to [Music21](http://web.mit.edu/music21/) Tiny Notation format (Music21 MIT library) or Python List of standard notation notes.
Also, provides some computation on the guitar tab like song's key, song's top phrases (of variable lenght, you can choose) and  best scales/ modes to play along. See below some sample outputs. It uses Python 3.6.1

CONVERTER:
----------
It defines and uses 5 basic functions to convert:

**openandread** - To read the tab file in ASCII format, see below specific requirements of the ASCII format. You need to provide the full path.

**producesortedtablist** -Produce list of notes in format string+fret, in the right playing order. Example: "D7" - this is: string D fret 7 . An example is: ['D7', 'D9', 'G7', 'B10', 'B10', 'B12', 'B12']
 
**converttonotes**  - Converts the "sorted tab list" output of the function "producesortedtablist" into a string of notes, in standard format, comma separated: "A,B,D,A,A,B,B,B,E,D,B,G,E,B,Gb". Note Octave information is not included, but it is included in function *converttomusic21*

**converttomusic21** - Produce a string, comma separated, in the [Music21](http://web.mit.edu/music21/) - MIT magic musical library- Tiny Notation Format. As ASCII Tabs normally do not have info  about the duration, it is converted by default in 4/4 format. 

Example outout:
"a4 b4 d4 a4 a4 b'4 b'4 b'4 e'4 d4 b4 g4 e4 b4 f#4"
These string can then be imported into Musc21 which is a powerful music library and will allow us to do a lot of analysis.

**getguitarstyledata** - Will provide some info about the guitar style. Like number of Hammers or slides.




STATS:
------
For the stats it uses 2 functions:
**songstatsmusic21** and **songstats**

They use as input the string obtained as output in the conversion. If you converted to Music21 format then use "songstatmusic21".
I recommend using the [Music21](http://web.mit.edu/music21/) format as the analysis uses [Music21](http://web.mit.edu/music21/) library which is powerful and gives a lot of more info.

These functions will give you info like:
* Song key (only in songstatsmusic21), 
* Top Notes 
* Top phrases ( you can modify the lenght of the phrase analysis by changing value of variable "pharselenght"), 
* Modes and scales to use ((only in songstatsmusic21)
  
  
Sample output of songstatmusic21:

```
 "Top 20 music21 notes:  [('a4', 281), ("b'4", 214), ("e'4", 155), ("d'4", 153), ("g'4", 120), ('d4', 112), ('g4', 105), ('b4', 91), ('e4', 90), ("f'#4", 73), ('f#4', 49), ("a'#4", 44), ('c4', 32), ("a'4", 32), ("f'4", 21), ("c'4", 20), ('f4', 19), ("c'#4", 19), ('c#4', 9), ("e''4", 8)]

Possible song Key:  e minor
 
Scales and Modes:

Possible Major scales: [(1539, <music21.scale.MajorScale G major>), (1515, <music21.scale.MajorScale D major>), (1453, <music21.scale.MajorScale C major>), (1293, <music21.scale.MajorScale A major>)]
Possible Dorian scales: [(1539, <music21.scale.DorianScale A dorian>), (1515, <music21.scale.DorianScale E dorian>), (1453, <music21.scale.DorianScale D dorian>), (1293, <music21.scale.DorianScale B dorian>)]
Possible Phrygian scales: [(1539, <music21.scale.PhrygianScale B phrygian>), (1515, <music21.scale.PhrygianScale F# phrygian>), (1453, <music21.scale.PhrygianScale E phrygian>), (1293, <music21.scale.PhrygianScale C# phrygian>)]
Possible Lydian scales: [(1539, <music21.scale.LydianScale C lydian>), (1515, <music21.scale.LydianScale G lydian>), (1453, <music21.scale.LydianScale F lydian>), (1293, <music21.scale.LydianScale D lydian>)]
Possible Mixolydian scales: [(1539, <music21.scale.MixolydianScale D mixolydian>), (1515, <music21.scale.MixolydianScale A mixolydian>), (1453, <music21.scale.MixolydianScale G mixolydian>), (1293, <music21.scale.MixolydianScale E mixolydian>)]
Possible Aeolian scales: [(1539, <music21.scale.MinorScale E minor>), (1515, <music21.scale.MinorScale B minor>), (1453, <music21.scale.MinorScale A minor>), (1293, <music21.scale.MinorScale F# minor>)]
Possible Locrian scales: [(1539, <music21.scale.LocrianScale F# locrian>), (1515, <music21.scale.LocrianScale C# locrian>), (1453, <music21.scale.LocrianScale B locrian>), (1293, <music21.scale.LocrianScale G# locrian>)]
Possible Blues Penta scales: [(1405, <music21.scale.WeightedHexatonicBlues E Weighted Hexatonic Blues>), (1262, <music21.scale.WeightedHexatonicBlues B Weighted Hexatonic Blues>), (1262, <music21.scale.WeightedHexatonicBlues C- Weighted Hexatonic Blues>), (1112, <music21.scale.WeightedHexatonicBlues A Weighted Hexatonic Blues>)]

 
top #10 phrases of  10  notes lenght (you can change this in var phraselenght)
 
['A', 'B', 'Bb', 'A', 'B', 'Bb', 'A', 'B', 'Bb', 'A'] :  21
['B', 'Bb', 'A', 'B', 'Bb', 'A', 'B', 'Bb', 'A', 'B'] :  21
['Bb', 'A', 'B', 'Bb', 'A', 'B', 'Bb', 'A', 'B', 'Bb'] :  21
['F', 'E', 'C', 'E', 'F', 'B', 'F', 'E', 'C', 'E'] :  5
['E', 'B', 'Gb', 'G', 'B', 'E', 'G', 'Gb', 'E', 'B'] :  4

```


HOW TO USE THE FUNCTIONS:
---------------------------
Example of how to use the functions:

```
#convert
sampletabread = openandread('C:\\UTabs\\tab.txt')  #Openfile
producedlist = producesortedtablist(sampletabread)                                #call function to produce list of noted in format string+fret, in the right playing order. Example: "D7" - this is: string D fret 7
convertedlist = converttonotes(producedlist)                                  #call function to convert to notes
convertedmusic21 = converttomusic21(producedlist)
counterstechniques = getguitarstyledata(sampletabread)

#stats
songstats(convertedlist)
songstatsmusic21(convertedmusic21)

```



ASCII TAB REQUIREMENTS:
-----------------------

    # it assumes a standard tunning with the following ASCII String indication
    #   e|-------------------   (also can work with the first string being "E")
    #   B|-------------------
    #   G|-------------------
    #   D|-------------------
    #   A|-------------------
    #   E|-------------------
    #
    #   Notes are expressed with numbers and techniques with h,b,pb,s,p or r. Sample:
    #    e |---------22p17-------17-|-17-------------17-|
    #    B |-22b24------------------|-------------15----|
    #    G |------------------------|-------19h16-------|
    #    D |------------------------|-------------------|
    #    A |------------------------|-------------------|
    #    E |------------------------|-------------------|

    # If you need to change from standard tunning, can do so in the following lines, function .startwith("







