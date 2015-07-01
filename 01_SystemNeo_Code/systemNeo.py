######################################################
#
# The project builds upon the initial framework 
# developed by Andrew Johnson for use by his students. 
# Copyright 2013 Andrew Johnson, evl, uic
# 
# The vast majority of this code was written by Kyle Berry,
# See "system.py" for initial code written by Andrew Johnson.
#
# This program was designed to be used by the UIC CAVE.
# 
# This program allows small multiples of exoplantary systems to
# be shown on the walls of the cave, and allows the comparison 
# of one or more systems in 3D in the center of the CAVE.
#
# The program also allows for 3D viewing of all of the stars that
# have known exoplanets, allowing the relative distances
# between the various systems to be view.
#
# This program was written in 2013. Its comments are less
# extensive than they should have been, and code I write
# for a company today would pay far more attention to the
# need for other people to be able to easily understand
# what is going on in my code.
######################################################

from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *
from time import *
from CoordinateCalculator import CoordinateCalculator


# V main sequence (O B A F G K M etc)
# III Giants (G K M)
# I super giants (B A F G K M)
# main sequence stars become brighter and hotter as they age
#
# good source of textures
# http://www.celestiamotherlode.net
#
# http://kepler.nasa.gov/multimedia/artwork/diagrams/?ImageID=245
# earth-size < 1.25 Rearth
# super earth-size 1.25 - 2 Rearth
# neptune-size 2 - 6 Rearth
# jupiter-size  6 - 15 Rearth
# larger than jupiter-size > 15 Rearth
#
# 1AU = 149597871 km
# 0.00315 Mj = One Earth Mass.  Super Earths 2-10 earth masses, so up to 0.0315 Mj
# Neptune size is up to 30 earths, so up to ????

# some hard coded data to start with

#name :(radius on km, orbit in km, texture, year, day, sun/planet, axial rotation, star type

###
allImages = [[],[],[],[]]

# Solar Body Class
class aSystem:
  def __init__(self):
   self.name = None
   self.declination = []
   self.rightAscension = []
   self.distance = 0
   self.numStars = 0
   self.numPlanets = 0
   self.terPlanetsInHabitableZone = 0
   self.gasPlanetsInHabitableZone = 0
   self.terPlanets = 0
   self.gasPlanets = 0
   self.StarTemps = []
   self.binaries = []
   self.stars = []
   self.planets = []
   self.flags = []
   self.needsData = 0
   #used for graphs
   self.ignore = 1
  
class aBinary:
  def __init__(self):
   self.semimajoraxis = None
   self.inclination = None
   self.period = None
   self.eccentricity = None
   self.semiLatusRectum = None
   self.periastron = None
   self.binaries = []
   self.stars = []
   self.planets = []  

class aStar:
  def __init__(self):
   self.name = None
   self.mass = None
   self.radius = None
   self.eccentricity = 0
   self.semimajoraxis = None
   self.periastron = 0
   self.temperature = None
   self.spectralType = None
   self.texture = None
   self.inclination = 0
   self.semiLatusRectum = None
   self.planets = []
   self.notes = []

class aPlanet:
  def __init__(self):
   self.name = []
   self.mass = None
   self.radius = None
   self.period = None
   self.eccentricity = None
   self.inclination = None
#   self.period = None
   self.texture = None
   self.discoverymethod = None
   self.discoveryyear = None
   self.semiLatusRectum = None
   self.periastron = None
   self.planets = []
   self.notes = []
   self.isGas = None

class aRotObject:
  def __init__(self):
   self.SceneNode = None
   self.period = None
   self.solarObject = None
   self.P = 0
   self.E = 0
   
########################
# XML file Acquisition
########################

import xml.etree.ElementTree as ET

tree = ET.parse('systems.xml')
root = tree.getroot()
allSystems = []


def fillSystem(xmlNode):
    global allSystems
    currSystem = aSystem()
    #Create instance of class
    #Name
    if(xmlNode.find('name') != None):
      currSystem.name = xmlNode.find('name').text
    else:
      currSystem.name = "Unnamed"
     
    #Distance 
    if(xmlNode.find('distance') != None):
       currSystem.distance = float(xmlNode.find('distance').text)
    else:
      currSystem.distance = 0
      currSystem.needsData = 1
      currSystem.flags.append('noDistance')
    
    #Right Ascension    
    if(xmlNode.find('rightascension') != None):
       theRightAscension = xmlNode.find('rightascension').text
       currSystem.rightAscension = theRightAscension.split()
    else:
      currSystem.rightAscension = None
      currSystem.needsData = 2
      currSystem.flags.append('noRightAscension')     
      
    #declination   
    if(xmlNode.find('declination') != None):
       theDeclination = xmlNode.find('declination').text
       currSystem.declination = theDeclination.split()
    else:
      currSystem.declination = None
      currSystem.needsData = 3
      currSystem.flags.append('noDeclination')     
    
     
    #Add instance to class
    allSystems.append(currSystem)

     
def fillStar(xmlNode, index, binIndex, semimajoraxis, innerBinIndex):
    global allSystems 
    allSystems[index].numStars = allSystems[index].numStars + 1    
    currStar = aStar()
    #Create instance of class
    #Name
    
    currStar.needsData = 0
    if(xmlNode.find('name') != None):
       currStar.name = xmlNode.find('name').text
    else:
       currStar.name = "Unnamed"    
     
    #mass
    if(xmlNode.find('mass') != None):
       currStar.mass = float(xmlNode.find('mass').text)
    else:
      currStar.mass = 1
      currStar.needsData = currStar.needsData + 1
     
    #radius
    if(xmlNode.find('radius') != None):
       currStar.radius = float(xmlNode.find('radius').text)
    else:
      currStar.radius = 1
      currStar.needsData = currStar.needsData + 3
         
    #spectraScopy
    if(xmlNode.find('spectraltype') != None):
       currStar.spectralType = xmlNode.find('spectraltype').text
    else:
      currStar.spectralType = "Unkown"
      currStar.needsData = currStar.needsData + 5

    #temp
    if(xmlNode.find('temperature') != None):
       currStar.temperature = float(xmlNode.find('temperature').text)
    else:
        if currStar.spectralType.find('A')!=-1 :
            currStar.temperature = 8750
        elif currStar.spectralType.find('F')!= -1 :
            currStar.temperature = 6750
        elif currStar.spectralType.find('G')!=-1 :
            currStar.temperature = 5600
        elif currStar.spectralType.find('K')!=-1 :
            currStar.temperature = 4450
        elif currStar.spectralType.find('M')!=-1 :
            currStar.temperature = 3500
        elif currStar.spectralType.find('O')!=-1 :
            currStar.temperature = 33000  
        elif currStar.spectralType.find('B')!=-1 :
            currStar.temperature = 21000 
        elif currStar.spectralType.find('T')!=-1:
            currStar.temperature = 900        
        else:
            currStar.temperature = 200
        currStar.needsData = currStar.needsData + 10
    
    #semimajoraxis
    currStar.semimajoraxis = semimajoraxis
    if(semimajoraxis != None and semimajoraxis != 0):
     currStar.semiLatusRectum = currStar.semimajoraxis - (currStar.semimajoraxis * (currStar.eccentricity * currStar.eccentricity))    
    else:
     currStar.semiLatusRectum = 0
    #Try to guestemate missing data
    #add Sun
    
    if(currStar.name == "Sun"):
       currStar.texture = "sol.png"
    elif currStar.spectralType.find('A')!=-1 :
        currStar.texture = "astar.jpg"
    elif currStar.spectralType.find('F')!=-1 :
        currStar.texture = "fstar.png"
    elif currStar.spectralType.find('G')!=-1 :
        currStar.texture = "gstar.png"
    elif currStar.spectralType.find('K')!=-1 :
        currStar.texture = "kstar.png"
    elif currStar.spectralType.find('M')!=-1 :
        currStar.texture = "mstar.png"
    elif currStar.spectralType.find('O')!=-1 :
        currStar.texture = "ostar.png"  
    elif currStar.spectralType.find('B')!=-1 :
        currStar.texture = "bstar.png" 
    elif currStar.spectralType.find('T')!=-1:
        currStar.texture = "Tstar.png"         
    else:
        currStar.texture = "green.jpg"
    
    if(binIndex == -1):
       allSystems[index].stars.append(currStar)
    if(binIndex != -1 and innerBinIndex == -1):
       allSystems[index].binaries[binIndex].stars.append(currStar)   
    if(binIndex != -1 and innerBinIndex != -1):
       allSystems[index].binaries[binIndex].binaries[innerBinIndex].stars.append(currStar)        

def fillPlanet(xmlNode, index, binIndex, starIndex, innerBinIndex):
    global allSystems
    allSystems[index].numPlanets = allSystems[index].numPlanets + 1
    currPlanet = aPlanet()
    #Create instance of class
    #Name
    currPlanet.needsData = 0
    
    #Name (Some planets have more than one name)
    if(xmlNode.find('name') != None):
       for name in xmlNode.findall('name'):
         currPlanet.name.append(name.text)
    else:
       currPlanet.name.append("Unnamed")
    
    #mass
    if(xmlNode.find('mass') != None):
     if(xmlNode.find('mass').text != None):
       currPlanet.mass = float(xmlNode.find('mass').text)
     else:
       currPlanet.mass = 1
       currPlanet.needsData = currPlanet.needsData + 1       
    else:
      currPlanet.mass = 1
      currPlanet.needsData = currPlanet.needsData + 1
     
    #radius
    if(xmlNode.find('radius') != None):
       currPlanet.radius = float(xmlNode.find('radius').text)
    else:
      currPlanet.radius = 1
      currPlanet.needsData = currPlanet.needsData + 3

    #semimajoraxis
    if(xmlNode.find('semimajoraxis') != None):
       currPlanet.semimajoraxis = float(xmlNode.find('semimajoraxis').text)
    else:
       currPlanet.semimajoraxis = 1000
       currPlanet.needsData = currPlanet.needsData + 5
    
    #eccentricity
    if(xmlNode.find('eccentricity') != None):
      if(xmlNode.find('eccentricity').text != None):
       currPlanet.eccentricity = float(xmlNode.find('eccentricity').text)
      else:
       currPlanet.eccentricity = 0
    else:
       currPlanet.eccentricity = 0
       
     #periastron
    if(xmlNode.find('periastron') != None):
      if(xmlNode.find('periastron').text != None):
       currPlanet.periastron = float(xmlNode.find('periastron').text)
      else:
       currPlanet.periastron = (1-currPlanet.eccentricity)*currPlanet.semimajoraxis
    else:
       currPlanet.semimajoraxis = (1-currPlanet.eccentricity)*currPlanet.semimajoraxis     
    
    #period
    if(xmlNode.find('period') != None):
       currPlanet.period = float(xmlNode.find('period').text)
    else:
       currPlanet.period = 365
       currPlanet.needsData = currPlanet.needsData + 200 
 
    #inclination
    if(xmlNode.find('inclination') != None):
       if(xmlNode.find('inclination').text != None):
         currPlanet.inclination = float(xmlNode.find('inclination').text)*0.0174532925
       else:
         currPlanet.inclination = 0
    else:
       currPlanet.inclination = 0
 
    #description
    if(xmlNode.find('description') != None):
       currPlanet.description = xmlNode.find('description').text
    else:
       currPlanet.description = "No Description Available"
       #currPlanet.needsData = currPlanet.needsData + 100
     
    #discoverymethod
    if(xmlNode.find('discoverymethod') != None):
       currPlanet.discoverymethod = xmlNode.find('discoverymethod').text
    else:
       currPlanet.discoverymethod = "No Discovery Method Data Available"
       #currPlanet.needsData = currPlanet.needsData + 100
     
    #discoveryyear
    if(xmlNode.find('discoveryyear') != None):
       currPlanet.discoveryyear = xmlNode.find('discoveryyear').text
    else:
       currPlanet.discoveryyear = "No Discovery Year Data Available"
       #currStar.needsData = currStar.needsData + 100
     
    #temp
    if(xmlNode.find('temperature') != None):
       currPlanet.temperature = float(xmlNode.find('temperature').text)
    else:
       currPlanet.temperature = None
       currPlanet.needsData = currPlanet.needsData + 10
     
    if(currPlanet.needsData == 1): #Only Mass is missing  FIIIIIIIIIIIIIIIIIIIIIIIIIIX
     if(currPlanet.radius <= 1.25): #About Earth-Sized
        currPlanet.mass = (0.00315*1.25) * (currPlanet.radius/1.25)        ############################
     if(currPlanet.radius > 1.25 and currPlanet.radius <= 2): #is a superEarth
        currPlanet.mass = (0.00315*10) * ((currPlanet.radius - 1.25)/0.75) ###############################SHOULD PROBABLY NOT BE LINEAR
     if(currPlanet.radius > 2 and currPlanet.radius <= 3): #is a mini-Neptune
        currPlanet.mass = (0.00315*15) * ((currPlanet.radius - 2))    
     if(currPlanet.radius > 3 and currPlanet.radius <= 6): #is Neptune-sized
        currPlanet.mass = (0.00315*30) * ((currPlanet.radius - 3)/3)     
     if(currPlanet.radius > 6 and currPlanet.radius <= 15): #is Jupiter-sized
        currPlanet.mass = (0.00315*300) * ((currPlanet.radius - 6)/9)
     if(currPlanet.radius > 15): #is a super-Jupiter
        currPlanet.mass = (0.00315*300) * ((currPlanet.radius - 15)*(currPlanetRadius))  ####USE EQUATION OF A SPHERE         

    if(currPlanet.needsData == 3): #Only Radius is Missing
      if(currPlanet.mass <= (0.00315*2)): #About Earth-Sized
        currPlanet.radius = 2 * (currPlanet.mass / (0.00315 * 2))          ############################
      else:
        if(currPlanet.mass <= (0.00315*10)): #Super Earth
           currPlanet.radius = 1.75        ############################        
        else:
           if(currPlanet.mass <= (0.00315*15)): #About Mini-Neptune
              currPlanet.radius = 2.5 
           else:
              if(currPlanet.mass <= (0.00315*30)): #About Neptune
                 currPlanet.radius = 4.5
              else:
                 if(currPlanet.mass <= (0.00315*300)): #About Jupiter
                    currPlanet.radius = 10.5
                 else:
                    if(currPlanet.mass > (0.00315*300)): #Super-Jupiter
                       currPlanet.radius = 18
    if(currPlanet.needsData == 4): #Both Mass and Radius is missing
      currPlanet.Radius = 1
      currPlanet.Mass = 1
      currPlanet.texture = "QM.png" 
    elif(currPlanet.name[0] == "Mercury"):
       allSystems[index].terPlanets = allSystems[index].terPlanets + 5   
       currPlanet.texture = "mercury.jpg"
       currPlanet.isGas = 0
    elif(currPlanet.name[0] == "Venus"):
       currPlanet.texture = "venus.jpg"  
       currPlanet.isGas = 0
    elif(currPlanet.name[0] == "Earth"):
       currPlanet.texture = "earthmap.jpg" 
       currPlanet.isGas = 0
    elif(currPlanet.name[0] == "Mars"):
       currPlanet.texture = "mars.png"
       currPlanet.isGas = 0      
    elif(currPlanet.name[0] == "Jupiter"):
       allSystems[index].gasPlanets = allSystems[index].gasPlanets + 4   
       currPlanet.texture = "jupiter.jpg" 
    elif(currPlanet.name[0] == "Neptune"):
       currPlanet.texture = "neptune.jpg"
    elif(currPlanet.name[0] == "Uranus"):
       currPlanet.texture = "uranus.jpg"  
    elif(currPlanet.name[0] == "Saturn"):
       currPlanet.texture = "saturn.png"  
    elif(currPlanet.mass <= 0.000315): 
       allSystems[index].terPlanets = allSystems[index].terPlanets + 1
       currPlanet.texture = "mercury.jpg"
       currPlanet.isGas = 0     
    elif(currPlanet.mass <= (0.00315*2)): #About Earth-Sized
       allSystems[index].terPlanets = allSystems[index].terPlanets + 1
       currPlanet.texture = "kcloud.png"
       currPlanet.isGas = 0       
    elif(currPlanet.mass <= (0.00315*10)): #Super Earth 
       allSystems[index].terPlanets = allSystems[index].terPlanets + 1
       currPlanet.texture = "searth.png" 
       currPlanet.isGas = 0      
    elif(currPlanet.mass <= (0.00315*15)): #About Mini-Neptune
       allSystems[index].gasPlanets = allSystems[index].gasPlanets + 1    
       currPlanet.texture = "uranus.jpg"
       currPlanet.isGas = 1     
    elif(currPlanet.mass <= (0.00315*30)): #About Neptune
       allSystems[index].gasPlanets = allSystems[index].gasPlanets + 1    
       currPlanet.texture = "neptune.jpg"
       currPlanet.isGas = 1       
    elif(currPlanet.mass <= (0.00315*300)): #About Jupiter
       allSystems[index].gasPlanets = allSystems[index].gasPlanets + 1    
       currPlanet.texture = "jupiter.jpg"
       currPlanet.isGas = 1      
    elif(currPlanet.mass > (0.00315*300)): #Super-Jupiter
       allSystems[index].gasPlanets = allSystems[index].gasPlanets + 1   
       currPlanet.texture = "Bdwarf.png"
       currPlanet.isGas = 1      
    else:  
       currPlanet.texture = "QM.png"
       currPlanet.isGas = 2      

    currPlanet.semiLatusRectum = currPlanet.semimajoraxis - (currPlanet.semimajoraxis * (currPlanet.eccentricity * currPlanet.eccentricity))          
    if(binIndex == -1 and starIndex == -1): #Lone Planet
      allSystems[index].planets.append(currPlanet)
    if(binIndex == -1 and starIndex != -1): #Planet Orbiting a star
      allSystems[index].stars[starIndex].planets.append(currPlanet)      
    if(binIndex != -1 and starIndex == -1 and innerBinIndex == -1): #Planet is Orbiting a binary
      allSystems[index].binaries[binIndex].planets.append(currPlanet)
    if(binIndex != -1 and starIndex == -1 and innerBinIndex != -1): #Planet is Orbiting a binary inside a binary
      allSystems[index].binaries[binIndex].binaries[innerBinIndex].planets.append(currPlanet)
    if(binIndex != -1 and starIndex != -1): #Planet is Orbiting a specific star (that is a part of a binary)
      allSystems[index].binaries[binIndex].stars[starIndex].planets.append(currPlanet)
      
def fillBinary(xmlNode, index, binIndex):
   global allSystems    
   currBinary = aBinary()
   #semimajoraxis
   if(xmlNode.find('semimajoraxis') != None):
       currBinary.semimajoraxis = float(xmlNode.find('semimajoraxis').text)
   else:
       currBinary.semimajoraxis = 100    

   #eccentricity
   if(xmlNode.find('eccentricity') != None):
      if(xmlNode.find('eccentricity').text != None):
       currBinary.eccentricity = float(xmlNode.find('eccentricity').text)
      else:
       currBinary.eccentricity = 0
   else:
       currBinary.eccentricity = 0
       
   #periastron
   if(xmlNode.find('periastron') != None):
      if(xmlNode.find('periastron').text != None):
       currBinary.periastron = float(xmlNode.find('periastron').text)
      else:
       currBinary.periastron = (1-currBinary.eccentricity)*currBinary.semimajoraxis
   else:
       currBinary.periastron = (1-currBinary.eccentricity)*currBinary.semimajoraxis 

    #period
   if(xmlNode.find('period') != None):
       currBinary.period = float(xmlNode.find('period').text)
   else:
      currBinary.period = 365
      
    #inclination
   if(xmlNode.find('inclination') != None):
      if(xmlNode.find('inclination').text != None):
         currBinary.inclination = float(xmlNode.find('inclination').text)*0.0174532925
      else:
         currBinary.inclination = 0
   else:
       currBinary.inclination = 0      

   currBinary.semiLatusRectum = currBinary.semimajoraxis - (currBinary.semimajoraxis * (currBinary.eccentricity * currBinary.eccentricity))          
   if(binIndex == -1):
      allSystems[index].binaries.append(currBinary)
   if(binIndex != -1):
      allSystems[index].binaries[binIndex].binaries.append(currBinary)
    
            
    
def binaryDelve(binary, index, binIndex, innerBinIndex):
   starIndex = -1
   for binStar in binary.findall('star'):
       starIndex = starIndex + 1
       if(binary.find('semimajoraxis') != None):
         semiMajAxis = float(binary.find('semimajoraxis').text)
       else:
         semiMajAxis = 0
       fillStar(binStar, index, binIndex, semiMajAxis, innerBinIndex)
  
       for binStarPlanet in binStar.findall('planet'):
          fillPlanet(binStarPlanet, index, binIndex, starIndex, innerBinIndex)
   
   for binPlanet in binary.findall('planet'):
       fillPlanet(binPlanet, index, binIndex, -1, innerBinIndex)
   
   for binBinary in binary.findall('binary'):
     innerBinIndex = innerBinIndex + 1   
     fillBinary(binary, index, binIndex)
     binaryDelve(binBinary, index, binIndex, innerBinIndex)
   #clipping##################################################################################################

   
index = -1
for system in root.findall('system'):
  index = index + 1
  binIndex = -1
  starIndex = -1
  fillSystem(system)  
  for star in system.findall('star'):
    starIndex = starIndex + 1
    fillStar(star, index, binIndex, 0, -1)
    for starPlanet in star.findall('planet'):
     fillPlanet(starPlanet, index, binIndex, starIndex, -1)
  for planet in system.findall('planet'):
    fillPlanet(planet, index, binIndex, -1, -1)
  for binary in system.findall('binary'):
    binIndex = binIndex + 1
    fillBinary(binary, index, -1)
    binaryDelve(binary, index, binIndex, -1)     
 


#6371
# 149597871


# if we only know mass we can get a very rough estimate of radius
# but a gaseous planet will have a larger radius than same mass rocky planet
#
# earth-sized   ( < 1.25 X radius of earth)  < 2 times  mass of the earth
# super earth   (1.25 - 2 X radius of earth) 2 -  5 times mass of earth
# mini-neptune  ( 2- 3 x radius of earth)    5 - 10 times mass of earth
# neptune sized ( 3 - 6 X radius of earth)   10 - 30 times mass of earth
# jupiter sized ( 6 - 15 X radius of earth)  30 - 300 times mass of earth
# super-jupiter ( > 15 X radius of earth)    >300 times mass of earth

#currentSystem = allPlanetarySystems[0]


##########################################################
#Various Initializations for Scene Nodes, Containers, Etc
##########################################################
#This section needs to be trimmed, some of these aren't used anymore.

# set up to rotate and revolve the suns and planets
activePlanets = {}
activeRotCenters = {}

# set up the initial scene hierarchy
everything = SceneNode.create('everything')
solarSystem = SceneNode.create('solarSystem')
thingsOnTheWall = SceneNode.create('thingsOnTheWall')
displayedSystems = SceneNode.create('displayedSystems')

everything.addChild(thingsOnTheWall)
everything.addChild(solarSystem)
thingsOnTheWall.addChild(displayedSystems)

##Wall and Menu paging##
ui = UiModule.createAndInitialize()
wf = ui.getWidgetFactory()
uiroot = ui.getUi()
centerChoicePage = 0


# Create a directional light
light1 = Light.create()
light1.setLightType(LightType.Point)
light1.setColor(Color(1.0, 1.0, 1.0, 1.0))
#light1.setPosition(Vector3(0.0, 1.5, 1.0))
light1.setPosition(Vector3(0.0, 0.0, 0.0))
light1.setEnabled(True)

# would be nice to have the light stay with the position of the sun
# for now it stays in the center of the cave
# would also be nice to change the light colour to match the star
everything.addChild(light1)

# need to compute goldilocks zone off the type or luminosity of the particular star
# by default set it to Sol
AUtoKM = 149597871
habInner = 0.95
habOuter = 1.4
habCenter = 0.5 * (habInner + habOuter)


# http://exoplanet.eu/catalog/

#######################################################################

def addOrbit(orbit, col, thick, solarObject):
    circle = LineSet.create()
    p = solarObject.semiLatusRectum
    e = solarObject.eccentricity    

    segments = 128
    radius = 1
    thickness = thick   #0.01 for orbit
    a = 0.0
    if(solarObject.semimajoraxis != 0):
      while a <= 360:       
        dist = (p / (1 - e*cos(radians(a)))) *orbitScaleFactor*userScaleFactor
        x = dist * cos(radians(a))
        y = dist * sin(radians(a))
        a += 360.0 / segments 
        dist = (p / (1 - e*cos(radians(a)))) *orbitScaleFactor*userScaleFactor        
        nx = dist * cos(radians(a))
        ny = dist * sin(radians(a))
    
        l = circle.addLine()
        l.setStart(Vector3(x, 0, y))
        l.setEnd(Vector3(nx, 0, ny))
        l.setThickness(thickness)
        
      circle.setPosition(Vector3(0, 2, -4))
        
      if col == 0:
            circle.setEffect('colored -e white')
      else:
            circle.setEffect('colored -e green')

      # Squish z to turn the torus into a disc-like shape.

      if col == 0:
            circle.setScale(Vector3(1, 1000.0, 1))
      else:
            circle.setScale(Vector3(1, 10.0, 1)) # 0.1
     # circle.yaw(solarObject.periastron)            
      if(solarObject.inclination != 0):
        circle.roll(-(solarObject.inclination))
      solarSystem.addChild(circle)
   # if(solarObject.semimajoraxis != 0):
    #      print("----------------->" +solarObject.name[0])
     #     sleep(3)

#######################################################################
# assuming main sequence (V):
# (O)                 - > 16 solar masses         - > 6.6 * Rsun        - blue
# (B)                 - 2.1 to 16 solar masses    - 1.8 to 6.6 * Rsun   - blue
# (A) 8.5 to 12.5 AU  - 1.4 to 2.1 solar masses   - 1.4 to 1.8 * Rsun   - white
# (F) 1.5 to 2.2 AU   - 1.04 to 1.4 solar masses  - 1.15 to 1.4 * Rsun  - yellow/white
# (G) 0.95 to 1.4 AU  - 0.8 to 1.04 solar masses  - 0.96 to 1.15 * Rsun - yellow
# (K) 0.38 to 0.56 AU - 0.45 to 0.8 solar masses  - 0.7 to 0.96 * Rsun  - orange
# (M) 0.08 to 0.12 AU - < 0.45 solar masses       - < 0.7 * Rsun        - red
#
# http://www.astronomy.ohio-state.edu/~pogge/Ast141/Unit5/Lect34_StarHZ.pdf
# dInner = 0.95AU * sqrt (L / Lsol)
# dOuter = 1.4AU * sqrt (L / Lsol)
#
# another method uses luminosity
# sun has habitable zone centered at 1.34 AU
# sqrt (luminoisty of star / luminosity of sun) * 1.34 AU
#
# http://www.planetarybiology.com/calculating_habitable_zone.htm
# has inner = sqrt (Lstar / 1.1) and outer = sqrt (Lstar / 0.53)
# for sun then inner = 1.09 AU and outer = 1.37 AU

def setHabZone (starType):
    global habInner
    global habOuter
    global AUtoKM
    global habCenter

    if starType.find('A')!=-1 :
        habInner = 8.5
        habOuter = 12.5
    elif starType.find('F')!=-1 :
        habInner = 1.5
        habOuter = 2.2
    elif starType.find('G')!=-1 :
        habInner = 0.95
        habOuter = 1.4
    elif starType.find('K')!=-1 :
        habInner = 0.38
        habOuter = 0.56
    elif starType.find('M')!=-1 :
        habInner = 0.08
        habOuter = 0.12
    else:
        habInner = 0
        habOuter = 0
        
    habCenter = (habInner + habOuter) * 0.5

#Used for the wall
thabInner = 0
thabOuter = 0
def tempHabZone (starType):
    global thabInner
    global thabOuter    
    if starType.find('A')!=-1 :
        thabInner = 8.5
        thabOuter = 12.5
    elif starType.find('F')!=-1 :
        thabInner = 1.5
        thabOuter = 2.2
    elif starType.find('G')!=-1 :
        thabInner = 0.95
        thabOuter = 1.4
    elif starType.find('K')!=-1 :
        thabInner = 0.38
        thabOuter = 0.56
    elif starType.find('M')!=-1 :
        thabInner = 0.08
        thabOuter = 0.12
    else:
        thabInner = 0
        thabOuter = 0
        
    thabCenter = (thabInner + thabOuter) * 0.5
#######################################################################


############################
#Creating the Center System
############################
allRotCenters = []            
currentSystems = []
for system in allSystems:
  currentSystems.append(system)

def createStar(currStar, theRotCenter):
            global activePlanets
            global allRotCenters
            model = StaticObject.create("defaultSphere")
            model.setPosition(Vector3(0.0, 1000.0, -currStar.semimajoraxis*orbitScaleFactor*userScaleFactor))
            model.setScale(Vector3(currStar.radius*sunScaleFactor, currStar.radius*sunScaleFactor, currStar.radius*sunScaleFactor))
            print("--------------------->", sunScaleFactor)
            sunDot = SphereShape.create(10/(-currStar.radius*sunScaleFactor), 2)
            sunDot.setPosition(Vector3(0.0, 1000/(-currStar.radius*sunScaleFactor), 0))
            model.addChild(sunDot)

            sunLine = LineSet.create()

            l = sunLine.addLine()
            l.setStart(Vector3(0, 1000/(-currStar.radius*sunScaleFactor), 0))
            l.setEnd(Vector3(0, 0, 0))
            l.setThickness(1/(currStar.radius*sunScaleFactor))
            sunLine.setEffect('colored -e white')
            model.addChild(sunLine)
            
            model.getMaterial().setProgram("textured")
            model.setEffect("textured -v emissive -d %s" % currStar.texture)
            activePlanets[currStar.name] = model
            
            # deal with the axial tilt of the sun & planets
            tiltCenter = SceneNode.create(currStar.name +"TiltCenter")
            tiltCenter.addChild(model)
            tiltCenter.roll(1/180.0*pi) 

            addOrbit(currStar.semimajoraxis*orbitScaleFactor*userScaleFactor, 0, 0.01, currStar)   
            theRotCenter.SceneNode.addChild(tiltCenter) 
            theRotCenter.P = currStar.semiLatusRectum 
            theRotCenter.E = currStar.eccentricity 
            theRotCenter.solarObject = model
            allRotCenters.append(theRotCenter)            

def createPlanet(currPlanet, theRotCenter):
            global activePlanets
            global allRotCenters
            model = StaticObject.create("defaultSphere")
            model.setPosition(Vector3(0.0, 1000.0, -currPlanet.semimajoraxis*orbitScaleFactor*userScaleFactor))
            model.setScale(Vector3(currPlanet.radius*planetScaleFactor, currPlanet.radius*planetScaleFactor, currPlanet.radius*planetScaleFactor))

            model.getMaterial().setProgram("textured")
            model.setEffect("textured -v emissive -d %s" % currPlanet.texture)
            activePlanets[currPlanet.name[0]] = model    
            
            orbitDot = SphereShape.create(10/(currPlanet.radius*planetScaleFactor), 2)
            orbitDot.setPosition(Vector3(0.0, 1000/(-currPlanet.radius*planetScaleFactor), 0.0))            

            orbitLine = LineSet.create()
            
            l = orbitLine.addLine()
            l.setStart(Vector3(0, 1/(-currPlanet.radius*planetScaleFactor), 0))
            l.setEnd(Vector3(0, 0, 0))
            l.setThickness(1/(currPlanet.radius*planetScaleFactor))
            orbitLine.setEffect('colored -e white')
            model.addChild(orbitDot) 
            model.addChild(orbitLine)           
            
            #deal with the axial tilt of the sun & planets
            tiltCenter = SceneNode.create(currPlanet.name[0] +"TiltCenter")
            theRotCenter.SceneNode.addChild(tiltCenter)
            tiltCenter.addChild(model)           
            #tiltCenter.roll(1/180.0*pi)         
           # theRotCenter.SceneNode.yaw(currPlanet.periastron)
            theRotCenter.SceneNode.roll(-(currPlanet.inclination))
            #theRotCenter.SceneNode.yaw((currPlanet.inclination))
           # print("OKOK____"+str(currPlanet.periastron))

            addOrbit(currPlanet.semimajoraxis*orbitScaleFactor*userScaleFactor, 0, 0.01, currPlanet)
            theRotCenter.P = currPlanet.semiLatusRectum 
            theRotCenter.E = currPlanet.eccentricity   
            theRotCenter.solarObject = model           
            allRotCenters.append(theRotCenter)   
            
           #Add lables
            v = Text3D.create('fonts/arial.ttf', 1, currPlanet.name[0])
            v.setPosition(Vector3(0, 1, 0))         
            v.setFontResolution(120)
            v.setFontSize(1)
            v.getMaterial().setDoubleFace(1)
            #v.setFixedSize(True)
            v.setColor(Color('white'))
            model.addChild(v)           
              

#def binaryCreationDelve(currBinary)              
              
for theSystem in currentSystems:
  if(theSystem.name == "Sun"):
     centerSystem = theSystem
     
def createCenterSystem(verticalHeight, isItHome):
  global currentSystems
  global centerSystem
  global activePlanets
  global allRotCenters
  global chosenName
  cam.setPosition(0,15, 40)
#Step 2: Create center mass object
  # Create center mass object for other solar bodies to orbit.
  theRotCenter = aRotObject()
  theRotCenter.period = 1
  rotCenter = SceneNode.create(centerSystem.name+"RotCenter")
  rotCenter.setPosition(Vector3(0,0,0))

  activeRotCenters[centerSystem.name] = rotCenter
  solarSystem.addChild(rotCenter)
#Step 3: Create first-level suns, planets
  currStar = None
  for currStar in centerSystem.stars:
      setHabZone(currStar.spectralType) 
      theRotCenter = aRotObject()
      theRotCenter.period = 0
      rotCenter = SceneNode.create(currStar.name+"_RotCenter")
      rotCenter.setPosition(Vector3(0,0,0))
      theRotCenter.SceneNode = rotCenter      
      createStar(currStar, theRotCenter)
      solarSystem.addChild(rotCenter)
 
  if(currStar != None):   
   for currPlanet in currStar.planets:
     theRotCenter = aRotObject()
     theRotCenter.period = currPlanet.period
     rotCenter = SceneNode.create(currPlanet.name[0]+"__RotCenter")
     rotCenter.setPosition(Vector3(0,0,0))
     theRotCenter.SceneNode = rotCenter
     createPlanet(currPlanet, theRotCenter)
     solarSystem.addChild(rotCenter)

     
  for currPlanet in centerSystem.planets:
     theRotCenter = aRotObject()
     theRotCenter.period = currPlanet.period
     rotCenter = SceneNode.create(currPlanet.name[0]+"RotCenter")
     rotCenter.setPosition(Vector3(0,0,0))
     theRotCenter.SceneNode = rotCenter
     createPlanet(currPlanet, theRotCenter)
     solarSystem.addChild(rotCenter)
 

  #Ran out of time.
  #index = -1
  #for currBinary in centerSystem.binaries:
   #  for currStar in currBinary.stars:
    #  index = index * -1
 #     currStar.semimajoraxis = currStar.semimajoraxis*index
  #    setHabZone(currStar.spectralType) 
   #   theRotCenter = aRotObject()
#      theRotCenter.period = currBinary.period
#      biRotCenter = SceneNode.create(currStar.name+"_RotCenter")
 #     biRotCenter.setPosition(Vector3(0,0,0))
  #    theRotCenter.SceneNode = biRotCenter      
   #   createStar(currStar, theRotCenter)
      # solarSystem.addChild(rotCenter)
      # for currPlanet in currStar.planets:
            # theRotCenter = aRotObject()
            # theRotCenter.period = currPlanet.period
            # rotCenter = SceneNode.create(currPlanet.name[0]+"__RotCenter")
            # rotCenter.setPosition(Vector3(0,0,0))
            # theRotCenter.SceneNode = rotCenter
            # createPlanet(currPlanet, theRotCenter)
            # biRotCenter.addChild(rotCenter)
        

    
 
  # deal with the goldilocks zone
     
  inner = CylinderShape.create(1, habInner * orbitScaleFactor*userScaleFactor, habInner * orbitScaleFactor*userScaleFactor, 10, 128)
  inner.setEffect('colored -e #ff000055')
  inner.getMaterial().setTransparent(True)
  inner.pitch(-3.14159*0.5)
  inner.setScale(Vector3(1, 1, 1.0))

  outer = CylinderShape.create(1, habOuter * orbitScaleFactor*userScaleFactor, habOuter * orbitScaleFactor*userScaleFactor, 10, 128)
  outer.setEffect('colored -e #00FF0055')
  outer.getMaterial().setTransparent(True)
  outer.pitch(-3.14159*0.5)
  outer.setScale(Vector3(1, 1, 0.1))

  gZone = SceneNode.create("GZone")
  gZone.addChild(outer)
  gZone.addChild(inner)
   
  solarSystem.addChild(gZone)
  solarSystem.addChild(light1)

  # add everything to the solarSystem node for scaling and default positioning
  solarSystem.setScale(Vector3(overallScaleFactor, overallScaleFactor, overallScaleFactor))
  solarSystem.setPosition(Vector3(0, verticalHeight, 1))

  
  
########################
#Creating Universe View
########################

def createUniverse():
    global allSystems
    universeScale = 100
    for system in allSystems:
      good = 0
      if(system.name == "Sun"):
          x = 0
          y = 0
          z = 0
          good = 1
      if(system.distance != None and system.declination != None and system.rightAscension != None):
          A = (float(system.rightAscension[0])/24) + (float(system.rightAscension[1])/1440) +  (float(system.rightAscension[0])/86400)
          D = (float(system.declination[0])) + (float(system.declination[0])/60) + (float(system.declination[0])/3600)
          r = system.distance
          #convert to <x,y,z> coordinates
          x = r*cos(D)*cos(A)
          y = r*cos(D)*sin(A)
          z = r*sin(D)
          good = 1
      if(good == 1):
          model = SphereShape.create(10, 2)
          model.setPosition(Vector3(x*universeScale, y*universeScale, z*universeScale))
          #print(str(x)+"___"+str(y)+"____"+str(z))
          model.getMaterial().setProgram("textured")
          model.setEffect("textured -v emissive -d sol.png")          
          solarSystem.addChild(model)
          
      #Add lables
          v = Text3D.create('fonts/arial.ttf', 1, system.name)
          v.setPosition(Vector3(0, 15, 0))         
          v.setFontResolution(120)
          v.setFontSize(10)
          v.getMaterial().setDoubleFace(1)
          #v.setFixedSize(True)
          v.setColor(Color('white'))
          model.addChild(v)
      
      

##########################
#Creating Wall of Systems
##########################     
def createWallNeo():
   global currentSystems
   global ui
   global uiroot
   global currentSystems
   habZ = loadImage('green.jpg')
   jupG = loadImage('jupG.png')
   merT = loadImage('merT.png')
   planetImg={
   "0": loadImage('merT.png'),
   "1": loadImage('jupG.png'),   
   "2": loadImage('circ.png')}
   starImg={
   "astar.jpg": loadImage('astar.jpg'),
   "bstar.png": loadImage('bstar.png'),
   "kstar.png": loadImage('kstar.png'), 
   "mstar.png": loadImage('mstar.png'),
   "fstar.png": loadImage('fstar.png'),
   "ostar.png": loadImage('ostar.png'), 
   "gstar.png": loadImage('gstar.png'),
   "Tstar.png": loadImage('Tstar.png'), 
   "sol.png": loadImage('sol.png'),
   "green.jpg": loadImage('QM.png')}  
   #black = loadImage('black2.jpg')
   for column in range(0, 18):
     if(column < 4 or column > 14):
       for row in range(0,4):       
         #slider container
         sliderContainer = wf.createContainer(("sliderContainer"+str(column)+"_"+str(row)), uiroot, ContainerLayout.LayoutFree)
         sliderContainer.setPosition(Vector2((1366*column), (768*row)))
         sliderContainer.setAutosize(False)
         sliderContainer.setSize(Vector2(1366, 768))

         # create the slider background
        # sliderBackground = wf.createImage(('theImage'+str(column)+"_"+str(row)), sliderContainer)
         #sliderBackground.setData(black)
         #sliderBackground.setBlendMode(WidgetBlendMode.BlendNormal)
         sliderContainer.setAlpha(0.9)
         sliderContainer.setStyleValue('border', '2 #ffff00')
         sliderContainer.setClippingEnabled(True)       
         
         
         #Create a text item to print the value of the slider 
         index = (column*4) + row + centerChoicePage
         if(column > 14):
             index = index - 40
         if(len(currentSystems) > index):
           numSuns = currentSystems[index].numStars
           label = wf.createLabel(('label1%s' % currentSystems[index].name), sliderContainer, 'System Name: '+str(currentSystems[index].name))
           label.setPosition(Vector2(5, 5))
           label = wf.createLabel(('label1%s' % currentSystems[index].name), sliderContainer, 'LYrs from Sol: '+str(float(currentSystems[index].distance)*3.26163344)) ##Convert to Lyrs from Parsecs
           label.setPosition(Vector2(25, 40))
           label = wf.createLabel(('label1%s' % currentSystems[index].name), sliderContainer, '# of Planets: '+str(float(currentSystems[index].numPlanets)))
           label.setPosition(Vector2(45, 60))
           
           starDex = -1;
           #Create the star elements
           if(len(currentSystems[index].stars) > 0 and numSuns > 0):
             slider = wf.createImage('star%s' % index, sliderContainer)
             slider.setData(starImg[currentSystems[index].stars[0].texture])
             slider.setWidth(40)
             slider.setHeight((768/numSuns))         
             centerP =  (768/numSuns)/2         
             slider.setCenter(Vector2(20, centerP))
             #HabitableZone
             tempHabZone(currentSystems[index].stars[0].spectralType)
             slider = wf.createImage('star%s_HabitableZone' % index, sliderContainer)
             slider.setData(habZ)
             slider.setWidth(((thabOuter - thabInner)*orbitScaleFactor))
             slider.setHeight((768/numSuns))         
             centerP = ((768/numSuns)*(max(1,starDex*3)))/2           
             slider.setCenter(Vector2(((thabInner*orbitScaleFactor)*1.5), centerP))
             slider.setAlpha(.3) 
             if(len(currentSystems[index].stars[0].planets) > 0):
                   for currPlanet in currentSystems[index].stars[0].planets:
                     slider = wf.createImage('planet%s' % currPlanet.name[0], sliderContainer)
                     slider.setData(planetImg[str(currPlanet.isGas)])
                     slider.setScale((currPlanet.radius*planetScaleFactor*.0000025))
                     slider.setCenter(Vector2(max(50,(40 + (currPlanet.semimajoraxis*orbitScaleFactor*.25))), centerP))                     
             
           if(len(currentSystems[index].binaries) > 0):
             if(len(currentSystems[index].binaries[0].stars) > 0):
                for i,currStar in enumerate(currentSystems[index].binaries[0].stars):
                    starDex = starDex + 1
                    slider = wf.createImage('star%s-%i' % (index, starDex), sliderContainer)
                    slider.setData(starImg[currentSystems[index].binaries[0].stars[i].texture])
                    slider.setWidth(40)
                    slider.setHeight((768/numSuns))
                    centerP = ((768/numSuns)*(max(1,starDex*3)))/2                 
                    slider.setCenter(Vector2(20, centerP)) 
                    #HabitableZone
                    tempHabZone(currStar.spectralType)
                    slider = wf.createImage('star%s_HabitableZone' % currStar.name, sliderContainer)
                    slider.setData(habZ)
                    slider.setWidth(((thabOuter - thabInner)*orbitScaleFactor))
                    slider.setHeight((768/numSuns))         
                    centerP = ((768/numSuns)*(max(1,starDex*3)))/2           
                    slider.setCenter(Vector2(((thabInner*orbitScaleFactor)*1.5), centerP))
                    slider.setAlpha(.3) 
                    if(currStar.planets > 0):
                      for currPlanet in currStar.planets:
                        slider = wf.createImage('planet%s' % currPlanet.name[0], sliderContainer)
                        slider.setData(planetImg[str(currPlanet.isGas)])
                        slider.setScale((currPlanet.radius*planetScaleFactor*.0000025))
                        slider.setCenter(Vector2(max(50,(40 + (currPlanet.semimajoraxis*orbitScaleFactor*.25))), centerP))                     
             for currBinary in currentSystems[index].binaries[0].binaries:
              if(len(currBinary.stars) > 0):
                for i,currStar in enumerate(currBinary.stars):
                      starDex = starDex + 1
                      slider = wf.createImage('star%s-%i' % (index, starDex), sliderContainer)
                      slider.setData(starImg[currBinary.stars[i].texture])
                      slider.setWidth(40)
                      slider.setHeight((768/numSuns))
                      centerP = ((768/numSuns)*(max(1,starDex*3)))/2                       
                      slider.setCenter(Vector2(20, centerP)) 
                      #HabitableZone
                      tempHabZone(currStar.spectralType)
                      slider = wf.createImage('star%s_HabitableZone' % currStar.name, sliderContainer)
                      slider.setData(habZ)
                      slider.setWidth(((thabOuter - thabInner)*orbitScaleFactor))
                      slider.setHeight((768/numSuns))         
                      centerP = ((768/numSuns)*(max(1,starDex*3)))/2           
                      slider.setCenter(Vector2(((thabInner*orbitScaleFactor)*1.5), centerP))
                      slider.setAlpha(.3)
                      if(currStar.planets > 0):
                       for currPlanet in currStar.planets:
                        slider = wf.createImage('planet%s' % currPlanet.name[0], sliderContainer)
                        slider.setData(planetImg[str(currPlanet.isGas)])
                        slider.setScale((currPlanet.radius*planetScaleFactor*.0000025))
                        slider.setCenter(Vector2(max(50,(40 + (currPlanet.semimajoraxis*orbitScaleFactor*.25))), centerP))                     
             if(len(currentSystems[index].binaries) > 1):
               if(len(currentSystems[index].binaries[1].stars) > 0):
                for i,currStar in enumerate(currentSystems[index].binaries[1].stars):
                    starDex = starDex + 1
                    slider = wf.createImage('star%s-%i' % (index, starDex), sliderContainer)
                    slider.setData(starImg[currentSystems[index].stars[i].texture])
                    slider.setWidth(40)
                    slider.setHeight((768/numSuns))                   
                    centerP = ((768/numSuns)*(max(1,starDex*3)))/2                 
                    slider.setCenter(Vector2(20, centerP)) 
                    #HabitableZone
                    tempHabZone(currStar.spectralType)
                    slider = wf.createImage('star%s_HabitableZone' % currStar.name, sliderContainer)
                    slider.setData(habZ)
                    slider.setWidth(((thabOuter - thabInner)*orbitScaleFactor))
                    slider.setHeight((768/numSuns))         
                    centerP = ((768/numSuns)*(max(1,starDex*3)))/2           
                    slider.setCenter(Vector2(((thabInner*orbitScaleFactor)*1.5), centerP))
                    slider.setAlpha(.3)
                    if(currStar.planets > 0):
                      for currPlanet in currStar.planets:
                        slider = wf.createImage('planet%s' % currPlanet.name[0], sliderContainer)
                        slider.setData(planetImg[str(currPlanet.isGas)])
                        slider.setScale((currPlanet.radius*planetScaleFactor*.0000025))
                        slider.setCenter(Vector2(max(50,(40 + (currPlanet.semimajoraxis*orbitScaleFactor*.25))), centerP))
               if(len(currBinary.stars) > 0):        
                for currBinary in currentSystems[index].binaries[1].binaries:
                  if(len(currBinary.stars) > 0):
                    for i,currStar in enumerate(currBinary.stars):
                        starDex = starDex + 1
                        slider = wf.createImage('star%s-%i' % (index, starDex), sliderContainer)
                        slider.setData(starImg[currentSystems[index].stars[i].texture])
                        slider.setWidth(40)
                        slider.setHeight((768/numSuns))      
                        centerP = ((768/numSuns)*(max(1,starDex*3)))/2                 
                        slider.setCenter(Vector2(20, centerP))
                        #HabitableZone
                        tempHabZone(currStar.spectralType)
                        slider = wf.createImage('star%s_HabitableZone' % currStar.name, sliderContainer)
                        slider.setData(habZ)
                        slider.setWidth(((thabOuter - thabInner)*orbitScaleFactor))
                        slider.setHeight((768/numSuns))         
                        centerP = ((768/numSuns)*(max(1,starDex*3)))/2           
                        slider.setCenter(Vector2(((thabInner*orbitScaleFactor)*1.5), centerP))
                        slider.setAlpha(.3)
                        if(currStar.planets > 0):
                          for currPlanet in currStar.planets:
                            slider = wf.createImage('planet%s' % currPlanet.name[0], sliderContainer)
                            slider.setData(planetImg[str(currPlanet.isGas)])
                            slider.setScale((currPlanet.radius*planetScaleFactor*.0000025))
                            slider.setCenter(Vector2(max(50,(40 + (currPlanet.semimajoraxis*orbitScaleFactor*.25))), centerP))                  
                  
           
   
displayType = 0
##################
#Reset System
##################

def resetWall():
    global uiroot
    for column in range(0, 18):
      if(column < 4 or column > 14):
        for row in range(0,4): 
         if(uiroot.getChildByName("sliderContainer"+str(column)+"_"+str(row)) != None) :     
           uiroot.removeChild((uiroot.getChildByName("sliderContainer"+str(column)+"_"+str(row))))
    #uiroot = None
    #uiroot = ui.getUi()
    if(displayType != 3):
      createWallNeo()

def resetSystem():
    global displayType
    global displayedSystems 
    global solarSystem
    global thingsOnTheWall
    global everything
    global activePlanets
    global activeRotCenters

    activePlanets = {}
    activeRotCenters = {}

    #need to clean the scene graph here too
    
    #displayedSystems getting cleaned but not solarSystem

    # clear out the center solar system
    everything.removeChildByRef(solarSystem)
    solarSystem = None
    solarSystem = SceneNode.create('solarSystem')
    everything.addChild(solarSystem)

    resetWall()
    if(displayType == 0):
       createCenterSystem(1.5, 0)
    if(displayType == 1):
       createUniverse()

       
#######################################################################
def changeScale():
    global displayType
    resetSystem(0)
    if(displayType == 0):
        createCenterSystem(1.5, 0)
    if(displayType == 1):
        createUniverse()    

#######################################################################

#allPlanetarySystems[0]
#len(allPlanetarySystems)

#######################################################################

upA = 0
timeFactor = 10
def onUpdate(frame, t, dt):
    global allRotCenters
    global displayType
    global upA
    global timeFactor
    if(displayType == 0):
      for i,currRotCenter in enumerate(allRotCenters):
       if(allRotCenters[i].period != 0):
         a = (dt/40)*(365/allRotCenters[i].period)*timeFactor
        # upA = ((upA + 1)/(allRotCenters[i].period/365)) % 360
         currRotCenter.SceneNode.yaw(a)
        # dist = (allRotCenters[i].P / (1 - allRotCenters[i].E*cos(radians(upA))))*orbitScaleFactor*userScaleFactor
        # x = dist * cos(radians(upA))
        # y = dist * sin(radians(upA))
       #  currRotCenter.SceneNode.setPosition(x, 0, y)
        # activeRotCenters[name].yaw(dt/40*(1.0 / currentSystem[name][3])) #revolution (year)

#######################################################################

scene = getSceneManager()
cam = getDefaultCamera()

#set the background to black - kinda spacy
scene.setBackgroundColor(Color(0, 0, 0, 1))

#set the far clipping plane back a bit
setNearFarZ(0.1, 1000000)

pi = 3.14159

#scale factor for 3d system in the cave
userScaleFactor = 4
# 4 for kepler 11
# 1 for sol

#scale factor for the systems on the walls
user2ScaleFactor = 1
# 30 for kepler 11


################
##Scale Factors
################


orbitScaleFactor = 0.00001 * 149597871 #xml is in Au
planetScaleFactor = 0.1 * 69911 #Xml is in jupiter radii
sunScaleFactor = 0.001 * 695500 #XmL is in sun radii
overallScaleFactor = 0.00025

def resetScaleFactors():
   orbitScaleFactor = 0.00001 * 149597871 #xml is in Au
   planetScaleFactor = 0.1 * 69911 #Xml is in jupiter radii
   sunScaleFactor = 0.001 * 695500 #XmL is in sun radii
   timeFactor = 10
   overallScaleFactor = 0.00025


# load in the sphere model for all of the planets
mi = ModelInfo()
mi.name = "defaultSphere"
mi.path = "sphere2.obj"
scene.loadModel(mi)

# we dont want the wall systems moving
#getDefaultCamera().addChild(displayedSystems)
getDefaultCamera().addChild(thingsOnTheWall)

#need to work out some issues with globals to get this to work

#addWallOfSystems() 

# start up with Sol in the center of the CAVE

resetSystem()
#createUniverse()

setUpdateFunction(onUpdate)


mm = MenuManager.createAndInitialize()

##1366*768*18

#se = getSoundEnvironment()
#sample = se.loadSoundFromFile('music', 'Users/evldemo/sounds/menu_sounds/menu_load.wav')
#sisample = SoundInstance(sample)
#sisample.play()

# for the panel version
#solarSystem.roll(3.14159/2.0)
#solarSystem.pitch(3.14159/2.0)
#solarSystem.setScale(0.00001, 0.00001, 0.00001) #scale for panels

##############
#Systems Menu
##############
# This section created by modifying Alex's menu code from the first project.

centerChoiceMenu = mm.getMainMenu().addSubMenu("Change Center System")

#centerChoicePage = 0 #Declared Earlier
centerChoiceRange = 16
centerChoiceSlots = []

def updateCenterChoiceMenu(inAlter):
    global centerChoicePage
    global centerChoiceRange
    
    newCenterChoicePage = centerChoicePage+inAlter
    if newCenterChoicePage >= 0 and centerChoicePage < (len(currentSystems) + 12):
        centerChoicePage = newCenterChoicePage
        
        # Update "centerChoiceMenu" content
        for i in range(centerChoiceRange):
            index = centerChoicePage+i
            if index < len(currentSystems):
                centerChoiceSlots[i].setText(currentSystems[index].name)
                centerChoiceSlots[i].setCommand("centerSystem = currentSystems["+str(index)+"]; resetSystem() ")
                centerChoiceSlots[i].getButton().setCheckable(True)
                centerChoiceSlots[i].getButton().setRadio(True)
                centerChoiceSlots[i].getButton().setChecked(False)
            else:
                centerChoiceSlots[i].setText("-")
                centerChoiceSlots[i].setCommand("print 'Nothing to visit'")
                centerChoiceSlots[i].getButton().setCheckable(False)
                centerChoiceSlots[i].getButton().setRadio(False)
    print "Viewing page "+str(centerChoicePage/centerChoiceRange)

# "Previous" is always an option
centerChoiceMenu.addButton("Previous", "updateCenterChoiceMenu(-centerChoiceRange); resetWall()")

for i in range(centerChoiceRange):
    centerChoiceSlots.append(centerChoiceMenu.addButton(currentSystems[i].name, "centerSystem = currentSystems["+str(i)+"]; resetSystem() "))
    centerChoiceSlots[i].getButton().setCheckable(True)
    centerChoiceSlots[i].getButton().setRadio(True)

# "Next" is always an option
centerChoiceMenu.addButton("Next", "updateCenterChoiceMenu(centerChoiceRange); resetWall()")

####################
# Dynamic Filtering
####################
# Filter by Sun Temp
# Filter by Number of Suns
# Filter by presence of gas giants in terrestial zone
# Filter by presence of terrestial planets in habitable Zone
# Filter by presence of terrestial planets
# Filter by presence of gas giants
# Filter by presence of planets
# Filter by number of planets

class filterSet():
  def __init__(self):
    self.sunTemp = None
    self.numStars = None
    self.presGasGiantHabit = None
    self.presTerHabit = None
    self.presTer = None
    self.presGasGiants = None
    self.presPlanets = None
    self.numPlanets = None

filterChoices = filterSet()

def systemFilter(filterSet):
 global currentSystems
 global allSystems
 global centerChoicePage
 currentSystems[:] = []
 updateCenterChoiceMenu(-centerChoicePage)
 
 for system in allSystems:
  #if(filterSet.starTemp != None):
   #FILTER BASED ON TEMP
  if(filterSet.numStars != None):
    if(filterSet.numStars != system.numStars):
      continue
  if(filterSet.numPlanets != None):
    if(filterSet.numPlanets != system.numPlanets):
        continue
  if(filterSet.presPlanets != None):
    if(filterSet.presPlanets > (system.numPlanets) or ((filterSet.presPlanets != (system.terPlanets + system.gasPlanets) and filterSet.presPlanets == 0))):
      continue         
  if(filterSet.presTer != None):
    if(filterSet.presTer > system.terPlanets or (filterSet.presTer != system.terPlanets and filterSet.presTer == 0)):
      continue 
  if(filterSet.presGasGiants != None):
    if(filterSet.presGasGiants > system.gasPlanets or (filterSet.presGasGiants != system.gasPlanets and filterSet.presGasGiants == 0)):
      continue      
  if(filterSet.presGasGiantHabit != None):
    if(filterSet.presGasGiantHabit > system.gasPlanetsInHabitableZone or (filterSet.presGasGiantHabit != system.gasPlanetsInHabitableZone and filterset.presGasGiantHabit == 0)):
        continue
  if(filterSet.presTerHabit != None):
    if(filterSet.presTerHabit > system.terPlanetsInHabitableZone or (filterSet.presTerHabit != system.terPlanetsInHabitableZone and filterSet.presTerHabit == 0)):
        continue
  currentSystems.append(system)

#####################
#FilterMenu Creation
#####################

filterMenu = mm.getMainMenu().addSubMenu("FilterSystemsBy")
filterList = ['Systems_with_planets', 'Systems_With_Gas_Giants', 'Systems_with_Terrestial_Planets', 'Systems_with_Terrestial_Planets_in_the_Habitable_Zone', 'Systems_with_Gas_Giants_in_the_Habitable_Zone']
#theFilters = ['filerSet.numStars'
#filteringSet = filterChoices(filteringSet)

def changeFilter(filterChoice):
    global filterList
    global filterChoices
    if(filterChoice == filterList[0]):
        if(filterChoices.presPlanets == None):
           filterChoices.presPlanets = 1
        else:
           filterChoices.presPlanets = None
    if(filterChoice == filterList[1]):
        if(filterChoices.presGasGiants == None):
           filterChoices.presGasGiants = 1
        else:
           filterChoices.presGasGiants = None
    if(filterChoice == filterList[2]):
        if(filterChoices.presTer == None):
           filterChoices.presTer = 1
        else:
           filterChoices.presTer = None
    if(filterChoice == filterList[3]):
        if(filterChoices.presTerHabit == None):
           filterChoices.presTerHabit = 1
        else:
           filterChoices.presTerHabit = None  
    if(filterChoice == filterList[4]):
        if(filterChoices.presGasGiantHabit == None):
           filterChoices.presGasGiantHabit = 1
        else:
           filterChoices.presGasGiantHabit = None 
    systemFilter(filterChoices)

           
for i,filter in enumerate(filterList):
 filterX = filterMenu.addButton(("%s" % filter), ("changeFilter('%s')" % filter))
 filterX.getButton().setCheckable(True)
 
sunTempMenu = filterMenu.addSubMenu("Type of Sun")
numSunsMenu = filterMenu.addSubMenu("Number of Suns")
for x in range(0,5):
  filterX = numSunsMenu.addButton(("%i Star(s)" % x), ("filterSet.numStars = %i; systemFilter(filterChoices)" % x)) 

numPlanetsMenu = filterMenu.addSubMenu("Number of Planets")
for x in range(0,11):
  filterX = numPlanetsMenu.addButton(("%i Planet(s)" % x), ("filterSet.numPlanets = %i; systemFilter(filterChoices)" % x))   

scalesMenu = mm.getMainMenu().addSubMenu("Scales")
timeFMenu = scalesMenu.addSubMenu("Time")
sunFMenu = scalesMenu.addSubMenu("Solar Scale")
planetFMenu = scalesMenu.addSubMenu("Planar Scale")
orbitFMenu = scalesMenu.addSubMenu("Orbit Scale")

scalesX = timeFMenu.addButton("Increase Speed", ("timeFactor = timeFactor*1.5; resetSystem()"))
scalesX = timeFMenu.addButton("Decrease Speed", ("timeFactor = timeFactor*.75; resetSystem()"))

scalesX = sunFMenu.addButton("Increase Relative Solar Scale", ("sunScaleFactor = sunScaleFactor*1.5; resetSystem()"))
scalesX = sunFMenu.addButton("Decrease Relative Solar Scale", ("sunScaleFactor = sunScaleFactor*.75; resetSystem()"))

scalesX = planetFMenu.addButton("Increase Relative Planar Scale", ("planetScaleFactor = planetScaleFactor*1.5; resetSystem()"))
scalesX = planetFMenu.addButton("Decrease Relative Planer Scale", ("planetScaleFactor = planetScaleFactor*.75; resetSystem()"))

scalesX = orbitFMenu.addButton("Increase Relative Orbit Scale", ("orbitScaleFactor = orbitScaleFactor*1.5; resetSystem()"))
scalesX = orbitFMenu.addButton("Decrease Relative Orbit Scale", ("orbitScaleFactor = orbitScaleFactor*.75; resetSystem()"))

scalesX = scalesMenu.addButton("Reset All Views", ("resetScaleFactors(); resetSystem()"))
#######################
#Display Menu Creation
#######################
displayMenu = mm.getMainMenu().addSubMenu("Display")
displayX = displayMenu.addButton("Single System and Wall", ("displayType = 0; resetSystem()"))
displayX.getButton().setCheckable(True)
displayX.getButton().setRadio(True)
displayX = displayMenu.addButton("Universe and Wall", ("displayType = 1; resetSystem()"))
displayX.getButton().setCheckable(True)
displayX.getButton().setRadio(True)
#displayX = displayMenu.addButton("Double System (Not Implemented)", ("resetSystem(3)"))
#displayX.getButton().setCheckable(True)
#displayX.getButton().setRadio(True)


##############
# Sound Menu
##############

se = getSoundEnvironment()
music = se.loadSoundFromFile('music', '/home/evl/cs526/Kyle/OWM/system/SYSTEM/Background.wav')
si_one = SoundInstance(music)

mm = MenuManager.createAndInitialize()
soundMenu = mm.getMainMenu().addSubMenu("Music")

def switchToSong1():
  si_one.playStereo()
  si_one.setVolume(0.05)
  
def silence():
  si_one.stop()
  
for x in range(1,2):
 songX = soundMenu.addButton(("Song %i" % x), ("switchToSong%i();" % x))
 songX.getButton().setCheckable(True)
 songX.getButton().setRadio(True)
 
songX = soundMenu.addButton("No sound", "silence()")
songX.getButton().setCheckable(True)
songX.getButton().setRadio(True) 

#(127.5 * 2.54 / 100)


############################
#Graph maker
############################

#Create Graph
#Determine type of scale
#Plot Graph
#Figure out way to highlight graph images.
#Create a box of info.


uniGraphFactor = 'auto'

#Use a 4-tuple?

class aGraph():
  def __init__(self):
   self.name = None
   self.size = None
   self.glyph = None
   self.xType = None
   self.yType = None
   self.axis = [[],[],[]]
   self.allData = [[],[],[]]
   self.finalData = []
   self.scale = [None, None, None]
   self.scaleType = [None, None, None]
   self.labels = []
   self.points = {}
   self.midLine = []
   
class gChoiceSel():
  def __init__(self):
    self.ID = None
    self.xAtr = None
    self.yAtr = None
    self.pAtr = None
    self.xType = None
    self.yType = None
    self.pType = None
    self.xVType = None
    self.yVType = None
    self.pVType = None
    self.size = None
    self.glyph = 'merT.png'  
    self.sysGroup = 'current'

def fillGraphData(choice, theGraph, theObject, type, systemID, starID, num):
    theAtr = getattr(theObject, choice)
    if(type != 'planet'):
        name = 'allPlanets'
        #name = theObject.name
    else:
        name = theObject.name[0]
    theGraph.allData[num].append((theAtr, type, name, starID, systemID))
    #print theAtr, type, name, starID, systemID
   
def fillGraphBinaryDelve(choice, theGraph, theBinary, systemID, type, num):
    if(type == 'planet'):
        for currPlanet in theBinary.planets:
            fillGraphData(choice, theGraph, currPlanet, 'planet', systemID, 'allStars', num)
    
    for currStar in theBinary.stars:
        if(type == 'star'):
            fillGraphData(choice, theGraph, currStar, 'star', systemID, currStar.name, num)
        else:
            for currPlanet in currStar.planets:
                fillGraphData(choice, theGraph, currPlanet, 'planet', systemID, currStar.name, num) 
    
    for currBinary in theBinary.binaries: 
        fillGraphBinaryDelve(choice, theGraph, currBinary, systemID, type, num)

def fillGraphSystemDelve(choice, theGraph, theSystem, type, num):
    systemID = theSystem.name
    if(type == 'system'):
        fillGraphData(choice, theGraph, theSystem, 'system', systemID, 'allStarsAndAllPlanets', num)
    else:
        if(type == 'planet'):
            for currPlanet in theSystem.planets:
                fillGraphData(choice, theGraph, currPlanet, 'planet', systemID, 'allStars', num)
    
        for currStar in theSystem.stars:
            if(type == 'star'):
                fillGraphData(choice, theGraph, currStar, 'star', systemID, currStar.name, num)
            else:
                for currPlanet in currStar.planets:
                    fillGraphData(choice, theGraph, currPlanet, 'planet', systemID, currStar.name, num) 
    
        for currBinary in theSystem.binaries: 
            fillGraphBinaryDelve(choice, theGraph, currBinary, systemID, type, num)      


# combine x and y into a single point value.  Star and System data is kept, although it is possible for both
# x and y to be 'allStars' if one of the choices is a star trait.
def xyCombine(xVal, yVal, theGraph):
    if(xVal[3] != 'allStars'):
        theGraph.finalData.append((xVal[0], yVal[0], xVal[5], yVal[5], xVal[3], xVal[4], xVal[2]))
    else:
        theGraph.finalData.append((xVal[0], yVal[0], xVal[5], yVal[5], yVal[3], yVal[4], yVal[2]))   
            
def xyCombineLoop(comboVal, theGraph):
    if(comboVal == 1):
        for xVal in theGraph.allData[0]:
            for yVal in theGraph.allData[1]:
                if(xVal[2] == yVal[2]):
                    xyCombine(xVal, yVal, theGraph)  
    elif(comboVal == 2):
        for xVal in theGraph.allData[0]:
            for yVal in theGraph.allData[1]:
                if(xVal[3] == yVal[3] or (xVal[3] == 'allStars' and xVal[4] == yVal[4]) or (yVal[3] == 'allStars' and xVal[4] == yVal[4])):
                    xyCombine(xVal, yVal, theGraph) 
    elif(comboVal == 3):
         for xVal in theGraph.allData[0]:
            for yVal in theGraph.allData[1]:
                if(xVal[4] == yVal[4]):
                    xyCombine(xVal, yVal, theGraph)    
    elif(True):
        print 'error: impossible combination value given.'

def xyzCombine2(zValues, theGraph, zType):
    newFinal = []
    for xyVal in theGraph.finalData:
        found = False
        for zVal in zValues:
            if(zVal[2] != 'allPlanets' and zVal[2] == xyVal[6] and zType == 'planet'): #z is a planet
                newFinal.append((xyVal[0], xyVal[1], xyVal[2], xyVal[3], xyVal[4], xyVal[5], zVal[5]))
                found = True
            elif(zVal[3] == xyVal[4] and zVal[2] != 'allPlanets' and zType == 'star'): #Z is a star
                print zVal[2], xyVal[6]
                newFinal.append((xyVal[0], xyVal[1], xyVal[2], xyVal[3], xyVal[4], xyVal[5], zVal[5]))
                found = True
            elif(zVal[4] == xyVal[5] and zVal[3] == 'allStarsAndPlanets' and zType == 'system'): #Z is a system
                newFinal.append((xyVal[0], xyVal[1], xyVal[2], xyVal[3], xyVal[4], xyVal[5], zVal[5]))
                found = True
        if(found == False):
            newFinal.append((xyVal[0], xyVal[1], xyVal[2], xyVal[3], xyVal[4], xyVal[5], -1))            
    theGraph.finalData = []
    theGraph.finalData = newFinal
 
def descretize(theGraph, dataNum):
    tempList = sorted(theGraph.allData[dataNum], key=lambda val: val[0])
    newAllData = []
    numVals = 0
    oldVal = None
    theGraph.axis[dataNum].append(tempList[0][0])
    for data in tempList:
        print data[0], numVals
        if(data[0] == None and numVals == 0):
            oldVal == data[0]
            numVals = numVals + 1
        else:
            if(oldVal != data[0]):
                oldVal = data[0]
                numVals = numVals + 1
                theGraph.axis[dataNum].append(data[0])
        newAllData.append((data[0], data[1], data[2], data[3], data[4], numVals))
    theGraph.allData[dataNum] = []
    theGraph.allData[dataNum] = newAllData
    theGraph.scale[dataNum] = (0, numVals)
    theGraph.scaleType[dataNum] = "Discrete"
    #LOOK THE ABOVE UP.

#Median altered from: http://stackoverflow.com/questions/10482339/how-to-find-median because I forgot if mod works the same in python and then I found this when searching.
#I believe all lists I pass to this will already be sorted, but I left the sorting to make it more modular.
def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return ((length / 2) + (length / 2 - 1)) / 2
    return (length / 2)

def quarter(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 4:
        return ((length / 4) + (length / 4 - 1)) / 2
    return (length / 4)
    
def handleNumberData(theGraph, dataNum):
    tempList = sorted(theGraph.allData[dataNum], key=lambda val: val[0])
    theMedian = median(tempList)
    theQuarter = quarter(tempList)
    theLast = len(tempList) - 1
    qVal = tempList[theQuarter][0]
    medVal = tempList[theMedian][0]
    endVal = tempList[theLast][0]
    if( (((medVal*2.5) < endVal) or ((qVal*2.5) < medVal) or ((medVal * 1.5) > endVal)) and qVal > 1):
        theGraph.scaleType[dataNum] = "Log"
    else:
        theGraph.scaleType[dataNum] = "Reg"
    theGraph.axis[dataNum].append("0")
    theGraph.axis[dataNum].append(str(endVal/2))
    theGraph.axis[dataNum].append(str(endVal))   
    theGraph.scale[dataNum] = (0, endVal)
    
    newAllData = []
    for data in tempList:
        #print data[0], data[1], data[2], data[3], data[4]
        newAllData.append((data[0], data[1], data[2], data[3], data[4], data[0]))        
    theGraph.allData[dataNum] = []
    theGraph.allData[dataNum] = newAllData


def fillGraph(choice, xChoice, yChoice, xType, yType, xValType, yValType, zChoice, zType, zValType):
    graphSystems = []
    theGraph = aGraph()
    if(choice == 'wall'):
        for system in currentSystems:
            graphSystems.append(system)
    elif(choice == 'all'):
        for system in allSystems:
            graphSystems.append(system)
    elif(choice == 'current'):
        for system in currentSystems:
            graphSystems.append(system)           
   # elif(choice == 'active')
        #grab only from active systems
        
    for theSystem in graphSystems:
        fillGraphSystemDelve(xChoice, theGraph, theSystem, xType, 0)
        fillGraphSystemDelve(yChoice, theGraph, theSystem, yType, 1)
        fillGraphSystemDelve(zChoice, theGraph, theSystem, zType, 2)        
            
    if(xValType == "text"):
        descretize(theGraph, 0)
    else:
        handleNumberData(theGraph,0)
    if(yValType == "text"):
        descretize(theGraph, 1)
    else:
        handleNumberData(theGraph, 1)
    if(zValType == "text"):
        descretize(theGraph, 2)
    else:
        handleNumberData(theGraph, 2)       
        
    #print xType, yType
    comboVal = 1
    if(xType == 'system' or yType == 'system'):
        comboVal = 3
    elif(xType == 'star' or yType == 'star'):
        comboVal = 2
    xyCombineLoop(comboVal, theGraph)
    xyzCombine2(theGraph.allData[2], theGraph, zType)
    return theGraph

allGraphContainers = {}
gSubsChoice = []
def createGraph(row, column, index):
    global uiroot
    gChoices = gSubsChoice[index]
    theGraph = fillGraph(gChoices.sysGroup, gChoices.xAtr, gChoices.yAtr, gChoices.xType, gChoices.yType, gChoices.xVType, gChoices.yVType, gChoices.pAtr, gChoices.pType, gChoices.pVType)
    
    #load image and set size
    merT = loadImage(str(gChoices.glyph))
    barImg = loadImage('white.jpg')
    imgSize = gChoices.size
    
    #create container
    height = 768*2
    width = 1366*2
    sliderContainer = wf.createContainer(("sliderContainerG"+str(column)+"_"+str(row)), uiroot, ContainerLayout.LayoutFree)
    sliderContainer.setPosition(Vector2((1366*column), (768*row)))
    sliderContainer.setAutosize(False)
    sliderContainer.setSize(Vector2(width, height))
    sliderContainer.setAlpha(0.9)
    sliderContainer.setStyleValue('border', '2 #ffff00')
    sliderContainer.setClippingEnabled(True)


    
    offW = width * 0.15  
    
    oldW = width
    oldH = height
    width = width * .85
    height = height * .85

    #Creating Borders    
    slider = wf.createImage('barVal_%s_%s_1' % (str(column), str(row)), sliderContainer)
    slider.setData(barImg)
    slider.setWidth(15)
    slider.setHeight(oldH)
    slider.setPosition(Vector2(offW, -oldH))
    
    slider = wf.createImage('barVal_%s_%s_0' % (str(column), str(row)), sliderContainer)
    slider.setData(barImg)
    slider.setWidth(oldW)
    slider.setHeight(15)
    slider.setPosition(Vector2(0,height))   
    
    end = []
    end.append(theGraph.scale[0][1])
    end.append(theGraph.scale[1][1])
    end.append(theGraph.scale[2][1])
    #print "GOT HERE"

    for i,data in enumerate(theGraph.finalData):
        #print "AND HERE"
        #Set x position
        #print data[0], data[1], data[4], theGraph.scaleType[0]
        if(theGraph.scaleType[0] != "Log"):
            xPos = (float(data[2]) / end[0]) * width
        else:
            if(data[2] != 0):
                xPos = (log10(data[2]) / log10(end[0])) * width
            else:
                xPos = 0
        
        #set y position
        if(theGraph.scaleType[1] != "Log"): 
            #print data[3], end[1]
            yPos = (float(data[3]) / end[1]) * height
        else:
            if(data[3] != 0):
                yPos = (log10(data[3]) / log10(end[1])) * height
            else:
                yPos = 0
        
        #Create point
        slider = wf.createImage('graphVal_%s_%s' % (str(index), str(i)), sliderContainer)
        slider.setData(merT)
        divider = float(data[6])
        if(divider < 1):
            divider = end[2]
        slider.setWidth(imgSize * ( float(data[6])/end[2]) * 10)
        slider.setHeight(imgSize * ( float(data[6])/end[2]) * 10)
        slider.setCenter(Vector2((xPos + offW), (height - yPos)))
        allImages[index].append((slider, data)) #Because trying to do this via children searching wasn't working.
        
        #add to point to dict to use with hitTesting later.
        theGraph.points[slider.getName()] = data
        
    #add Graph to dict to use with hitTesting later.
    #allGraphContainers[sliderContainer.getName()] = theGraph    
    xAxisLen = len(theGraph.axis[0])
    yAxisLen = len(theGraph.axis[1])
    
    for i,text in enumerate(theGraph.axis[0]):
        axlab = wf.createLabel('L_%s_1' % index, sliderContainer, str(text))
        xPos = offW + ((float(i)/xAxisLen)*width)
        axlab.setPosition(Vector2(xPos, (height + 60)))

    for i,text in enumerate(theGraph.axis[1]):
        axlab = wf.createLabel('L_%s_1' % index, sliderContainer, str(text))
        yPos =  height - ((float(i)/yAxisLen)*height)
        axlab.setPosition(Vector2( (offW - 60), yPos))
    
    xylab = wf.createLabel('Axis_%s_0' % index, sliderContainer, "%s(%s)[X] by %s(%s)[Y] by %s(%s)[P]" % (str(gChoices.xAtr), str(theGraph.scaleType[0]), str(gChoices.yAtr), str(theGraph.scaleType[1]), str(gChoices.pAtr), str(theGraph.scaleType[2])  )   )
    xylab.setPosition(Vector2(600,5)) 
    highlightData()
    
    #More Labels
    #xylab = wf.createLabel('L_%s_1' % index, sliderContainer, 
    #xylab.setPosition(Vector2(600,5))   
    
    #for axis in theGraph.axis[1]
        
    #DO LABEL STUFF HERE

    
def clearGraphs():
    global uiroot
    allImages = []
    allImages = [[],[],[],[]]
    for column in range(0, 18):
      if(column > 3 or column < 14):
        for row in range(0,4): 
         if(uiroot.getChildByName("sliderContainerG"+str(column)+"_"+str(row)) != None) :     
            graph = uiroot.getChildByName("sliderContainerG"+str(column)+"_"+str(row))
            uiroot.removeChild((uiroot.getChildByName("sliderContainerG"+str(column)+"_"+str(row))))
            graph = None   
 
#----------------------
#Graphing Menu
#----------------------
gMenu = mm.getMainMenu().addSubMenu("Graphs")
gSubs = []

#Creating list of stored choices.
newChoice = gChoiceSel()
newChoice.ID = 1
gSubsChoice.append(newChoice)

newChoice = gChoiceSel()
newChoice.ID = 2
gSubsChoice.append(newChoice)

newChoice = gChoiceSel()
newChoice.ID = 3
gSubsChoice.append(newChoice)

newChoice = gChoiceSel()
newChoice.ID = 4
gSubsChoice.append(newChoice)#

#Creating graph sub menus
gSubs.append(gMenu.addSubMenu("Graph1"))
gSubs.append(gMenu.addSubMenu("Graph2"))
gSubs.append(gMenu.addSubMenu("Graph3"))
gSubs.append(gMenu.addSubMenu("Graph4"))

gChoiceList = [
               ("Ignore", "ignore", "system", "num"),   
               ("Planet Mass", "mass", "planet", "num"),
               ("Planet Radius", "radius", "planet", "num"),              
               ("Planet Orbital Period", "period", "planet", "num"),              
               ("Planet Eccentricity", "eccentricity", "planet", "num"),
               ("Planet Semimajoraxis", "semimajoraxis", "planet", "num"),
               ("Planet Detection Method", "mass", "planet", "text"),               
               ("Stellar Magnitude", "spectralType", "star", "text"),
               ("Star Temp", "temperature", "star", "num"),
               ("Star Mass", "mass", "star", "num"), 
               ("Star Radius", "radius", "star", "num"),                
               ("Distance to System", "distance", "system", "num"),
               ("Number of Suns In System", "numStars", "system", "num"), 
               ("Number of Planets In System", "numPlanets", "system", "num"),  
               ("Number of Terrestrial Planets in System", "terPlanets", "system", "num"),
               ("Number of Gas Planets in System", "gasPlanets", "system", "num")           
               ]
               
gSubVals = [(0,4), (2,4), (0,13), (2,13)]   

glyphList = [("Mercury", "merT.png"), 
             ("A Type Star", "astar.jpg"),
             ("M Type Star", "mstar.png"),
             ("F Type Star", "fstar.png"),
             ("T Type Star", "Tstar.png")]        

def doNothing():
    print 'did'

for i,sub in enumerate(gSubs):
    xSub = sub.addSubMenu("X Axis")
    ySub = sub.addSubMenu("Y Axis")
    pSub = sub.addSubMenu("P Axis")    
    confirmSub = sub.addSubMenu("Confirm?")
    xSub.addLabel("Choose X Axis")
    ySub.addLabel("Choose Y Axis")
    pSub.addLabel("Choose P Axis")
    for choice in gChoiceList:
        #X axis
        currButton = xSub.addButton(str(choice[0]), "gSubsChoice[%i].xAtr = '%s'; gSubsChoice[%i].xType = '%s'; gSubsChoice[%i].xVType = '%s'" % (i, str(choice[1]) , i, str(choice[2]), i, str(choice[3]))  )
        currButton.getButton().setCheckable(True)  
        currButton.getButton().setRadio(True)
        currButton.getButton().setChecked(False)
        
        #y axis
        currButton = ySub.addButton(str(choice[0]), "gSubsChoice[%i].yAtr = '%s'; gSubsChoice[%i].yType = '%s'; gSubsChoice[%i].yVType = '%s'" % (i, str(choice[1]) , i, str(choice[2]), i, str(choice[3]))  )
        currButton.getButton().setCheckable(True)
        currButton.getButton().setRadio(True)
        currButton.getButton().setChecked(False)
        
        #p 'axis'
        currButton = pSub.addButton(str(choice[0]), "gSubsChoice[%i].pAtr = '%s'; gSubsChoice[%i].pType = '%s'; gSubsChoice[%i].pVType = '%s'" % (i, str(choice[1]) , i, str(choice[2]), i, str(choice[3]))  )
        currButton.getButton().setCheckable(True)
        currButton.getButton().setRadio(True)
        currButton.getButton().setChecked(False)
        
    #Sub Menu for other options (Currently Glyphs and Size)
    gOptionsSub = sub.addSubMenu("Other Options")
    
    #Glyph Options
    glyphSub = gOptionsSub.addSubMenu("Choose Glyph")
    for glyph in glyphList:
        currButton = glyphSub.addButton(str(glyph[0]), "gSubsChoice[%i].glyph = '%s'" % (i, str(glyph[1])))
        currButton.getButton().setCheckable(True)
        currButton.getButton().setRadio(True)
        currButton.getButton().setChecked(False)
        
    #'Where to grab data from' options
    grabSub = gOptionsSub.addSubMenu("Choose System Group")
    currButton = grabSub.addButton("Current", "gSubsChoice[%i].sysGroup = 'current'" % (i))
    currButton.getButton().setCheckable(True)
    currButton.getButton().setRadio(True)
    currButton.getButton().setChecked(False)
    currButton = grabSub.addButton("Wall", "gSubsChoice[%i].sysGroup = 'wall'" % (i))
    currButton.getButton().setCheckable(True)
    currButton.getButton().setRadio(True)
    currButton.getButton().setChecked(False)    
    currButton = grabSub.addButton("All", "gSubsChoice[%i].sysGroup = 'all'" % (i))
    currButton.getButton().setCheckable(True)
    currButton.getButton().setRadio(True)
    currButton.getButton().setChecked(False)    
    
    #Size Options
    gSizeSub = gOptionsSub.addSubMenu("Change Point Size")
    #gSizeSub.addLabel("Current Size: 15")
    gSubsChoice[i].size = 15
    currButton = gSizeSub.addButton("Increase Size", "gSubsChoice[%i].size = gSubsChoice[%i].size * 1.25" % (i,i))
    currButton = gSizeSub.addButton("Decrease Size", "gSubsChoice[%i].size = gSubsChoice[%i].size * 0.8" % (i,i))     
    
    
    confirmSub.addButton("Create Graph", ("createGraph(%i,%i,%i)" % (gSubVals[i][0], gSubVals[i][1],i)))

gMenu.addButton("Clear Graphs", "clearGraphs()")    
    
    
#--------------------
#Wand Update and printing functions
#--------------------
 
infoBox = wf.createContainer(("InfoBox"), uiroot, ContainerLayout.LayoutFree)
infoBox.setPosition(Vector2((1366*9), (768*0)))
infoBox.setAutosize(False)
infoBox.setSize(Vector2((1366*2), (768/2)))
infoBox.setAlpha(0.7)
infoBox.setStyleValue('border', '2 #ffff00')
infoBox.setClippingEnabled(True)
infoLables = []     
infoLables.append(wf.createLabel('InfoLabel 1', infoBox, '-'))
infoLables[0].setPosition(Vector2(5, 5))
infoLables.append(wf.createLabel('InfoLabel 2', infoBox, '-'))
infoLables[1].setPosition(Vector2(5, 40))
infoLables.append(wf.createLabel('InfoLabel 3', infoBox, '-'))
infoLables[2].setPosition(Vector2(5, 75))
infoLables.append(wf.createLabel('InfoLabel 4', infoBox, '-'))
infoLables[3].setPosition(Vector2(5, 110))
infoLables.append(wf.createLabel('InfoLabel 5', infoBox, '-'))
infoLables[4].setPosition(Vector2(5, 145))
infoLables.append(wf.createLabel('InfoLabel 6', infoBox, '-'))
infoLables[5].setPosition(Vector2(5, 180))
infoLables.append(wf.createLabel('InfoLabel 7', infoBox, '-'))
infoLables[6].setPosition(Vector2(5, 215))
infoLables.append(wf.createLabel('InfoLabel 8', infoBox, '-'))
infoLables[7].setPosition(Vector2(5, 250))
infoLables.append(wf.createLabel('InfoLabel 9', infoBox, '-'))
infoLables[8].setPosition(Vector2(5, 285))
 
def printInfo(image):
        global infoBox
        global infoLables
        
        data = image[1]
        sys = None
        for system in allSystems:
            if(system.name == data[5] and system.name != 'unknown'):
                sys = system
            
        if(sys != None):
            infoLables[0].setText('System Name: %s' % data[5])
            infoLables[1].setText('Distance From Earth: %i' % sys.distance)            
            infoLables[2].setText('Star of Note: %s' % data[4])
            infoLables[3].setText('Selected Planet: %s' % data[3])
            infoLables[4].setText('Number of Stars in System: %i' % sys.numStars)
            infoLables[5].setText('Number of Planets in System: %i' % sys.numPlanets)        
        
     #theGraph.allData[num].append((theAtr, type, name, starID, systemID))
     #data = (xVal[0], yVal[0], xVal[5], yVal[5], xVal[3], xVal[4], zVal[5]))       
           
highlight = loadImage('green.jpg')   
def highlightData():
    for i,imageList in enumerate(allImages):
        daImage = loadImage(gSubsChoice[i].glyph)
        for image in imageList:
            if(image[1][5] == centerSystem.name):
                w = image[0].getWidth()
                h = image[0].getHeight()
                image[0].setData(highlight)
                image[0].setWidth(w)
                image[0].setHeight(h)
            else:
                w = image[0].getWidth()
                h = image[0].getHeight()
                image[0].setData(daImage)
                image[0].setWidth(w)
                image[0].setHeight(h)
        
def changeCenterByClick(image):
        global centerSystem
        global allSystems
        data = image[1] 
        chosen = data[5]       
        for system in allSystems:
            if(system.name == chosen and system.name != 'unknown'):
                centerSystem = system
                resetSystem()
        
        
coordCalc = CoordinateCalculator() 
 
global lastImage
cross = loadImage('cross.png')
uim2 = UiModule.createAndInitialize()
target = Image.create(uim2.getUi())
target.setData(cross)
target.setCenter(Vector2(100, 100))
target.setWidth(40)
target.setHeight(40)

onIt = False
def handleEvent():
        global userScaleFactor
        global displayType
        global uiroot
        global allImages
        global onIt
        global lastImage
        global target

        e = getEvent()
        if(e.isButtonDown(EventFlags.ButtonLeft)): 
            print("Left button pressed")
            #userScaleFactor = userScaleFactor * 0.75
            resetSystem()

        if(e.isButtonDown(EventFlags.ButtonRight)): 
            print("Right button pressed")
            #userScaleFactor = userScaleFactor * 1.25
            resetSystem()
                            
        if(e.isButtonDown(EventFlags.ButtonUp) and onIt == True):
            changeCenterByClick(lastImage)
            highlightData()
            
        if (e.getServiceType() == ServiceType.Wand ):#or e.getServiceType() == ServiceType.Pointer):
          r = getRayFromEvent(e)
          if (r[0]):
            o = e.getOrientation()
            p = e.getPosition()
            q = Quaternion(o.w, o.x, o.y, o.z)
            v = q*Vector3(0.0, 0.0, -1.0)
            
            coordCalc.set_position(p.x, p.y, p.z)
            coordCalc.set_orientation(v.x, v.y, v.z)
            coordCalc.calculate()
            
            ccx = coordCalc.get_x()
            ccy = coordCalc.get_y()
            if ccx >= 0.0 and ccy >= 0.0:
                currPosition = Vector2(ccx*24588, ccy*3072)
                for imageList in allImages:
                    for image in imageList:
                        if(image[0].hitTest(currPosition) == True):
                            printInfo(image)
                            onIt = True
                            lastImage = image
                target.setCenter(currPosition)           

setEventFunction(handleEvent)
