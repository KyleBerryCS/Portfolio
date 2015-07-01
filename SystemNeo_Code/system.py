######################################################
#
# starter program for Project 2 - CS 526 - Fall 2013
# Copyright 2013 Andrew Johnson, evl, uic
#
# goal is to show small multiples of exoplantary systems on
# the walls of the cave, and compare one or more systems in 3D 
# in the center of the CAVE
#
# goal is to be able to filter visible exoplanetary systems
# by various criteria and then look at a couple in detail
#
######################################################

from math import *
from euclid import *
from omega import *
from cyclops import *


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

# some hard coded data to start with

#name :(radius on km, orbit in km, texture, year, day, sun/planet, axial rotation, star type

Sol = {
    'Sol'    :(695500,           0, "sol.png",       1.00,   24.27, 1,   7.50, "G2V"),
    'Mercury':(  2440,    57910000, "mercury.jpg",   0.24,   58.65, 0,   0.00, "-"), 
    'Venus'  :(  6052,   108200000, "venus.jpg",     0.62, -243.00, 0, 177.36, "-"),
    'Earth'  :(  6371,   149600000, "8kEarth.jpg",   1.00,    1.00, 0,  23.45, "-"),
    'Mars'   :(  3400,   227900000, "mars.png",      1.88,    1.03, 0,  25.19, "-"),
    'Jupiter':( 69911,   778500000, "jupiter.jpg",  11.86,    0.41, 0,   3.13, "-"),
    'Saturn' :( 58232,  1433000000, "saturn.png",   29.46,    0.44, 0,  26.73, "-"),
    'Uranus' :( 25362,  2877000000, "uranus.jpg",   84.01,   -0.72, 0,  97.77, "-"),
    'Neptune':( 24622,  4503000000, "neptune.jpg", 164.80,    0.72, 0,  28.32, "-")
}

Kepler11 = {
    'Kepler 11':(765050,         0, "gstar.png",     1.00,    24.0,  1,   1.0, "G6V"),
    'b'      :(  12551,   13613600, "venus.jpg",     0.03,    1.0,  0,    1.5, "-"), 
    'c'      :(  20069,   15857600, "uranus.jpg",    0.04,    1.0,  0,    1.0, "-"),
    'd'      :(  21789,   23786400, "uranus.jpg",    0.06,    1.0,  0,    0.7, "-"),
    'e'      :(  28797,   29022400, "neptune.jpg",   0.09,    1.0,  0,    1.2, "-"),
    'f'      :(  16628,   37400000, "venus.jpg",     0.13,    1.0,  0,    0.6, "-"), 
    'g'      :(  23318,   69115200, "neptune.jpg",   0.32,    1.0,  0,    0.2, "-")
}

HD10180 = {
    'HD 10180':(834600,         0, "gstar.png",     1.00,    24.0,  1,    0.0, "G1V"),
    'b'      :(  7690,    2992000, "venus.jpg",     0.003,    1.0,  0,    0.0, "-"), 
    'c'      :(  17477,   8976000, "uranus.jpg",    0.016,    1.0,  0,    0.0, "-"),
    'd'      :(  17477,  19148800, "uranus.jpg",    0.04,     1.0,  0,    0.0, "-"),
    'e'      :(  71309,  40392000, "jupiter.jpg",   0.13,     1.0,  0,    0.0, "-"),
    'f'      :(  48239,  73304000, "saturn.png",    0.33,     1.0,  0,    0.0, "-"), 
    'g'      :(  30761, 210936000, "jupiter.jpg",   1.63,     1.0,  0,    0.0, "-"),
    'h'      :(  17477, 522104000, "neptune.jpg",   6.3,      1.0,  0,    0.0, "-")
}

Kepler32 = {
    'Kepler 32':(334750,       0,  "mstar.png",    1.00,    24.0,  1,    0.0, "M1V"),
    'f'      :(  5479,    2992000, "venus.jpg",    0.002,    1.0,  0,    0.0, "-"), 
    'e'      :(  7072,    8976000, "venus.jpg",    0.008,    1.0,  0,    0.0, "-"),
    'b'      :(  25484,  19148800, "uranus.jpg",   0.016,    1.0,  0,    0.0, "-"),
    'c'      :(  23573,  40392000, "uranus.jpg",   0.02,     1.0,  0,    0.0, "-"),
    'd'      :(  15864,  73304000, "neptune.jpg",  0.06,     1.0,  0,    0.0, "-")
}

Kepler62 = {
    'Kepler 62':(445120,       0,  "kstar.png",    1.00,    39.0,  1,   0.0, "K2V"),
    'b'      :(  8346,    8227823, "venus.jpg",    0.01,    1.0,  0,    0.0, "-"), 
    'c'      :(  3440,   13912602, "venus.jpg",    0.03,    1.0,  0,    0.0, "-"),
    'd'      :(  12423,  17951745, "uranus.jpg",   0.05,    1.0,  0,    0.0, "-"),
    'e'      :(  10257,  63878290, "uranus.jpg",   0.33,    1.0,  0,    0.0, "-"),
    'f'      :(   8983, 107411271, "neptune.jpg",  0.73,    1.0,  0,    0.0, "-")
}

Kepler20 = {
    'Kepler 20':(653770,       0,  "gstar.png",   1.00,    24.0,  1,   0.0, "G8"),
    'b'      :( 12169,   6371904, "neptune.jpg",  0.01,    1.0,  0,    0.0, "-"), 
    'e'      :(  5530,   7584612, "venus.jpg",    0.016,    1.0,  0,    0.0, "-"),
    'c'      :( 19559,  13912602, "uranus.jpg",   0.03,    1.0,  0,    0.0, "-"),
    'f'      :(  6588,  16515605, "venus.jpg",    0.05,    1.0,  0,    0.0, "-"),
    'd'      :( 17520,  44879361, "neptune.jpg",  0.21,    1.0,  0,    0.0, "-")
}

Gliese667C = {
    'Gliese 667 C':(292110,       0,  "mstar.png",   1.00,   105.0,  1,   0.0, "M1.5V"),
    'b'      :( 19113,   7479893, "neptune.jpg",  0.02,    1.0,  0,    0.0, "-"), 
    'c'      :( 15605,  18699734, "uranus.jpg",   0.08,    1.0,  0,    0.0, "-"),
    'f'      :( 11035,  22439681, "venus.jpg",    0.11,    1.0,  0,    0.0, "-"),
    'e'      :( 12742,  31415553, "venus.jpg",    0.17,    1.0,  0,    0.0, "-"),
    'd'      :( 17447,  41139415, "neptune.jpg",  0.25,    1.0,  0,    0.0, "-"),
    'g'      :( 16243,  80483654, "neptune.jpg",  0.69,    1.0,  0,    0.0, "-")
}

Gliese581 = {
    'Gliese 581':(201695,       0,  "mstar.png",   1.00,    24.0,   1,   0.0, "M3V"),
    'e'      :(  8919,  4188740, "venus.jpg",      0.009,    1.0,   0,    0.0, "-"), 
    'b'      :( 30554,  6133513, "jupiter.jpg",    0.014,    1.0,   0,    0.0, "-"),
    'c'      :( 20147, 10920645, "neptune.jpg",    0.18,     1.0,   0,    0.0, "-")
}

TauCeti = {
    'Tau Ceti':(556400,        0,  "gstar.png",   1.00,    34.0,   1,   0.0, "G8.5V"),
    'b'      :(  9009,  15707776, "venus.jpg",    0.04,    1.0,   0,    0.0, "-"), 
    'c'      :( 11217,  29171585, "neptune.jpg",  0.09,    1.0,   0,    0.0, "-"),
    'd'      :( 12088,  55949604, "uranus.jpg",   0.26,     1.0,   0,    0.0, "-"),
    'e'      :( 13211,  82578024, "neptune.jpg",  0.46,    1.0,   0,    0.0, "-"),
    'f'      :( 16454, 201957126, "uranus.jpg",   1.75,     1.0,   0,    0.0, "-")
}

#6371
# 149597871

allPlanetarySystems = [Sol, Kepler11, HD10180, Kepler32, Kepler62, Kepler20, Gliese667C, Gliese581, TauCeti]

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


# set up to rotate and revolve the suns and planets

activePlanets = {}
activeRotCenters = {}

# set up the initial scene hierarchy

everything = SceneNode.create('everything')
solarSystem = SceneNode.create('solarSystem')
thingsOnTheWall = SceneNode.create('thingsOnTheWall')
allSystems = SceneNode.create('allSystems')

everything.addChild(thingsOnTheWall)
everything.addChild(solarSystem)
thingsOnTheWall.addChild(allSystems)

# Create a directional light
light1 = Light.create()
light1.setLightType(LightType.Point)
light1.setColor(Color(1.0, 1.0, 1.0, 1.0))
#light1.setPosition(Vector3(0.0, 1.5, 1.0))
light1.setPosition(Vector3(0.0, 0.0, 0.0))
light1.setEnabled(True)

# would be nice to have the light stay with the position of the sun
# for now it stays in the center of the cave
#
# would also be nice to change the light colour to match the star
everything.addChild(light1)

# need to compute goldilocks zone off the type or luminosity of the particular star
# by default set it to Sol
AUtoKM = 149597871
habInner = 0.95 * AUtoKM
habOuter = 1.4 * AUtoKM
habCenter = 0.5 * (habInner + habOuter)

# set up the max distance shown on the wall systems (this doesnt really work yet)

wallLimit = 400000000

# http://exoplanet.eu/catalog/

#######################################################################

def addOrbit(orbit, col, thick):
    circle = LineSet.create()

    segments = 128
    radius = 1
    thickness = thick   #0.01 for orbit

    a = 0.0
    while a <= 360:
        x = cos(radians(a)) * radius
        y = sin(radians(a)) * radius
        a += 360.0 / segments 
        nx = cos(radians(a)) * radius
        ny = sin(radians(a)) * radius
    
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
            circle.setScale(Vector3(orbit, 1000.0, orbit))
        else:
            circle.setScale(Vector3(orbit, 10.0, orbit)) # 0.1


        solarSystem.addChild(circle)

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
        habInner = 8.5 * AUtoKM
        habOuter = 12.5 * AUtoKM
    elif starType.find('F')!=-1 :
        habInner = 1.5 * AUtoKM
        habOuter = 2.2 * AUtoKM
    elif starType.find('G')!=-1 :
        habInner = 0.95 * AUtoKM
        habOuter = 1.4 * AUtoKM
    elif starType.find('K')!=-1 :
        habInner = 0.38 * AUtoKM
        habOuter = 0.56 * AUtoKM
    elif starType.find('M')!=-1 :
        habInner = 0.08 * AUtoKM
        habOuter = 0.12 * AUtoKM
    else:
        habInner = 0
        habOuter = 0
        
    habCenter = (habInner + habOuter) * 0.5

#######################################################################

# may need to go to three panels horiontally per system
# especially for A type stars

def addWallOfSystems():
    global planets
    global planets2
    global planets3

    panelCounter = 0

    for h in xrange(1, 10): # 2, 20

        # leave a 'hole' in the center of the cave to see the far planets through
        if h == 5:
            continue
        for v in xrange(0, 8): # 0, 4

            # for now lets just alternate between the given systems
            thisSystem = allPlanetarySystems[(h+v) % len(allPlanetarySystems)]

            outlineBox = BoxShape.create(2.0, 0.25, 0.001)
            outlineBox.setPosition(Vector3(-0.5, 0, 0.01))
            outlineBox.setEffect('colored -e #111111')
#            outlineBox.getMaterial().setTransparent(True)
            screenCenter = SceneNode.create("box"+str(panelCounter))

            sSystem = SceneNode.create("sSystem"+str(panelCounter))
            for name,model in thisSystem.iteritems():

                # only show planets out to orbit of asteroid belt
                # ideally this scale should be on the menu
                if thisSystem[name][1] > wallLimit:
                    continue
                if thisSystem[name][5] == 0:
                    model = StaticObject.create("defaultSphere")
                    model.setScale(Vector3(thisSystem[name][0]*XplanetScaleFactor, thisSystem[name][0]*XplanetScaleFactor, thisSystem[name][0]*XplanetScaleFactor))
                else:
                    setHabZone(thisSystem[name][7])

                    t = Text3D.create('fonts/arial.ttf', 1, name + " - " + thisSystem[name][7])
#                    t = Text3D.create('./arial.ttf', 1, name + " - " + thisSystem[name][7])
#                    t.setPosition(Vector3(-0.2, 0.05, -0.5))
                    t.setPosition(Vector3(-0.2, 0.05, -0.05))
                    t.yaw(3.14159)
                    t.setFontResolution(120)
#                    t.setFontSize(120) # 120 works for CAVE2 but not for desktop version
                    t.setFontSize(0.05) # 120 works for CAVE2 but not for desktop version
                   # t.getMaterial().setDoubleFace(1)
                    t.getMaterial().setTransparent(False)
                    t.getMaterial().setDepthTestEnabled(False)
#                    t.setFixedSize(True)
                    t.setColor(Color('white'))
                    screenCenter.addChild(t)

                    # star is a box in this view
                    # need to make the colors more obvious
                    model = BoxShape.create(100, 25000, 2000)

                model.setPosition(Vector3(0.0, 0.0, 48000 - thisSystem[name][1] * XorbitScaleFactor * user2ScaleFactor))
                sSystem.addChild(model)
                model.setEffect("textured -v emissive -d "+thisSystem[name][2])

                panelCounter += 1

            # need to show habitable zone in this view as well
            # transparency not quite working here ...
                
            # wallLimit should also affect the visibility and edges of this if done well
            goldi = BoxShape.create(4, 25000, (1.0 * (habOuter - habInner)) * XorbitScaleFactor * user2ScaleFactor)

            goldi.setPosition(Vector3(0.0, 0.0, 48000 - habCenter * XorbitScaleFactor * user2ScaleFactor))
            sSystem.addChild(goldi)
            goldi.setEffect('colored -e #004400') 
#            goldi.getMaterial().setTransparent(True)


            sSystem.yaw(pi/2.0)
            sSystem.setScale(0.0000001, 0.00001, 0.00001) #scale for panels - flat to screen

            # should add a name and some other statistics in here as well     
            
            hLoc = h + 0.5
            degreeConvert = 36.0/360.0*2*pi #18 degrees per panel times 2 panels per viz = 36
            caveRadius = 3.25
            screenCenter.setPosition(Vector3(sin(hLoc*degreeConvert)*caveRadius, v * 0.29 + 0.41, cos(hLoc*degreeConvert)*caveRadius))
            screenCenter.yaw(hLoc*degreeConvert)
            screenCenter.addChild(sSystem)
            screenCenter.addChild(outlineBox)
            allSystems.addChild(screenCenter)

#######################################################################

def createCenterSystem(verticalHeight, isItHome):

# set up to show one of the systems in the center of the cave

    global currentSystem

    if isItHome == 1:
        theSystem = planets
    else: 
        theSystem = currentSystem

    for name,model in theSystem.iteritems():
        model = StaticObject.create("defaultSphere")
        if theSystem[name][5] == 0:
            model.setPosition(Vector3(0.0, 0.0, -theSystem[name][1]*orbitScaleFactor*userScaleFactor))
            model.setScale(Vector3(theSystem[name][0]*planetScaleFactor, theSystem[name][0]*planetScaleFactor, theSystem[name][0]*planetScaleFactor))
        else:
            setHabZone(theSystem[name][7])
            model.setPosition(Vector3(0.0, 1000.0, -theSystem[name][1]*orbitScaleFactor*userScaleFactor))
            model.setScale(Vector3(theSystem[name][0]*sunScaleFactor, theSystem[name][0]*sunScaleFactor, theSystem[name][0]*sunScaleFactor))
            sunDot = StaticObject.create("defaultSphere")
            sunDot.setPosition(Vector3(0.0, 0.0, -theSystem[name][1]*orbitScaleFactor*userScaleFactor))
            sunDot.setScale(Vector3(10, 10, 10))
            solarSystem.addChild(sunDot)

            sunLine = LineSet.create()

            l = sunLine.addLine()
            l.setStart(Vector3(0, 0, 0))
            l.setEnd(Vector3(0, 1000, 0))
            l.setThickness(1)
            sunLine.setEffect('colored -e white')
            solarSystem.addChild(sunLine)


        model.getMaterial().setProgram("textured")
        if theSystem[name][5] == 0:
            model.setEffect("textured -d "+theSystem[name][2])
        else:
            model.setEffect("textured -v emissive -d "+theSystem[name][2])
        activePlanets[name] = model

        #set up for planet name on top of planet
        planetCenter = SceneNode.create(name+str(isItHome)+"PlanetCenter")

        # deal with the axial tilt of the sun & planets
        tiltCenter = SceneNode.create(name+str(isItHome)+"TiltCenter")
        planetCenter.addChild(tiltCenter)
        tiltCenter.addChild(model)
        tiltCenter.roll(theSystem[name][6]/180.0*pi) 

        # deal with rotating the planets around the sun
        rotCenter = SceneNode.create(name+str(isItHome)+"RotCenter")
        rotCenter.setPosition(Vector3(0,0,0))
        rotCenter.addChild(planetCenter)

        activeRotCenters[name] = rotCenter
        solarSystem.addChild(rotCenter)

        addOrbit(theSystem[name][1]*orbitScaleFactor*userScaleFactor, 0, 0.01)

        # deal with labelling everything
        v = Text3D.create('fonts/arial.ttf', 1, name)
        if theSystem[name][5] == 0:
            v.setPosition(Vector3(0, theSystem[name][0]*planetScaleFactor, - theSystem[name][1]*orbitScaleFactor*userScaleFactor))
        else:
            v.setPosition(Vector3(0, 500, - theSystem[name][1]*orbitScaleFactor*userScaleFactor))
        v.setFontResolution(120)

        v.setFontSize(160)
        v.getMaterial().setDoubleFace(1)
        v.setFixedSize(True)
        v.setColor(Color('white'))
        planetCenter.addChild(v)

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

#######################################################################

def resetSystem():
    global allSystems 
    global solarSystem
    global thingsOnTheWall
    global everything
    global activePlanets
    global activeRotCenters

    activePlanets = {}
    activeRotCenters = {}

    #need to clean the scene graph here too
    
    #allSystems getting cleaned but not solarSystem

    # clear out the center solar system
    everything.removeChildByRef(solarSystem)
    solarSystem = None
    solarSystem = SceneNode.create('solarSystem')
    everything.addChild(solarSystem)

    # clear out all the systems on the wall
    #thingsOnTheWall.removeChildByRef(allSystems)
    #allSystems = None
    #allSystems = SceneNode.create('allSystems')
    #thingsOnTheWall.addChild(allSystems)

#######################################################################

def changeScale():
    resetSystem()
    createCenterSystem(1.5, 0)

#######################################################################

#allPlanetarySystems[0]
#len(allPlanetarySystems)

#######################################################################

def onUpdate(frame, t, dt):
    for name,model in currentSystem.iteritems():
        activeRotCenters[name].yaw(dt/40*(1.0 / currentSystem[name][3])) #revolution (year)
        activePlanets[name].yaw(dt/40*365*(1.0 / currentSystem[name][4])) #rotation (day) 

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

orbitScaleFactor = 0.00001
planetScaleFactor = 0.01
sunScaleFactor = 0.001
overallScaleFactor = 0.00025

#XorbitScaleFactor = 0.000043
#XorbitScaleFactor = 0.00023
# currently scaling for inner planets of our solar system

#XorbitScaleFactor = 0.0008
# this is not really right ...
XorbitScaleFactor = 320000.0 / wallLimit
XplanetScaleFactor = 0.2

# load in the sphere model for all of the planets
mi = ModelInfo()
mi.name = "defaultSphere"
mi.path = "sphere.obj"
scene.loadModel(mi)

# we dont want the wall systems moving
#getDefaultCamera().addChild(allSystems)
getDefaultCamera().addChild(thingsOnTheWall)

#need to work out some issues with globals to get this to work

addWallOfSystems() 

# start up with Sol in the center of the CAVE

resetSystem()
currentSystem = allPlanetarySystems[0]
createCenterSystem(1.5, 0)

setUpdateFunction(onUpdate)


mm = MenuManager.createAndInitialize()
sysmnu = mm.getMainMenu().addSubMenu("Choose Solar System")

# test to convert this into a loop
#for b in xrange(1, len(allPlanetarySystems) ):
#    print(str(b)+" "+allPlanetarySystems[b].name)

btn1 = sysmnu.addButton("Sol", "resetSystem(); currentSystem = allPlanetarySystems[0];createCenterSystem(1.5, 0)")
btn2 = sysmnu.addButton("Kepler 11", "resetSystem(); currentSystem = allPlanetarySystems[1];createCenterSystem(1.5, 0)")
btn3 = sysmnu.addButton("HD 10180", "resetSystem(); currentSystem = allPlanetarySystems[2];createCenterSystem(1.5, 0)")
btn4 = sysmnu.addButton("Kepler 32", "resetSystem(); currentSystem = allPlanetarySystems[3];createCenterSystem(1.5, 0)")
btn5 = sysmnu.addButton("Kepler 62", "resetSystem(); currentSystem = allPlanetarySystems[4];createCenterSystem(1.5, 0)")
btn6 = sysmnu.addButton("Kepler 20", "resetSystem(); currentSystem = allPlanetarySystems[5];createCenterSystem(1.5, 0)")
btn7 = sysmnu.addButton("Gliese 667 C", "resetSystem(); currentSystem = allPlanetarySystems[6];createCenterSystem(1.5, 0)")
btn8 = sysmnu.addButton("Gliese 581", "resetSystem(); currentSystem = allPlanetarySystems[7];createCenterSystem(1.5, 0)")
btn9 = sysmnu.addButton("Tau Ceti", "resetSystem(); currentSystem = allPlanetarySystems[8];createCenterSystem(1.5, 0)")


def handleEvent():
    global userScaleFactor

    e = getEvent()
    if(e.isButtonDown(EventFlags.ButtonLeft)): 
        print("Left button pressed")
        userScaleFactor = userScaleFactor * 0.75
        resetSystem()
        createCenterSystem(1.5, 0)

    if(e.isButtonDown(EventFlags.ButtonRight)): 
        print("Right button pressed")
        userScaleFactor = userScaleFactor * 1.25
        resetSystem()
        createCenterSystem(1.5, 0)

setEventFunction(handleEvent)


#se = getSoundEnvironment()
#sample = se.loadSoundFromFile('music', 'Users/evldemo/sounds/menu_sounds/menu_load.wav')
#sisample = SoundInstance(sample)
#sisample.play()

# for the panel version
#solarSystem.roll(3.14159/2.0)
#solarSystem.pitch(3.14159/2.0)
#solarSystem.setScale(0.00001, 0.00001, 0.00001) #scale for panels
