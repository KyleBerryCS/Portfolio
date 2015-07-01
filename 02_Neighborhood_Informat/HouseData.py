###############################################################
# Created by Kyle Berry
# 
# This code is not used by Neighbourhood Informant, as attempts
# to integrate it initially failed and our team decided it we had
# enough time to safely redo the back-end to C#.
#
# This code was also not finished (since it would never be used),
# but it is in this portfolio for completeness' sake.
#
# I guided my partners through implementing the back-end in C#,
# including the functions that I had yet to implement in the python code. 
# (I was unfamiliar with C#, so this largely took the form of me carefully
# describing what needed to be done and how I did/was going to do it, followed 
# by me answering any questions that came up due to differences between C# 
# and Python)
#
###############################################################

import json
import urllib
import pprint
import datetime
import re
import operator
from math import *
#from euclid import *
#from cyclops import *

#Get metadata for views in the Chicago data portal
#fileHandle = urllib.urlopen("http://data.cityofchicago.org/resource/ijzp-q8t2.json")
#views = json.loads((fileHandle.read()).decode('utf-8'))

# makes use of python utm converter from https://pypi.python.org/pypi/utm
#import utm

#Use Stored MetaData
#input_file  = open("rows.json")
#views = json.loads(input_file.read())



################
### Classes
################

class Community:
    #def __init__ (self, inName, inNum, inCrime, inTax, inSchool)
    def __init__ (self, inName, inNum):
        self.name = inName
        self.number = inNum
        self.streets = []
        self.crime = 0
        self.crimeTypes = []
        self.perCaptiaIncome = -1
        self.hardshipIndex = -1
        self.taxdata = [] ##[ [Fund], [Revenue], [Expenditures]]
        #self.schoolGeneral = inSchool
        self.schoolSpecific = []
        self.healthStatistics = []
    def __repr__(self):
        return repr((self.name, self.number, self.crime))  

class WildZone:
    def __init__ (self, inName, -1)
        self.name = inName
        self.number = inNum
        self.streets = []
        self.taxdata = []   
        
class CrimeStats:
    def __init__ (self, inType, inSeverity):
        self.type = inType
        self.severity = inSeverity
        self.lastDate = []
        
class SchoolStats:
    def __init__ (self, inName, inRating):
        self.Name = inName
        self.rating = inRating
        
class HealthStats:
    def __init__ (self):
        self.none = None
        
class TaxStats:
    def __init__ (self)
        self.totalRev = -1
        self.totalExp = -1
        self.startingBalance = -1
        self.RevList = []
        self.ExpList = []
    

##################
#Global Variables
##################
comNames =  [line.rstrip('\n') for line in open("ChicagoComNames.txt")]
communities = []
sortedCommunities = []
topX = []

for(counter, name) in enumerate(comNames):
    communities.append(Community(name, (counter+1)))

    
##########################################
# Methods for Manipulating/Printing Lists
##########################################
       
    
def createSortedList(value, reverseOrder): #This method is very unsafe - MAKE SURE INPUT IS CORRECT
    global sortedCommunities
    sortedCommunities = eval(("sorted(communities, key=lambda community: community." + value + ", reverse=" + str(reverseOrder) + ")"))

def createSortedByInnerList(value, otherValue): #So unsafe. Keep out of reach of children.  This one hasn't been tested, even. (NEEDS UPDATING)
    global sortedCommunities
    sortedCommunities = eval(("sorted(communities, key=lambda community: community." + value + "['" + otherValue + "'])"))
    
def createTopX(desiredSize): #desiredSize should be an int. If desired size > size of complete list, complete list is returned.
    global topX
    global sortedCommunities   
    topX = []
    for(counter, area) in enumerate(sortedCommunities):
        if(counter == desiredSize):
            break;
        topX.append(area)

def sortAndTopX(desiredSize, value, reverseOrder): #desiredSize should be an int, value should be a string
    createSortedList(value, reverseOrder)
    createTopX(desiredSize)
    
def returnAreaAt(aList, location):
    if (location < len(aList) and location > -1):
        return aList[location]
        
def returnValue(area, value): #unsaaaafeee
    return eval( ("area." + value))
    
def returnDeepValue(area, valueList):              ##Using Eval like this is not generally advisable, etc, etc. 
    for (counter, value) in enumerate(valueList):  ##Assumes each layer past the first is a list (unless the final value which may or may not be a list)
        if (counter == 0):
            currObj = eval( ("area." + value))
        else:
            currObj = eval( ("currObj[" + str(value) + "]"))
    print currObj #<---TEST CODE
    return currObj


def printComData(aList, aValue): #Unsafe method - aValue is assumed to be a parameter of community.
    print "---"
    for area in aList:
        print str(area.number) + ", " + area.name + ", " + str((eval("area." + str(aValue))))
    print "---"
    
def printRelevantComData(area, aValue): #Unsafe method - aValue is assumed to be a parameter of community.
    if(str((eval("area." + str(aValue)))) != str(-1)):
        print str(area.number) + ", " + area.name + ", " + str((eval("area." + str(aValue)))) 

def printDataAndOthers(aList, aValue, otherValues) #Other values is a list of path lists to needed vars.
    print "---"
    for area in aList:
        if(str((eval("area." + str(aValue)))) != str(-1)):
            print str(area.number) + ", " + area.name + ", " + str((eval("area." + str(aValue)))),
            for val in otherValues:
                if(str((eval("area." + str(val)))) != None and str((eval("area." + str(val)))) != str(-1)):
                    print str((str(returnDeepValue(area,val)))),
            print ""
    print "---"       
        
#############################################################
# Section that deals with compiling data to create summaries.
#############################################################

def runCrimeCompilationExample():
    f = open("ComCrimeExample.csv")
    for i, line in enumerate(f):
        entries = line.split(',')
        entries[-1] = entries[-1].rstrip() #I have no idea why I need to do this, or even what it is doing?!
        if(-1 < int(entries[0]) and int(entries[0]) < 77):
            communities[int(entries[0])].crime = communities[int(entries[0])].crime + 1
        if((i%1000000) == 0):
            print "Working...[" + str(i) + "]"

def runCensusDataCompilation():
    f = open("Census_Data.csv")
    for i, line in enumerate(f):
        if (i != 0):
            entries = line.split(',')
            entries[-1] = entries[-1].rstrip() #I have no idea why I need to do this, or even what it is doing?!
            if(-1 < int(entries[0]) and int(entries[0]) < 78):
                communities[(int(entries[0])-1)].perCaptiaIncome = int(entries[7])
                communities[(int(entries[0])-1)].hardshipIndex = int(entries[8])  
            if((int(entries[0]) -1) == 76):
               break; 

def runTaxDataCompilation():
    f = open("Tax_Data.csv")
    for i, line in enumerate(f):
        if (i != 0):
            entries = line.split(',')
            entries[-1] = entries[-1].rstrip() #I have no idea why I need to do this, or even what it is doing?!
            if( None != str(entries[1]) and None != str(entries[2]) and None != int(entries[4]):
                found = False
                for com in communities:
                    if (found != True):
                        for street in com.streets:
                            if (street.name == str(entries[1)):
                                found = True
                                    if len(street.name.taxdata) = 0):
                                        neoData = TaxStats()
                                        street.name.taxdata
                                        if(str(entries[2]) == "revenue")
                                            
                            
                communities[(int(entries[0])-1)].perCaptiaIncome = int(entries[7])
                communities[(int(entries[0])-1)].hardshipIndex = int(entries[8])  
            if((int(entries[0]) -1) == 76):
               break;     
               
##EXAMPLES! 
#communities[0].crimeTypes = [[1,2],[3,4],[5,('kittens', 1)]]
#returnDeepValue(communities[0], ['crimeTypes', 2, 1, 0]) 
       
runCrimeCompilationExample()
runCensusDataCompilation()

createSortedList("crime", "False")
printComData(sortedCommunities, "crime")
print "___________________"
printComData(communities, "perCaptiaIncome")
createTopX(10)
print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
printComData(topX, "crime")
print "___________________"
createSortedList("perCaptiaIncome", "True")
printComData(communities, "perCaptiaIncome")
printComData(sortedCommunities, "perCaptiaIncome")

    
def crimeCounts():
    for crime in Crimes:
        yes = None

##############################
# Section that deals with loading in previously compiled data
#
##############################

##############################
# Section that deals with retrieving data
#
##############################

#def searchForCrimeData(): 


def testPrinting():
    for area in communities:
        print area.name
        print area.number
        print area.crime
    

####################
# Program Interface
####################