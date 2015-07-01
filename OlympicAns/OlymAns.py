## 
# This program prompts the user for sentences that are then converted into trees that are then converted into SQL queries via semantic processing.
# THe program loops until until a sentence consisting solely of 'q' is inputted.
# 
# The load_parser function is picky about where it wants the fcfg file to be.  It will give you a warning that tells you where it is trying to search.
# (For some reason it checks multiple places, but doesn't include 'same directory as program' among the locations.)
# Created by Kyle Berry and Faisal Hasan Najar
##

import nltk
import pprint
import re
from nltk import *
from nltk.tree import *
from nltk.draw import tree
from nltk import load_parser
import sqlite3 as lite
import sys

#Opening SQL database
def readData():
    
    f = open('olympics-db-2014.sql', 'r')
    
    with f:
        data = f.read()
        return data
        
con = lite.connect(':memory:')

##This is the loop that parses the sentence and creates the query.
cur = con.cursor()
cp = load_parser('sql1.fcfg')
while True:
 #break
 with con:  
    rawtext = raw_input()  ##Read in data from user and returns it as a string.    
    n = rawtext
    if n.strip() == 'q':
        print 'Goodbye'
        break
        
    print 'Query: ' + rawtext    
        
    try:
      trees = cp.nbest_parse(rawtext.split())
    except ValueError:
      trees = []
      print 'Parsing Failed - Found word(s) not in grammar'

    rows = []      
    #print trees #<- Debugging code.
    if trees: #false if empty
        answer = str(trees[0].node['SEM'])
        answer = answer.replace(',','')
        answer = answer.replace('(','')
        answer = answer.replace(')','')    
        #print answer #<-Debugging code
    
        sql = readData()
        cur.executescript(sql)
    
        longJoin = "SELECT * FROM results INNER JOIN competitions ON results.comp_id = competitions.comp_id INNER JOIN athletes ON results.winner = athletes.name"
        print longJoin + ' WHERE ' + answer
        cur.execute("%s WHERE %s" % (longJoin, answer))

        rows = cur.fetchall()
        
    if 'Did' in rawtext:
        if rows:
            print 'Yes'
        else:
            print 'No'              
    if 'Who' in rawtext:
        if not rows:
            print 'No such contest and/or place'
        else:
            for row in rows:
                print row[1]
                
        #for row in rows:
            #print row