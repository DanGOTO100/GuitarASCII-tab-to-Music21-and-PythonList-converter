import sys
import os
import re
import operator
from collections import Counter
import asciitabconverter
from music21 import *



# functions

def openandread(tabpath):
    tabread = open(tabpath, 'r')
    tabfull = tabread.read()
    tabread.close()
    return tabfull;


def getguitarstyledata(rawtabread):

    # Function to produce list of noted in format string+fret, in the right playing order. Example: "D7" - this is: string D fret 7

    rawresults = []   #in this list we will place each fret line (block of 6 string lines) iteration, that will be dumped into the final resulting list with each 6 string iteration
    fullrawresults = []
    fullnotesonlyresults  = []
    expresionhammer = "h"
    expresionslide = "s"
    expresionbend = "b"
    expresionprebend = "pb"
    expresionpulloff = "p"
    expresionrelease = "r"
    countham = 0
    countslide = 0
    countbend = 0
    countprebend = 0
    countpullof = 0
    countrelease = 0
    flag = 0
    bar = 1

    tablinesraw = rawtabread.split("\n")
    for tline in tablinesraw:               #Let's iterate through each string and create the unsorted list of indexes + string + fret number

        if tline.startswith("e|") or tline.startswith("E|"):
                                            # Firt check if one fret line (a six string lines) has paased? If so, clear flag and increase bar counter, sort and dump the bar with indexes
            if (flag == 6):
                flag = 0
                bar += 1
                tupledresults = list(zip(rawresults[0::2], rawresults[1::2]))        # convert the list to a list of 2 elements (index, string+fret) from the temp rawresults list
                sortedtupledresults = sorted(tupledresults, key=lambda pos: pos[0])  # sort accoding to index
                notesonlysorted = [item[1] for item in sortedtupledresults]          # now that notes are sorted as they appear in the 6 string block, extract only notes from the list, remove indexes
                fullnotesonlyresults += notesonlysorted                              # add to the aglutinated list fullnotesonlyresults
                rawresults = []                                                      # reinit the temp list that will go changing with each iteration


            flag += 1                                           #increment flag that allow us to detect a bar - six string analyzed
            for m in re.finditer(expresionhammer, tline):
                countham += 1
            for m in re.finditer(expresionslide, tline):
                countslide += 1
            for m in re.finditer(expresionbend, tline):
                countbend += 1
            for m in re.finditer(expresionprebend, tline):
                countprebend += 1
            for m in re.finditer(expresionpulloff, tline):
                countpullof += 1
            for m in re.finditer(expresionrelease, tline):
                countrelease += 1

        if tline.startswith("B|"):
            # print(tline)
            flag += 1
            for m in re.finditer(expresionhammer, tline):
                countham += 1
            for m in re.finditer(expresionslide, tline):
                countslide += 1
            for m in re.finditer(expresionbend, tline):
                countbend += 1
            for m in re.finditer(expresionprebend, tline):
                countprebend += 1
            for m in re.finditer(expresionpulloff, tline):
                countpullof += 1
            for m in re.finditer(expresionrelease, tline):
                countrelease += 1

        if tline.startswith("G|"):
            flag += 1
            for m in re.finditer(expresionhammer, tline):
                countham += 1
            for m in re.finditer(expresionslide, tline):
                countslide += 1
            for m in re.finditer(expresionbend, tline):
                countbend += 1
            for m in re.finditer(expresionprebend, tline):
                countprebend += 1
            for m in re.finditer(expresionpulloff, tline):
                countpullof += 1
            for m in re.finditer(expresionrelease, tline):
                countrelease += 1

        if tline.startswith("D|"):
            flag += 1
            for m in re.finditer(expresionhammer, tline):
                countham += 1
            for m in re.finditer(expresionslide, tline):
                countslide += 1
            for m in re.finditer(expresionbend, tline):
                countbend += 1
            for m in re.finditer(expresionprebend, tline):
                countprebend += 1
            for m in re.finditer(expresionpulloff, tline):
                countpullof += 1
            for m in re.finditer(expresionrelease, tline):
                countrelease += 1

        if tline.startswith("A|"):
            flag += 1
            for m in re.finditer(expresionhammer, tline):
                countham += 1
            for m in re.finditer(expresionslide, tline):
                countslide += 1
            for m in re.finditer(expresionbend, tline):
                countbend += 1
            for m in re.finditer(expresionprebend, tline):
                countprebend += 1
            for m in re.finditer(expresionpulloff, tline):
                countpullof += 1
            for m in re.finditer(expresionrelease, tline):
                countrelease += 1

        #if 'E|' in tline:
        #   # print(tline)
        #   flag += 1
        #   for m in re.finditer(expresion, tline):
        #        rawresults += (m.start(), 'E'+m.group(0))       # create temp list with index  plus the string+fret
        #        print('Cuerda E - Detectado posicion', m.start(), " - nota: ", m.group(0))

    print('number of hammers: ', countham)
    print('number of slides: ', countslide)
    print('number of bends  : ', countbend)
    print('number of prebend: ', countprebend)
    print('number of pulloff: ', countpullof)
    print('number of releases: ', countrelease)

    return ;


def producesortedtablist(rawtabread):

    # Function to produce list of notes in format string+fret, in the right playing order. Example: "D7" - this is: string D fret 7
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




    rawresults = []   #in this list we will place each fret line (block of 6 string lines) iteration, that will be dumped into the final resulting list with each 6 string iteration
    fullrawresults = []
    fullnotesonlyresults  = []
    expresion = "[0-9][0-9]?"
    flag = 0
    bar = 1

    tablinesraw = rawtabread.split("\n")
    for tline in tablinesraw:               #Let's iterate through each string and create the unsorted list of indexes + string + fret number

        # Firt check if one fret line (a six string lines) has paased? If so, clear flag and increase bar counter, sort and dump the bar with indexes
        if (flag == 6):
            flag = 0
            bar += 1
            tupledresults = list(zip(rawresults[0::2], rawresults[1::2]))  # convert the list to a list of 2 elements (index, string+fret) from the temp rawresults list
            sortedtupledresults = sorted(tupledresults, key=lambda pos: pos[0])  # sort accoding to index
            notesonlysorted = [item[1] for item in
                               sortedtupledresults]  # now that notes are sorted as they appear in the 6 string block, extract only notes from the list, remove indexes
            fullnotesonlyresults += notesonlysorted  # add to the aglutinated list fullnotesonlyresults
            rawresults = []  # reinit the temp list that will go changing with each iteration

        if tline.startswith("e|") or tline.startswith("E|"):

            flag += 1                                           #increment flag that allow us to detect a bar - six string analyzed
            for m in re.finditer(expresion, tline):
                rawresults += (m.start() , 'e'+m.group(0))      # create temp list with index  plus the string+fret

        if tline.startswith("B|"):
            flag += 1

            for m in re.finditer(expresion, tline):
                rawresults += (m.start(), 'B'+m.group(0))        # create temp list with index  plus the string+fret

        if tline.startswith("G|"):
            # print(tline)
            flag += 1
            for m in re.finditer(expresion, tline):
                rawresults += (m.start(), 'G'+m.group(0))        # create list with index (incremented by bar so it does not overwritsess)  pplus the string+fret

        if tline.startswith("D|"):
            # print(tline)
            flag += 1
            for m in re.finditer(expresion, tline):
                rawresults += (m.start(), 'D'+m.group(0))       # create temp list with index  plus the string+fret

        if tline.startswith("A|"):
            # print(tline)
            flag += 1
            for m in re.finditer(expresion, tline):
                rawresults += (m.start(), 'A'+m.group(0))        # create temp list with index  plus the string+fret


    #it returns a string with notes separated by commas
    print("                                                  ")
    print("************mod producesortedtablist*************************************")
    print("Total number of notes: ", len(fullnotesonlyresults))
    print("Converted notes: ", fullnotesonlyresults)
    print("*******************************************************************")
    print("                                                  ")


    return fullnotesonlyresults;


def converttonotes (sequencedlist):
    #let's convert the ordered stream of string + fret list into s string of notes, comma separated
    stringpart = ""
    finalconvertednotes = ""
    estringdict = dict(
        {'0': 'E', '1': 'F', '2': 'Gb', '3': 'G', '4': 'Ab', '5': 'A', '6': 'Bb', '7': 'B', '8': 'C', '9': 'Db',
         '10': 'D', '11': 'Eb', '12': 'E', '13': 'F', '14': 'Gb', '15': 'G', '16': 'Ab', '17': 'A', '18': 'Bb',
         '19': 'B', '20': 'C', '21': 'Db', '22': 'D', '23': 'Eb', '24': 'E', '25': 'F', '26': 'Gb'})
    Bstringdict = dict(
        {'0': 'B', '1': 'C', '2': 'Db', '3': 'D', '4': 'Eb', '5': 'E', '6': 'F', '7': 'Gb', '8': 'G', '9': 'Ab',
         '10': 'A', '11': 'Bb', '12': 'B', '13': 'C', '14': 'Db', '15': 'D', '16': 'Eb', '17': 'E', '18': 'F',
         '19': 'Gb', '20': 'G', '21': 'Ab', '22': 'A', '23': 'Bb', '24': 'B', '25': 'C', '26': 'Db'})
    Gstringdict = dict(
        {'0': 'G', '1': 'Ab', '2': 'A', '3': 'Bb', '4': 'B', '5': 'C', '6': 'Db', '7': 'D', '8': 'Eb', '9': 'E',
         '10': 'F', '11': 'Gb', '12': 'G', '13': 'Ab', '14': 'A', '15': 'Bb', '16': 'B', '17': 'C', '18': 'Db',
         '19': 'D', '20': 'Eb', '21': 'E', '22': 'F', '23': 'Gb', '24': 'G', '25': 'Ab', '26': 'A'})
    Dstringdict = dict(
        {'0': 'D', '1': 'Eb', '2': 'E', '3': 'F', '4': 'Gb', '5': 'G', '6': 'Ab', '7': 'A', '8': 'Bb', '9': 'B',
         '10': 'C', '11': 'Db', '12': 'D', '13': 'Eb', '14': 'E', '15': 'F', '16': 'Gb', '17': 'G', '18': 'Ab',
         '19': 'A', '20': 'Bb', '21': 'B', '22': 'C', '23': 'Db', '24': 'D', '25': 'Eb', '26': 'E'})
    Astringdict = dict(
        {'0': 'A', '1': 'Bb', '2': 'B', '3': 'C', '4': 'Db', '5': 'D', '6': 'Eb', '7': 'E', '8': 'F', '9': 'Gb',
         '10': 'G', '11': 'Ab', '12': 'A', '13': 'Bb', '14': 'B', '15': 'C', '16': 'Db', '17': 'D', '18': 'Eb',
         '19': 'E', '20': 'F', '21': 'Gb', '22': 'G', '23': 'Ab', '24': 'A', '25': 'Bb', '26': 'B'})
    Estringdict = dict(
        {'0': 'E', '1': 'F', '2': 'Gb', '3': 'G', '4': 'Ab', '5': 'A', '6': 'Bb', '7': 'B', '8': 'C', '9': 'Db',
         '10': 'D', '11': 'Eb', '12': 'E', '13': 'F', '14': 'Gb', '15': 'G', '16': 'Ab', '17': 'A', '18': 'Bb',
         '19': 'B', '20': 'C', '21': 'Db', '22': 'D', '23': 'Eb', '24': 'E', '25': 'F', '26': 'Gb'})


    for element in sequencedlist:                   #each element is a string + fret number like "e10", string e, fret 10

        if element[0] == 'e':                         #we know we are in the string e, then convert fret to note
            fretnote = estringdict[element[1:]] + "," #call the dictionary with 2nd part of element
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'B':
            fretnote = Bstringdict[element[1:]] + ","
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'G':
            fretnote = Gstringdict[element[1:]] + ","
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'D':
            fretnote = Dstringdict[element[1:]] + ","
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'A':
            fretnote = Astringdict[element[1:]] + ","
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'E':
            fretnote = Estringdict[element[1:]] + ","
            finalconvertednotes = finalconvertednotes + fretnote

    tempo = finalconvertednotes.split(",")
    print("                                                  ")
    print("************mod converttonotes*************************************")
    print('Total number of notes: ', (len(tempo)-1))    #minus one, the string end in "," as per the definition built (maybe changed in future reviews)
    print ('Converted notes: ', tempo[:-1])             #we dont want to see the final empty one.
    print("*******************************************************************")
    print("                                                  ")

    #it returns a string with notes separated by commas
    return finalconvertednotes;




def converttomusic21 (sequencedlist):
    #let's convert the ordered string + fret list into a music21 tiny notation string
    # first from extract the string, and use to locate the right dict, then use the fret number to convert to the right note
    stringpart = ""
    finalconvertednotes = ""
    estringdict = dict(
        {'0': 'e', '1': 'f', '2': 'f#', '3': 'g', '4': 'g#', '5': 'a', '6': 'a#', '7': 'b', '8': 'c', '9': 'c#',
         '10': 'd', '11': 'd#', '12': "e'", '13': "f'", '14': "f'#", '15': "g'", '16' : "g'#", '17': 'a', '18': "a'#",
         '19': "b'", '20': "'c'", '21': "c'#", '22': "d'", '23': "d'#", '24': "e''", '25': "f''", '26': "f''#"})
    Bstringdict = dict(
        {'0': 'b', '1': 'c', '2': 'c#', '3': 'd', '4': 'd#', '5': 'e', '6': 'f', '7': 'f#', '8': 'g', '9': 'g#',
         '10': 'a', '11': 'a#', '12': "b'", '13': "c'", '14': "c'#", '15': "d'", '16': "d'#", '17': "e'", '18': "f'",
         '19': "f'#", '20': "g'", '21': "g'#", '22': "a'" ,'23': "a'#", '24': "b'" , '25': "C'", '26': "c'#"})
    Gstringdict = dict(
        {'0': 'g', '1': 'g#', '2': 'a', '3': 'a#', '4': 'b', '5': 'c', '6': 'c#', '7': 'd', '8': 'd#', '9': 'e',
         '10': 'f', '11': 'f#', '12': "g'", '13': "g'#", '14': 'a', '15': "a'#", '16': "b'", '17': "c'", '18': "c'#",
         '19': "d'", '20': "d'#", '21': "e'", '22': "f'", '23': "f'#", '24': "g''", '25': "g''#", '26': "a''"})
    Dstringdict = dict(
        {'0': 'd', '1': 'd#', '2': 'e', '3': 'f', '4': 'f#', '5': 'g', '6': 'g#', '7': 'a', '8': 'a#', '9': 'b',
         '10': 'c', '11': 'c#', '12': 'd', '13': "d'#", '14': "e'", '15': "f", '16': "f'#", '17': "g'", '18': "g'#",
         '19': "a'", '20': "a'#", '21': "b'", '22': "c'", '23': "c'#", '24': "d''", '25': "d''#", '26': "e''"})
    Astringdict = dict(
        {'0': 'a', '1': 'a#', '2': 'b', '3': 'c', '4': 'c#', '5': 'd', '6': 'd#', '7': 'e', '8': 'f', '9': 'f#',
         '10': 'g', '11': 'g#', '12': "a'", '13': "a'#", '14': "b'", '15': "c'", '16': "c'#" , '17': "d'", '18': "d'#",
         '19': "e'", '20': "f'", '21': "f'#", '22': "g", '23': "g'#", '24': "a''", '25': "a'#", '26': "b''"})
    Estringdict = dict(
        {'0': 'e', '1': 'f', '2': 'f#', '3': 'g', '4': 'g#', '5': 'a', '6': 'a#', '7': 'b', '8': 'c', '9': 'c#',
         '10': 'd', '11': 'd#', '12': "e'", '13': "f'", '14': "f'#", '15': "g'", '16': "g'#", '17': 'a', '18': "a'#",
         '19': "b'", '20': "'c'", '21': "c'#", '22': "d'", '23': "d'#", '24': "e''", '25': "f''", '26': "f''#"})

    print('list que entra a la funcion music21 ', sequencedlist)

    for element in sequencedlist:                   #each element is a string + fret number like "e10", string e, fret 10

        if element[0] == 'e':                         #we know we are in the string e, then convert fret to note
            fretnote = estringdict[element[1:]] + "4 " #call the dictionary with 2nd part of element
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'B':
            fretnote = Bstringdict[element[1:]] + "4 "
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'G':
            fretnote = Gstringdict[element[1:]] + "4 "
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'D':
            fretnote = Dstringdict[element[1:]] + "4 "
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'A':
            fretnote = Astringdict[element[1:]] + "4 "
            finalconvertednotes = finalconvertednotes + fretnote
        if element[0] == 'E':
            fretnote = Estringdict[element[1:]] + "4 "
            finalconvertednotes = finalconvertednotes + fretnote



    #it returns a string with notes separated by commas
    tempos = finalconvertednotes.split(" ")
    print("                                                  ")
    print("************mod convertomusic21*************************************")
    print('Total number of notes: ', (len(
        tempos) - 1))  # minus one, the string end in "," as per the definition built (maybe changed in future reviews)
    print('Converted notes: ', tempos[:-1])  # we dont want to see the final empty one.
    print("*******************************************************************")
    pathi = 'C:\\Users\\dmanerob\\Downloads\\Tabs\\MI.txt'
    f = open(pathi, 'w')
    f.write(finalconvertednotes)
    return finalconvertednotes;


def songstats (notelist):

    import collections

    templist = notelist.split(",")
    mostcommon = Counter(templist).most_common(15)
    print("  ")
    print("********************module songstats******************")
    print("Top 15 notes: ", mostcommon)

    #find phrases
    #compare phrases of lenght equal to variable phraselenght from all the notes in sequence

    songlenght=len(templist)
    pharselenght = 10
    phrasecount = {}
    for elements in range(0,songlenght):
        token = templist[elements:(pharselenght+elements)]
        #print("token ",elements, " --> ",token)
        tokenstr = repr(token)
        if tokenstr not in phrasecount:
            phrasecount[tokenstr]=1
        else:
            phrasecount[tokenstr] += 1


    print(" ")
    print('top #10 phrases of ',pharselenght," notes lenght (you can change this in var phraselenght)" )
    print(" "          )
    Tempus = collections.Counter(phrasecount)

    for word, count in Tempus.most_common(10):
    	print(word, ": ", count)



    print("xpe:  ",)
    maxi = max(phrasecount.items(), key=lambda k : k[1])
    print("top phrase: ", maxi[0])

    print("********************module songsmusic21stats******************")


def songstatsmusic21 (notelist):

    import collections

    print(" ")
    print("*******************mod songstatsmusic21**************************")
    temp = notelist.split(" ")
    commonnotes = Counter(temp).most_common(20)
    print ("Top 20 music21 notes: ", commonnotes)
    tnc = tinyNotation.Converter(notelist)
    tnc.parse()
    s = tnc.stream
    #s.plot('HistogramPitchSpace', title='Love of God - Steve Vai')
    print("Possible song Key: ", s.analyze('key'))
    #scales with whole note set
    print(" ")
    print("Scales and Modes:")
    print("----------------")
    #sc1 = scale.MajorScale()
    #print("Possible Major scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.DorianScale()
    #print("Possible Dorian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.PhrygianScale()
    #print("Possible Phrygian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.LydianScale()
    #print("Possible Lydian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.MixolydianScale()
    #print("Possible Mixolydian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.MinorScale()
    #print("Possible Aeolian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1 = scale.LocrianScale()
    #print("Possible Locrian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    #sc1=scale.WeightedHexatonicBlues()
    #print("Possible Blues Penta scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    print(" ")
    print(" ")

    # now let's find commmon phrases and its scales
    # we will create a dictionary, iterating through the notes
    #the pharse lenght can be modified in variable phraselenght
    songlenght = len(temp)
    pharselenght = 2
    phrasecount = {}
    for elements in range(0, songlenght):
        token = temp[elements:(pharselenght + elements)]
        # print("token ",elements, " --> ",token)
        tokenstr = repr(token)
        if tokenstr not in phrasecount:
            phrasecount[tokenstr] = 1
        else:
            phrasecount[tokenstr] += 1

    print(" ")
    print('top #10 phrases of ', pharselenght, " notes lenght (you can change this in var phraselenght)")
    print(" ")
    Tempus = collections.Counter(phrasecount)

    for word, count in Tempus.most_common(100):
        print(word, ": ", count)

    print(" ")
    maxi = max(phrasecount.items(), key=lambda k: k[1])
    print("Top phrase of ",pharselenght," notes is: ", maxi[0])
    #convert to string to find scale with music21
    temp1str = "".join(str(x) for x in maxi[0])
    temp2str = temp1str.replace(",","")
    temp3str = temp2str.replace("\"","")
    temp4str = temp3str.replace(" '"," ")
    temp5str = temp4str.replace("' "," ")
    temp6str = temp5str.replace("['","")
    temp7str = temp6str.replace("]","")
    temp8str = temp7str.replace("[", "")

    tempstr = temp8str
    print(">>>> ", tempstr)
    tnc2 = tinyNotation.Converter(tempstr)
    tnc2.parse()
    s = tnc.stream
    print("Possible Phrase Key: ", s.analyze('key'))
    # scales with whole note set
    print(" ")
    print("Scales and Modes:")
    print("----------------")
    sc1 = scale.MajorScale()
    print("Possible Major scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.DorianScale()
    print("Possible Dorian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.PhrygianScale()
    print("Possible Phrygian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.LydianScale()
    print("Possible Lydian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.MixolydianScale()
    print("Possible Mixolydian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.MinorScale()
    print("Possible Aeolian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1 = scale.LocrianScale()
    print("Possible Locrian scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    sc1=scale.WeightedHexatonicBlues()
    print("Possible Blues Penta scales:", sc1.deriveRanked(s, comparisonAttribute='name'))
    print(" ")
    print(" ")

    print(" ")
    print("********************module songstats******************")


#Main prog
#There we go

sampletabread = openandread('C:\\Users\\dmanerob\\Downloads\\Tabs\\tab.txt')  #Openfile
producedlist = producesortedtablist(sampletabread)                                #call function to produce list of noted in format string+fret, in the right playing order. Example: "D7" - this is: string D fret 7
convertedlist = converttonotes(producedlist)                                  #call function to convert to notes
convertedmusic21 = converttomusic21(producedlist)
#counterstechniques = getguitarstyledata(sampletabread)


#sample outputs for checking purposes
print(' ')
print('RESULTS:')
print('lista produced: ',producedlist)
print('lista converted: ',convertedlist)
print('lista music21: ',convertedmusic21)
print(' ')
print('---------------------------------')

#statistic
#songstats(convertedlist)
songstatsmusic21(convertedmusic21)
