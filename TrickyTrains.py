
##################################
#Isabelle Organ & Fayza Oyarekhua#
#Tricky Trains                   #
#ICSO2                           #
#January 20th 2020               #
##################################

#importing essentials
import pygame
import numpy
import os
import time
import random
from random import choice
from random import randint
import datetime

pygame.init()

currenttime = datetime.datetime.now()
startTime = int(currenttime.second)

trainCooldown = 0
coolDownTime = 175

trainColour = randint(1,6)

screenWidth = 640
screenHeight = 480

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

gameSurface = pygame.display.get_surface()
keys = pygame.key.get_pressed()

#Assigning colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

#Import Images
redTrain = pygame.image.load(os.path.join('data', 'RedTrain.png')).convert()
redTrain.set_colorkey(white)
redTrain1 = pygame.image.load(os.path.join('data', 'RedTrain.png')).convert()
redTrain1.set_colorkey(white)
redTrain2 = pygame.image.load(os.path.join('data', 'RedTrain.png')).convert()
redTrain2.set_colorkey(white)
redTrain3 = pygame.image.load(os.path.join('data', 'RedTrain.png')).convert()
redTrain3.set_colorkey(white)
redTrain4 = pygame.image.load(os.path.join('data', 'RedTrain.png')).convert()
redTrain4.set_colorkey(white)
orangeTrain = pygame.image.load(os.path.join('data', 'OrangeTrain.png')).convert()
orangeTrain.set_colorkey(white)
orangeTrain1 = pygame.image.load(os.path.join('data', 'OrangeTrain.png')).convert()
orangeTrain1.set_colorkey(white)
orangeTrain2 = pygame.image.load(os.path.join('data', 'OrangeTrain.png')).convert()
orangeTrain2.set_colorkey(white)
orangeTrain3 = pygame.image.load(os.path.join('data', 'OrangeTrain.png')).convert()
orangeTrain3.set_colorkey(white)
orangeTrain4 = pygame.image.load(os.path.join('data', 'OrangeTrain.png')).convert()
orangeTrain4.set_colorkey(white)
yellowTrain = pygame.image.load(os.path.join('data', 'YellowTrain.png')).convert()
yellowTrain.set_colorkey(white)
yellowTrain1 = pygame.image.load(os.path.join('data', 'YellowTrain.png')).convert()
yellowTrain1.set_colorkey(white)
yellowTrain2 = pygame.image.load(os.path.join('data', 'YellowTrain.png')).convert()
yellowTrain2.set_colorkey(white)
yellowTrain3 = pygame.image.load(os.path.join('data', 'YellowTrain.png')).convert()
yellowTrain3.set_colorkey(white)
yellowTrain4 = pygame.image.load(os.path.join('data', 'YellowTrain.png')).convert()
yellowTrain4.set_colorkey(white)
greenTrain = pygame.image.load(os.path.join('data', 'GreenTrain.png')).convert()
greenTrain.set_colorkey(white)
greenTrain1 = pygame.image.load(os.path.join('data', 'GreenTrain.png')).convert()
greenTrain1.set_colorkey(white)
greenTrain2 = pygame.image.load(os.path.join('data', 'GreenTrain.png')).convert()
greenTrain2.set_colorkey(white)
greenTrain3 = pygame.image.load(os.path.join('data', 'GreenTrain.png')).convert()
greenTrain3.set_colorkey(white)
greenTrain4 = pygame.image.load(os.path.join('data', 'GreenTrain.png')).convert()
greenTrain4.set_colorkey(white)
blueTrain = pygame.image.load(os.path.join('data', 'BlueTrain.png')).convert()
blueTrain.set_colorkey(white)
blueTrain1 = pygame.image.load(os.path.join('data', 'BlueTrain.png')).convert()
blueTrain1.set_colorkey(white)
blueTrain2 = pygame.image.load(os.path.join('data', 'BlueTrain.png')).convert()
blueTrain2.set_colorkey(white)
blueTrain3 = pygame.image.load(os.path.join('data', 'BlueTrain.png')).convert()
blueTrain3.set_colorkey(white)
blueTrain4 = pygame.image.load(os.path.join('data', 'BlueTrain.png')).convert()
blueTrain4.set_colorkey(white)
purpleTrain = pygame.image.load(os.path.join('data', 'PurpleTrain.png')).convert()
purpleTrain.set_colorkey(white)
purpleTrain1 = pygame.image.load(os.path.join('data', 'PurpleTrain.png')).convert()
purpleTrain1.set_colorkey(white)
purpleTrain2 = pygame.image.load(os.path.join('data', 'PurpleTrain.png')).convert()
purpleTrain2.set_colorkey(white)
purpleTrain3 = pygame.image.load(os.path.join('data', 'PurpleTrain.png')).convert()
purpleTrain3.set_colorkey(white)
purpleTrain4 = pygame.image.load(os.path.join('data', 'PurpleTrain.png')).convert()
purpleTrain4.set_colorkey(white)
redStation = pygame.image.load(os.path.join('data', 'RedStation.png')).convert()
redStation.set_colorkey(white)
orangeStation = pygame.image.load(os.path.join('data', 'OrangeStation.png')).convert()
orangeStation.set_colorkey(white)
yellowStation = pygame.image.load(os.path.join('data', 'YellowStation.png')).convert()
yellowStation.set_colorkey(white)
greenStation = pygame.image.load(os.path.join('data', 'GreenStation.png')).convert()
greenStation.set_colorkey(white)
blueStation = pygame.image.load(os.path.join('data', 'BlueStation.png')).convert()
blueStation.set_colorkey(white)
purpleStation = pygame.image.load(os.path.join('data', 'PurpleStations.png')).convert()
purpleStation.set_colorkey(white)
track1 = pygame.image.load(os.path.join('data', 'Track1.png')).convert()
track1.set_colorkey(white)
track1Variation = pygame.image.load(os.path.join('data', 'Track1Variation.png')).convert()
track1Variation.set_colorkey(white)
track2 = pygame.image.load(os.path.join('data', 'Track2.png')).convert()
track2.set_colorkey(white)
track2Variation = pygame.image.load(os.path.join('data', 'Track2Variation.png')).convert()
track2Variation.set_colorkey(white)
track3 = pygame.image.load(os.path.join('data', 'Track3.png')).convert()
track3.set_colorkey(white)
track3Variation = pygame.image.load(os.path.join('data', 'Track3Variation.png')).convert()
track3Variation.set_colorkey(white)
track4 = pygame.image.load(os.path.join('data', 'Track4.png')).convert()
track4.set_colorkey(white)
track4Variation = pygame.image.load(os.path.join('data', 'Track4Variation.png')).convert()
track4Variation.set_colorkey(white)
track5 = pygame.image.load(os.path.join('data', 'Track5.png')).convert()
track5.set_colorkey(white)
track5Variation = pygame.image.load(os.path.join('data', 'Track5Variation.png')).convert()
track5Variation.set_colorkey(white)
background = pygame.image.load(os.path.join('data', 'Background.png')).convert()
openBackground = pygame.image.load(os.path.join('data', 'OpenBackground.png')).convert()


#Assign Train coordinates
redTrainX = 578
redTrainY = 500
redTrain1X = 578
redTrain1Y = 500
redTrain2X = 578
redTrain2Y = 500
redTrain3X = 578
redTrain3Y = 500
redTrain4X = 578
redTrain4Y = 500
orangeTrainX = 578
orangeTrainY = 500
orangeTrain1X = 578
orangeTrain1Y = 500
orangeTrain2X = 578
orangeTrain2Y = 500
orangeTrain3X = 578
orangeTrain3Y = 500
orangeTrain4X = 578
orangeTrain4Y = 500
yellowTrainX = 578
yellowTrainY = 500
yellowTrain1X = 578
yellowTrain1Y = 500
yellowTrain2X = 578
yellowTrain2Y = 500
yellowTrain3X = 578
yellowTrain3Y = 500
yellowTrain4X = 578
yellowTrain4Y = 500
greenTrainX = 578
greenTrainY = 500
greenTrain1X = 578
greenTrain1Y = 500
greenTrain2X = 578
greenTrain2Y = 500
greenTrain3X = 578
greenTrain3Y = 500
greenTrain4X = 578
greenTrain4Y = 500
blueTrainX = 578
blueTrainY = 500
blueTrain1X = 578
blueTrain1Y = 500
blueTrain2X = 578
blueTrain2Y = 500
blueTrain3X = 578
blueTrain3Y = 500
blueTrain4X = 578
blueTrain4Y = 500
purpleTrainX = 578
purpleTrainY = 500
purpleTrain1X = 578
purpleTrain1Y = 500
purpleTrain2X = 578
purpleTrain2Y = 500
purpleTrain3X = 578
purpleTrain3Y = 500
purpleTrain4X = 578
purpleTrain4Y = 500

#Assigning visibility
redTrainNum0 = 0
redTrainNum1 = 0
redTrainNum2 = 0
redTrainNum3 = 0
redTrainNum4 = 0
orangeTrainNum0 = 0
orangeTrainNum1 = 0
orangeTrainNum2 = 0
orangeTrainNum3 = 0
orangeTrainNum4 = 0
yellowTrainNum0 = 0
yellowTrainNum1 = 0
yellowTrainNum2 = 0
yellowTrainNum3 = 0
yellowTrainNum4 = 0
greenTrainNum0 = 0
greenTrainNum1 = 0
greenTrainNum2 = 0
greenTrainNum3 = 0
greenTrainNum4 = 0
blueTrainNum0 = 0
blueTrainNum1 = 0
blueTrainNum2 = 0
blueTrainNum3 = 0
blueTrainNum4 = 0
purpleTrainNum0 = 0
purpleTrainNum1 = 0
purpleTrainNum2 = 0
purpleTrainNum3 = 0
purpleTrainNum4 = 0
track1Visible = 1
track1VariationVisible = 0
track2Visible = 1
track2VariationVisible = 0
track3Visible = 1
track3VariationVisible = 0
track4Visible = 1
track4VariationVisible = 0
track5Visible = 1
track5VariationVisible = 0
trackNum1Button = 1
trackNum2Button = 1
trackNum3Button = 1
trackNum4Button = 1
trackNum5Button = 1

#Game mechanics
lives = 3
trainsIn = 0
trainsOut = 0
trainsBack = 0


track1Button = pygame.Rect(475, 255, 60, 60)
track2Button = pygame.Rect(458, 364, 60, 60)
track3Button = pygame.Rect(240, 420, 60, 60)
track4Button = pygame.Rect(478, 165, 60, 60)
track5Button = pygame.Rect(150, 15, 60, 60)

#train rotation variables
redTrainRotation = 0
redTrainTurns = 0
redTrain1Rotation = 0
redTrain1Turns = 0
redTrain2Rotation = 0
redTrain2Turns = 0
redTrain3Rotation = 0
redTrain3Turns = 0
redTrain4Rotation = 0
redTrain4Turns = 0
orangeTrainRotation = 0
orangeTrainTurns = 0
orangeTrain1Rotation = 0
orangeTrain1Turns = 0
orangeTrain2Rotation = 0
orangeTrain2Turns = 0
orangeTrain3Rotation = 0
orangeTrain3Turns = 0
orangeTrain4Rotation = 0
orangeTrain4Turns = 0
yellowTrainRotation = 0
yellowTrainTurns = 0
yellowTrain1Rotation = 0
yellowTrain1Turns = 0
yellowTrain2Rotation = 0
yellowTrain2Turns = 0
yellowTrain3Rotation = 0
yellowTrain3Turns = 0
yellowTrain4Rotation = 0
yellowTrain4Turns = 0
greenTrainRotation = 0
greenTrainTurns = 0
greenTrain1Rotation = 0
greenTrain1Turns = 0
greenTrain2Rotation = 0
greenTrain2Turns = 0
greenTrain3Rotation = 0
greenTrain3Turns = 0
greenTrain4Rotation = 0
greenTrain4Turns = 0
blueTrainRotation = 0
blueTrainTurns = 0
blueTrain1Rotation = 0
blueTrain1Turns = 0
blueTrain2Rotation = 0
blueTrain2Turns = 0
blueTrain3Rotation = 0
blueTrain3Turns = 0
blueTrain4Rotation = 0
blueTrain4Turns = 0
purpleTrainRotation = 0
purpleTrainTurns = 0
purpleTrain1Rotation = 0
purpleTrain1Turns = 0
purpleTrain2Rotation = 0
purpleTrain2Turns = 0
purpleTrain3Rotation = 0
purpleTrain3Turns = 0
purpleTrain4Rotation = 0
purpleTrain4Turns = 0


#Game settings
gameOn = False
menuOn = True
popUp = False
gameOver = False

instructionCounter = 0

while True:
    font = pygame.font.SysFont("timesnewromanms", 60)
    font1 = pygame.font.SysFont("timesnewromanms", 20)
    while menuOn:
        screen.blit(openBackground,[0,0])
        menuButton = pygame.Rect(160, 350, 300, 50)
        startButton = pygame.Rect(270, 230, 100, 50)
        startButtonText = font.render("Start", True, white)
        quitButton = pygame.Rect(270, 350, 100, 50)
        quitButtonText = font.render("Quit", True, white)
        instructionsButton = pygame.Rect(200, 290, 250, 50)
        instructionsButtonText = font.render("Instructions", True, white)
        menuText = font.render("Return to Menu", True, black)
        instructions = font1.render('Get each train to the station that matches their colour by clicking on', True, black)
        instructions2 = font1.render('the track on a green circle to change their course! You have 3 lives!', True, black)

        pygame.draw.rect(screen, black,startButton)
        screen.blit(startButtonText, (270, 240))

        pygame.draw.rect(screen, black, quitButton)
        screen.blit(quitButtonText, (270, 360))

        pygame.draw.rect(screen, black, instructionsButton)
        screen.blit(instructionsButtonText, (200, 300))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if startButton.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    menuOn = False
                    gameOn = True
                    screen.blit(background,[0,0])

                if quitButton.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    pygame.quit()
                    exit

                if instructionsButton.collidepoint(mouse_pos):
                    instructionCounter = 1
                    print('button was pressed at {0}'.format(mouse_pos))
                    popUp = True
                    menuOn = False

        pygame.display.flip()
        clock.tick(60)

    while popUp:
        screen.fill(black)
        pygame.draw.rect(screen, white, (75, 75, 490, 330))
        pygame.draw.rect(screen, white, (menuButton))
        screen.blit(menuText, (155, 350))
        screen.blit(instructions, (100, 200))
        screen.blit(instructions2, (100, 225))


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

        if menuButton.collidepoint(mouse_pos):
            print('button was pressed at {0}'.format(mouse_pos))
            instructionCounter = 0
            menuOn = True
            popUp = False

        pygame.display.flip()
        clock.tick(60)


    while gameOn:
        #text
        score = str(trainsIn) + '/' + str(trainsOut)
        scoreText = font.render(score, True, white)
        livesText = str(lives) + '/3'
        livesText1 = font.render(livesText, True, white)
        #blitting images
        pygame.draw.rect(screen, black,track1Button)
        pygame.draw.rect(screen, black,track2Button)
        pygame.draw.rect(screen, black,track3Button)
        pygame.draw.rect(screen, black,track4Button)
        pygame.draw.rect(screen, black,track5Button)
        screen.blit(background,[0,0])
        screen.blit(redStation,[20,10])
        screen.blit(orangeStation,[437,328])
        screen.blit(yellowStation,[120,330])
        screen.blit(greenStation,[394,75])
        screen.blit(blueStation,[60,90])
        screen.blit(purpleStation,[245,121])
        screen.blit(scoreText, (550, 10))
        screen.blit(livesText1, (550, 50))

        #Hit boxes
        redTrainCollider = redTrain.get_rect(topleft=(redTrainX,redTrainY))
        redTrain1Collider = redTrain1.get_rect(topleft=(redTrain1X,redTrain1Y))
        redTrain2Collider = redTrain2.get_rect(topleft=(redTrain2X,redTrain2Y))
        redTrain3Collider = redTrain3.get_rect(topleft=(redTrain3X,redTrain3Y))
        redTrain4Collider = redTrain4.get_rect(topleft=(redTrain4X,redTrain4Y))
        orangeTrainCollider = orangeTrain.get_rect(topleft=(orangeTrainX,orangeTrainY))
        orangeTrain1Collider = orangeTrain1.get_rect(topleft=(orangeTrain1X,orangeTrain1Y))
        orangeTrain2Collider = orangeTrain2.get_rect(topleft=(orangeTrain2X,orangeTrain2Y))
        orangeTrain3Collider = orangeTrain3.get_rect(topleft=(orangeTrain3X,orangeTrain3Y))
        orangeTrain4Collider = orangeTrain4.get_rect(topleft=(orangeTrain4X,orangeTrain4Y))
        yellowTrainCollider = yellowTrain.get_rect(topleft=(yellowTrainX,yellowTrainY))
        yellowTrain1Collider = yellowTrain1.get_rect(topleft=(yellowTrain1X,yellowTrain1Y))
        yellowTrain2Collider = yellowTrain2.get_rect(topleft=(yellowTrain2X,yellowTrain2Y))
        yellowTrain3Collider = yellowTrain3.get_rect(topleft=(yellowTrain3X,yellowTrain3Y))
        yellowTrain4Collider = yellowTrain4.get_rect(topleft=(yellowTrain4X,yellowTrain4Y))
        greenTrainCollider = greenTrain.get_rect(topleft=(greenTrainX,greenTrainY))
        greenTrain1Collider = greenTrain1.get_rect(topleft=(greenTrain1X,greenTrain1Y))
        greenTrain2Collider = greenTrain2.get_rect(topleft=(greenTrain2X,greenTrain2Y))
        greenTrain3Collider = greenTrain3.get_rect(topleft=(greenTrain3X,greenTrain3Y))
        greenTrain4Collider = greenTrain4.get_rect(topleft=(greenTrain4X,greenTrain4Y))
        blueTrainCollider = blueTrain.get_rect(topleft=(blueTrainX,blueTrainY))
        blueTrain1Collider = blueTrain1.get_rect(topleft=(blueTrain1X,blueTrain1Y))
        blueTrain2Collider = blueTrain2.get_rect(topleft=(blueTrain2X,blueTrain2Y))
        blueTrain3Collider = blueTrain3.get_rect(topleft=(blueTrain3X,blueTrain3Y))
        blueTrain4Collider = blueTrain4.get_rect(topleft=(blueTrain4X,blueTrain4Y))
        purpleTrainCollider = purpleTrain.get_rect(topleft=(purpleTrainX,purpleTrainY))
        purpleTrain1Collider = purpleTrain1.get_rect(topleft=(purpleTrain1X,purpleTrain1Y))
        purpleTrain2Collider = purpleTrain2.get_rect(topleft=(purpleTrain2X,purpleTrain2Y))
        purpleTrain3Collider = purpleTrain3.get_rect(topleft=(purpleTrain3X,purpleTrain3Y))
        purpleTrain4Collider = purpleTrain4.get_rect(topleft=(purpleTrain4X,purpleTrain4Y))
        redStationCollider = redStation.get_rect(topleft=(20,10))
        orangeStationCollider = orangeStation.get_rect(topleft=(437,328))
        yellowStationCollider = yellowStation.get_rect(topleft=(120,330))
        greenStationCollider = greenStation.get_rect(topleft=(404,75))
        blueStationCollider = blueStation.get_rect(topleft=(60,90))
        purpleStationCollider = purpleStation.get_rect(topleft=(245,121))

        #Controlling tracks
        if track1Visible == 1:
            screen.blit(track1,[160,159])
        if track1VariationVisible == 1:
            screen.blit(track1Variation,[270,55])
        if track2Visible == 1:
            screen.blit(track2,[442,344])
        if track2VariationVisible == 1:
            screen.blit(track2Variation,[440,360])
        if track3Visible == 1:
            screen.blit(track3,[240,422])
        if track3VariationVisible == 1:
            screen.blit(track3Variation,[250,416])
        if track4Visible == 1:
            screen.blit(track4,[164,55])
        if track4VariationVisible == 1:
            screen.blit(track4Variation,[349,146])
        if track5Visible == 1:
            screen.blit(track5,[158,19])
        if track5VariationVisible == 1:
            screen.blit(track5Variation,[157,20])

        #If a track is clicked, it will switch directions
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if track1Button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    trackNum1Button += 1
                    if trackNum1Button %2 == 0:
                        track1Visible = 0
                        track1VariationVisible = 1
                    else:
                        track1Visible = 1
                        track1VariationVisible = 0

                if track2Button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    trackNum2Button += 1
                    if trackNum2Button %2 == 0:
                        track2Visible = 0
                        track2VariationVisible = 1
                    else:
                        track2Visible = 1
                        track2VariationVisible = 0

                if track3Button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    trackNum3Button += 1
                    if trackNum3Button %2 == 0:
                        track3Visible = 0
                        track3VariationVisible = 1
                    else:
                        track3Visible = 1
                        track3VariationVisible = 0

                if track4Button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    trackNum4Button += 1
                    if trackNum4Button %2 == 0:
                        track4Visible = 0
                        track4VariationVisible = 1
                    else:
                        track4Visible = 1
                        track4VariationVisible = 0

                if track5Button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    trackNum5Button += 1
                    if trackNum5Button %2 == 0:
                        track5Visible = 0
                        track5VariationVisible = 1
                    else:
                        track5Visible = 1
                        track5VariationVisible = 0

        #timePlayed = str(120 - (currenttime.second - startTime))
        #timePlayedText = font.render(timePlayed, True, white)
        #timePlayed1 = int(120 - (currenttime.second - startTime))
        #if timePlayed1 <= 0:
        #    endPopUp = pygame.Rect(120, 90, 400, 300)
        #    pygame.draw.rect(screen, black,startButton)
        #    pygame.draw.rect(screen, black,startButton)
        #    endPopUp = pygame.Rect(375, 350, 100, 50)
        #    pygame.draw.rect(screen, black,startButton)A



        #Assigning which train to blit
        if trainCooldown <= 0:  # only draw train if cooldown time expires
            trainColour = randint(1,6)
            #red train
            if trainColour == 1:
                if redTrainNum0 == 0:
                    redTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif redTrainNum1 == 0:
                    redTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif redTrainNum2 == 0:
                    redTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif redTrainNum3 == 0:
                    redTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif redTrainNum4 == 0:
                    redTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

                #orange train
            if trainColour == 2:
                if orangeTrainNum0 == 0:
                    orangeTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif orangeTrainNum1 == 0:
                    orangeTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif orangeTrainNum2 == 0:
                    orangeTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif orangeTrainNum3 == 0:
                    orangeTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif orangeTrainNum4 == 0:
                    orangeTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

                #yellow train
            if trainColour == 3:
                if yellowTrainNum0 == 0:
                    yellowTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif yellowTrainNum1 == 0:
                    yellowTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif yellowTrainNum2 == 0:
                    yellowTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif yellowTrainNum3 == 0:
                    yellowTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif yellowTrainNum4 == 0:
                    yellowTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

                #green train
            if trainColour == 4:
                if greenTrainNum0 == 0:
                    greenTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif greenTrainNum1 == 0:
                    greenTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif greenTrainNum2 == 0:
                    greenTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif greenTrainNum3 == 0:
                    greenTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif greenTrainNum4 == 0:
                    greenTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

                #blue train
            if trainColour == 5:
                if blueTrainNum0 == 0:
                    blueTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif blueTrainNum1 == 0:
                    blueTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif blueTrainNum2 == 0:
                    blueTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif blueTrainNum3 == 0:
                    blueTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif blueTrainNum4 == 0:
                    blueTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

                #purple train
            if trainColour == 6:
                if purpleTrainNum0 == 0:
                    purpleTrainNum0 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif purpleTrainNum1 == 0:
                    purpleTrainNum1 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif purpleTrainNum2 == 0:
                    purpleTrainNum2 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif purpleTrainNum3 == 0:
                    purpleTrainNum3 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime
                elif purpleTrainNum4 == 0:
                    purpleTrainNum4 = 1
                    trainsOut += 1
                    trainCooldown = coolDownTime

        else:
            trainCooldown -=.25


        #Controlling train movement
        #Red trains
        if redTrainNum0 == 1:
            screen.blit(redTrain,[redTrainX,redTrainY])
            if redTrainTurns == 0:
                redTrainY -= .25
            if redTrainY == 270 and redTrainX == 578:
                redTrainTurns = 1
            if redTrainTurns == 1:
                if redTrainRotation == 0:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 1
                    redTrainTurns = 2
            if redTrainTurns == 2:
                redTrainX -= .25

            #first track
            if redTrainY == 270 and redTrainX == 493:
                if track1Visible == 1:
                    redTrainTurns = 3
                else:
                    redTrainTurns = 23
            if redTrainTurns == 3:
                redTrainX -= .25
            if redTrainX == 329 and redTrainY == 270:
                redTrainTurns = 4
            if redTrainTurns == 4:
                if redTrainRotation == 1:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 2
                    redTrainTurns = 5
            if redTrainTurns == 5:
                redTrainY += .25
            if redTrainX == 329 and redTrainY == 370:
                redTrainTurns = 6
            if redTrainTurns == 6:
                if redTrainRotation == 2:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 3
                    redTrainTurns = 7
            if redTrainTurns == 7:
                redTrainX += .25

            #second track
            if redTrainX == 470 and redTrainY == 370:
                if track2Visible == 1:
                    redTrainTurns = 8
                else:
                    redTrainTurns = 13

            #going to orange station
            if redTrainTurns == 8:
                redTrainX += .25
            if redTrainX == 530 and redTrainY == 370:
                redTrainTurns = 9
            if redTrainTurns == 9:
                if redTrainRotation == 3:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 4
                    redTrainTurns = 10
            if redTrainTurns == 10:
                redTrainY -= .25
            if redTrainX == 530 and redTrainY == 320:
                redTrainTurns = 11
            if redTrainTurns == 11:
                if redTrainRotation == 4:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 5
                    redTrainTurns = 12
            if redTrainTurns == 12:
                redTrainX -= .25
            if redTrainTurns == 13:
                if redTrainRotation == 3:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 6
                    redTrainTurns = 14
            if redTrainTurns == 14:
                redTrainY += .25
            if redTrainY == 432 and redTrainX == 470:
                redTrainTurns = 15
            if redTrainTurns == 15:
                if redTrainRotation == 6:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 7
                    redTrainTurns = 16
            if redTrainTurns == 16:
                redTrainX -= .25

            #Third track
            if redTrainY == 432 and redTrainX == 255:
                if track3Visible == 1:
                    redTrainTurns = 17
                else:
                    redTrainTurns = 21

            #going to yellow station
            if redTrainTurns == 17:
                redTrainX -= .25
            if redTrainY == 432 and redTrainX == 18:
                redTrainTurns = 18
            if redTrainTurns == 18:
                if redTrainRotation == 7:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 8
                    redTrainTurns = 19
            if redTrainTurns == 19:
                redTrainY -= .25
            if redTrainY == 335 and redTrainX == 18:
                if redTrainRotation == 8:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 9
                    redTrainTurns = 20
            if redTrainTurns == 20:
                redTrainX += .25

            #going to purple station
            if redTrainTurns == 21:
                if redTrainRotation == 7:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 10
                    redTrainTurns = 22
            if redTrainTurns == 22:
                redTrainY -= .25

            if redTrainTurns == 23:
                if redTrainRotation == 1:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 11
                    redTrainTurns = 24
            if redTrainTurns == 24:
                redTrainY -= .25

            #fourth track
            if redTrainX == 493 and redTrainY == 178:
                if track4Visible == 1:
                    redTrainTurns = 29
                else:
                    redTrainTurns = 25

            #going to green station
            if redTrainTurns == 25:
                if redTrainRotation == 11:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 12
                    redTrainTurns = 26
            if redTrainTurns == 26:
                redTrainX -= .25
            if redTrainX == 335 and redTrainY == 178:
                if redTrainRotation == 12:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 13
                    redTrainTurns = 27
            if redTrainTurns == 27:
                redTrainY -= .25
            if redTrainX == 335 and redTrainY == 100:
                if redTrainRotation == 13:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 14
                    redTrainTurns = 28
            if redTrainTurns == 28:
                redTrainX += .25

            if redTrainTurns == 29:
                redTrainY -= .25
            if redTrainX == 493 and redTrainY == 27:
                if redTrainRotation == 11:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 15
                    redTrainTurns = 30
            if redTrainTurns == 30:
                redTrainX -= .25

            #fifth track
            if redTrainX == 165 and redTrainY == 27:
                if track5Visible == 1:
                    redTrainTurns = 31
                else:
                    redTrainTurns = 32

            #going to red station
            if redTrainTurns == 31:
                redTrainX -= .25

            #going to blue station
            if redTrainTurns == 32:
                if redTrainRotation == 15:
                    redTrain = pygame.transform.rotate(redTrain, 90)
                    redTrainRotation = 16
                    redTrainTurns = 33
            if redTrainTurns == 33:
                redTrainY += .25
            if redTrainX == 165 and redTrainY == 257:
                if redTrainRotation == 16:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 17
                    redTrainTurns = 34
            if redTrainTurns == 34:
                redTrainX -= .25
            if redTrainX == 71 and redTrainY == 257:
                if redTrainRotation == 17:
                    redTrain = pygame.transform.rotate(redTrain, 270)
                    redTrainRotation = 18
                    redTrainTurns = 35
            if redTrainTurns == 35:
                redTrainY -= .25

        if redTrainNum1 == 1:
            screen.blit(redTrain1,[redTrain1X,redTrain1Y])
            if redTrain1Turns == 0:
                redTrain1Y -= .25
            if redTrain1Y == 270 and redTrain1X == 578:
                redTrain1Turns = 1
            if redTrain1Turns == 1:
                if redTrain1Rotation == 0:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 1
                    redTrain1Turns = 2
            if redTrain1Turns == 2:
                redTrain1X -= .25

            #first track
            if redTrain1Y == 270 and redTrain1X == 493:
                if track1Visible == 1:
                    redTrain1Turns = 3
                else:
                    redTrain1Turns = 23
            if redTrain1Turns == 3:
                redTrain1X -= .25
            if redTrain1X == 329 and redTrain1Y == 270:
                redTrain1Turns = 4
            if redTrain1Turns == 4:
                if redTrain1Rotation == 1:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 2
                    redTrain1Turns = 5
            if redTrain1Turns == 5:
                redTrain1Y += .25
            if redTrain1X == 329 and redTrain1Y == 370:
                redTrain1Turns = 6
            if redTrain1Turns == 6:
                if redTrain1Rotation == 2:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 3
                    redTrain1Turns = 7
            if redTrain1Turns == 7:
                redTrain1X += .25

            #second track
            if redTrain1X == 470 and redTrain1Y == 370:
                if track2Visible == 1:
                    redTrain1Turns = 8
                else:
                    redTrain1Turns = 13

            #going to orange station
            if redTrain1Turns == 8:
                redTrain1X += .25
            if redTrain1X == 530 and redTrain1Y == 370:
                redTrain1Turns = 9
            if redTrain1Turns == 9:
                if redTrain1Rotation == 3:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 4
                    redTrain1Turns = 10
            if redTrain1Turns == 10:
                redTrain1Y -= .25
            if redTrain1X == 530 and redTrain1Y == 320:
                redTrain1Turns = 11
            if redTrain1Turns == 11:
                if redTrain1Rotation == 4:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 5
                    redTrain1Turns = 12
            if redTrain1Turns == 12:
                redTrain1X -= .25
            if redTrain1Turns == 13:
                if redTrain1Rotation == 3:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 6
                    redTrain1Turns = 14
            if redTrain1Turns == 14:
                redTrain1Y += .25
            if redTrain1Y == 432 and redTrain1X == 470:
                redTrain1Turns = 15
            if redTrain1Turns == 15:
                if redTrain1Rotation == 6:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 7
                    redTrain1Turns = 16
            if redTrain1Turns == 16:
                redTrain1X -= .25

            #Third track
            if redTrain1Y == 432 and redTrain1X == 255:
                if track3Visible == 1:
                    redTrain1Turns = 17
                else:
                    redTrain1Turns = 21

            #going to yellow station
            if redTrain1Turns == 17:
                redTrain1X -= .25
            if redTrain1Y == 432 and redTrain1X == 18:
                redTrain1Turns = 18
            if redTrain1Turns == 18:
                if redTrain1Rotation == 7:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 8
                    redTrain1Turns = 19
            if redTrain1Turns == 19:
                redTrain1Y -= .25
            if redTrain1Y == 335 and redTrain1X == 18:
                if redTrain1Rotation == 8:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 9
                    redTrain1Turns = 20
            if redTrain1Turns == 20:
                redTrain1X += .25

            #going to purple station
            if redTrain1Turns == 21:
                if redTrain1Rotation == 7:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 10
                    redTrain1Turns = 22
            if redTrain1Turns == 22:
                redTrain1Y -= .25

            if redTrain1Turns == 23:
                if redTrain1Rotation == 1:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 11
                    redTrain1Turns = 24
            if redTrain1Turns == 24:
                redTrain1Y -= .25

            #fourth track
            if redTrain1X == 493 and redTrain1Y == 178:
                if track4Visible == 1:
                    redTrain1Turns = 29
                else:
                    redTrain1Turns = 25

            #going to green station
            if redTrain1Turns == 25:
                if redTrain1Rotation == 11:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 12
                    redTrain1Turns = 26
            if redTrain1Turns == 26:
                redTrain1X -= .25
            if redTrain1X == 335 and redTrain1Y == 178:
                if redTrain1Rotation == 12:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 13
                    redTrain1Turns = 27
            if redTrain1Turns == 27:
                redTrain1Y -= .25
            if redTrain1X == 335 and redTrain1Y == 100:
                if redTrain1Rotation == 13:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 14
                    redTrain1Turns = 28
            if redTrain1Turns == 28:
                redTrain1X += .25

            if redTrain1Turns == 29:
                redTrain1Y -= .25
            if redTrain1X == 493 and redTrain1Y == 27:
                if redTrain1Rotation == 11:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 15
                    redTrain1Turns = 30
            if redTrain1Turns == 30:
                redTrain1X -= .25

            #fifth track
            if redTrain1X == 165 and redTrain1Y == 27:
                if track5Visible == 1:
                    redTrain1Turns = 31
                else:
                    redTrain1Turns = 32

            #going to red station
            if redTrain1Turns == 31:
                redTrain1X -= .25

            #going to blue station
            if redTrain1Turns == 32:
                if redTrain1Rotation == 15:
                    redTrain1 = pygame.transform.rotate(redTrain1, 90)
                    redTrain1Rotation = 16
                    redTrain1Turns = 33
            if redTrain1Turns == 33:
                redTrain1Y += .25
            if redTrain1X == 165 and redTrain1Y == 257:
                if redTrain1Rotation == 16:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 17
                    redTrain1Turns = 34
            if redTrain1Turns == 34:
                redTrain1X -= .25
            if redTrain1X == 71 and redTrain1Y == 257:
                if redTrain1Rotation == 17:
                    redTrain1 = pygame.transform.rotate(redTrain1, 270)
                    redTrain1Rotation = 18
                    redTrain1Turns = 35
            if redTrain1Turns == 35:
                redTrain1Y -= .25


        if redTrainNum2 == 1:
            screen.blit(redTrain2,[redTrain2X,redTrain2Y])
            if redTrain2Turns == 0:
                redTrain2Y -= .25
            if redTrain2Y == 270 and redTrain2X == 578:
                redTrain2Turns = 1
            if redTrain2Turns == 1:
                if redTrain2Rotation == 0:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 1
                    redTrain2Turns = 2
            if redTrain2Turns == 2:
                redTrain2X -= .25

            #first track
            if redTrain2Y == 270 and redTrain2X == 493:
                if track1Visible == 1:
                    redTrain2Turns = 3
                else:
                    redTrain2Turns = 23
            if redTrain2Turns == 3:
                redTrain2X -= .25
            if redTrain2X == 329 and redTrain2Y == 270:
                redTrain2Turns = 4
            if redTrain2Turns == 4:
                if redTrain2Rotation == 1:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 2
                    redTrain2Turns = 5
            if redTrain2Turns == 5:
                redTrain2Y += .25
            if redTrain2X == 329 and redTrain2Y == 370:
                redTrain2Turns = 6
            if redTrain2Turns == 6:
                if redTrain2Rotation == 2:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 3
                    redTrain2Turns = 7
            if redTrain2Turns == 7:
                redTrain2X += .25

            #second track
            if redTrain2X == 470 and redTrain2Y == 370:
                if track2Visible == 1:
                    redTrain2Turns = 8
                else:
                    redTrain2Turns = 13

            #going to orange station
            if redTrain2Turns == 8:
                redTrain2X += .25
            if redTrain2X == 530 and redTrain2Y == 370:
                redTrain2Turns = 9
            if redTrain2Turns == 9:
                if redTrain2Rotation == 3:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 4
                    redTrain2Turns = 10
            if redTrain2Turns == 10:
                redTrain2Y -= .25
            if redTrain2X == 530 and redTrain2Y == 320:
                redTrain2Turns = 11
            if redTrain2Turns == 11:
                if redTrain2Rotation == 4:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 5
                    redTrain2Turns = 12
            if redTrain2Turns == 12:
                redTrain2X -= .25
            if redTrain2Turns == 13:
                if redTrain2Rotation == 3:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 6
                    redTrain2Turns = 14
            if redTrain2Turns == 14:
                redTrain2Y += .25
            if redTrain2Y == 432 and redTrain2X == 470:
                redTrain2Turns = 15
            if redTrain2Turns == 15:
                if redTrain2Rotation == 6:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 7
                    redTrain2Turns = 16
            if redTrain2Turns == 16:
                redTrain2X -= .25

            #Third track
            if redTrain2Y == 432 and redTrain2X == 255:
                if track3Visible == 1:
                    redTrain2Turns = 17
                else:
                    redTrain2Turns = 21

            #going to yellow station
            if redTrain2Turns == 17:
                redTrain2X -= .25
            if redTrain2Y == 432 and redTrain2X == 18:
                redTrain2Turns = 18
            if redTrain2Turns == 18:
                if redTrain2Rotation == 7:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 8
                    redTrain2Turns = 19
            if redTrain2Turns == 19:
                redTrain2Y -= .25
            if redTrain2Y == 335 and redTrain2X == 18:
                if redTrain2Rotation == 8:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 9
                    redTrain2Turns = 20
            if redTrain2Turns == 20:
                redTrain2X += .25

            #going to purple station
            if redTrain2Turns == 21:
                if redTrain2Rotation == 7:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 10
                    redTrain2Turns = 22
            if redTrain2Turns == 22:
                redTrain2Y -= .25

            if redTrain2Turns == 23:
                if redTrain2Rotation == 1:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 11
                    redTrain2Turns = 24
            if redTrain2Turns == 24:
                redTrain2Y -= .25

            #fourth track
            if redTrain2X == 493 and redTrain2Y == 178:
                if track4Visible == 1:
                    redTrain2Turns = 29
                else:
                    redTrain2Turns = 25

            #going to green station
            if redTrain2Turns == 25:
                if redTrain2Rotation == 11:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 12
                    redTrain2Turns = 26
            if redTrain2Turns == 26:
                redTrain2X -= .25
            if redTrain2X == 335 and redTrain2Y == 178:
                if redTrain2Rotation == 12:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 13
                    redTrain2Turns = 27
            if redTrain2Turns == 27:
                redTrain2Y -= .25
            if redTrain2X == 335 and redTrain2Y == 100:
                if redTrain2Rotation == 13:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 14
                    redTrain2Turns = 28
            if redTrain2Turns == 28:
                redTrain2X += .25

            if redTrain2Turns == 29:
                redTrain2Y -= .25
            if redTrain2X == 493 and redTrain2Y == 27:
                if redTrain2Rotation == 11:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 15
                    redTrain2Turns = 30
            if redTrain2Turns == 30:
                redTrain2X -= .25

            #fifth track
            if redTrain2X == 165 and redTrain2Y == 27:
                if track5Visible == 1:
                    redTrain2Turns = 31
                else:
                    redTrain2Turns = 32

            #going to red station
            if redTrain2Turns == 31:
                redTrain2X -= .25

            #going to blue station
            if redTrain2Turns == 32:
                if redTrain2Rotation == 15:
                    redTrain2 = pygame.transform.rotate(redTrain2, 90)
                    redTrain2Rotation = 16
                    redTrain2Turns = 33
            if redTrain2Turns == 33:
                redTrain2Y += .25
            if redTrain2X == 165 and redTrain2Y == 257:
                if redTrain2Rotation == 16:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 17
                    redTrain2Turns = 34
            if redTrain2Turns == 34:
                redTrain2X -= .25
            if redTrain2X == 71 and redTrain2Y == 257:
                if redTrain2Rotation == 17:
                    redTrain2 = pygame.transform.rotate(redTrain2, 270)
                    redTrain2Rotation = 18
                    redTrain2Turns = 35
            if redTrain2Turns == 35:
                redTrain2Y -= .25

        if redTrainNum3 == 1:
            screen.blit(redTrain3,[redTrain3X,redTrain3Y])
            if redTrain3Turns == 0:
                redTrain3Y -= .25
            if redTrain3Y == 270 and redTrain3X == 578:
                redTrain3Turns = 1
            if redTrain3Turns == 1:
                if redTrain3Rotation == 0:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 1
                    redTrain3Turns = 2
            if redTrain3Turns == 2:
                redTrain3X -= .25

            #first track
            if redTrain3Y == 270 and redTrain3X == 493:
                if track1Visible == 1:
                    redTrain3Turns = 3
                else:
                    redTrain3Turns = 23
            if redTrain3Turns == 3:
                redTrain3X -= .25
            if redTrain3X == 329 and redTrain3Y == 270:
                redTrain3Turns = 4
            if redTrain3Turns == 4:
                if redTrain3Rotation == 1:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 2
                    redTrain3Turns = 5
            if redTrain3Turns == 5:
                redTrain3Y += .25
            if redTrain3X == 329 and redTrain3Y == 370:
                redTrain3Turns = 6
            if redTrain3Turns == 6:
                if redTrain3Rotation == 2:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 3
                    redTrain3Turns = 7
            if redTrain3Turns == 7:
                redTrain3X += .25

            #second track
            if redTrain3X == 470 and redTrain3Y == 370:
                if track2Visible == 1:
                    redTrain3Turns = 8
                else:
                    redTrain3Turns = 13

            #going to orange station
            if redTrain3Turns == 8:
                redTrain3X += .25
            if redTrain3X == 530 and redTrain3Y == 370:
                redTrain3Turns = 9
            if redTrain3Turns == 9:
                if redTrain3Rotation == 3:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 4
                    redTrain3Turns = 10
            if redTrain3Turns == 10:
                redTrain3Y -= .25
            if redTrain3X == 530 and redTrain3Y == 320:
                redTrain3Turns = 11
            if redTrain3Turns == 11:
                if redTrain3Rotation == 4:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 5
                    redTrain3Turns = 12
            if redTrain3Turns == 12:
                redTrain3X -= .25
            if redTrain3Turns == 13:
                if redTrain3Rotation == 3:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 6
                    redTrain3Turns = 14
            if redTrain3Turns == 14:
                redTrain3Y += .25
            if redTrain3Y == 432 and redTrain3X == 470:
                redTrain3Turns = 15
            if redTrain3Turns == 15:
                if redTrain3Rotation == 6:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 7
                    redTrain3Turns = 16
            if redTrain3Turns == 16:
                redTrain3X -= .25

            #Third track
            if redTrain3Y == 432 and redTrain3X == 255:
                if track3Visible == 1:
                    redTrain3Turns = 17
                else:
                    redTrain3Turns = 21

            #going to yellow station
            if redTrain3Turns == 17:
                redTrain3X -= .25
            if redTrain3Y == 432 and redTrain3X == 18:
                redTrain3Turns = 18
            if redTrain3Turns == 18:
                if redTrain3Rotation == 7:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 8
                    redTrain3Turns = 19
            if redTrain3Turns == 19:
                redTrain3Y -= .25
            if redTrain3Y == 335 and redTrain3X == 18:
                if redTrain3Rotation == 8:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 9
                    redTrain3Turns = 20
            if redTrain3Turns == 20:
                redTrain3X += .25

            #going to purple station
            if redTrain3Turns == 21:
                if redTrain3Rotation == 7:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 10
                    redTrain3Turns = 22
            if redTrain3Turns == 22:
                redTrain3Y -= .25

            if redTrain3Turns == 23:
                if redTrain3Rotation == 1:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 11
                    redTrain3Turns = 24
            if redTrain3Turns == 24:
                redTrain3Y -= .25

            #fourth track
            if redTrain3X == 493 and redTrain3Y == 178:
                if track4Visible == 1:
                    redTrain3Turns = 29
                else:
                    redTrain3Turns = 25

            #going to green station
            if redTrain3Turns == 25:
                if redTrain3Rotation == 11:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 12
                    redTrain3Turns = 26
            if redTrain3Turns == 26:
                redTrain3X -= .25
            if redTrain3X == 335 and redTrain3Y == 178:
                if redTrain3Rotation == 12:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 13
                    redTrain3Turns = 27
            if redTrain3Turns == 27:
                redTrain3Y -= .25
            if redTrain3X == 335 and redTrain3Y == 100:
                if redTrain3Rotation == 13:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 14
                    redTrain3Turns = 28
            if redTrain3Turns == 28:
                redTrain3X += .25

            if redTrain3Turns == 29:
                redTrain3Y -= .25
            if redTrain3X == 493 and redTrain3Y == 27:
                if redTrain3Rotation == 11:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 15
                    redTrain3Turns = 30
            if redTrain3Turns == 30:
                redTrain3X -= .25

            #fifth track
            if redTrain3X == 165 and redTrain3Y == 27:
                if track5Visible == 1:
                    redTrain3Turns = 31
                else:
                    redTrain3Turns = 32

            #going to red station
            if redTrain3Turns == 31:
                redTrain3X -= .25

            #going to blue station
            if redTrain3Turns == 32:
                if redTrain3Rotation == 15:
                    redTrain3 = pygame.transform.rotate(redTrain3, 90)
                    redTrain3Rotation = 16
                    redTrain3Turns = 33
            if redTrain3Turns == 33:
                redTrain3Y += .25
            if redTrain3X == 165 and redTrain3Y == 257:
                if redTrain3Rotation == 16:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 17
                    redTrain3Turns = 34
            if redTrain3Turns == 34:
                redTrain3X -= .25
            if redTrain3X == 71 and redTrain3Y == 257:
                if redTrain3Rotation == 17:
                    redTrain3 = pygame.transform.rotate(redTrain3, 270)
                    redTrain3Rotation = 18
                    redTrain3Turns = 35
            if redTrain3Turns == 35:
                redTrain3Y -= .25


        if redTrainNum4 == 1:
            screen.blit(redTrain4,[redTrain4X,redTrain4Y])
            if redTrain4Turns == 0:
                redTrain4Y -= .25
            if redTrain4Y == 270 and redTrain4X == 578:
                redTrain4Turns = 1
            if redTrain4Turns == 1:
                if redTrain4Rotation == 0:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 1
                    redTrain4Turns = 2
            if redTrain4Turns == 2:
                redTrain4X -= .25

            #first track
            if redTrain4Y == 270 and redTrain4X == 493:
                if track1Visible == 1:
                    redTrain4Turns = 3
                else:
                    redTrain4Turns = 23
            if redTrain4Turns == 3:
                redTrain4X -= .25
            if redTrain4X == 329 and redTrain4Y == 270:
                redTrain4Turns = 4
            if redTrain4Turns == 4:
                if redTrain4Rotation == 1:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 2
                    redTrain4Turns = 5
            if redTrain4Turns == 5:
                redTrain4Y += .25
            if redTrain4X == 329 and redTrain4Y == 370:
                redTrain4Turns = 6
            if redTrain4Turns == 6:
                if redTrain4Rotation == 2:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 3
                    redTrain4Turns = 7
            if redTrain4Turns == 7:
                redTrain4X += .25

            #second track
            if redTrain4X == 470 and redTrain4Y == 370:
                if track2Visible == 1:
                    redTrain4Turns = 8
                else:
                    redTrain4Turns = 13

            #going to orange station
            if redTrain4Turns == 8:
                redTrain4X += .25
            if redTrain4X == 530 and redTrain4Y == 370:
                redTrain4Turns = 9
            if redTrain4Turns == 9:
                if redTrain4Rotation == 3:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 4
                    redTrain4Turns = 10
            if redTrain4Turns == 10:
                redTrain4Y -= .25
            if redTrain4X == 530 and redTrain4Y == 320:
                redTrain4Turns = 11
            if redTrain4Turns == 11:
                if redTrain4Rotation == 4:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 5
                    redTrain4Turns = 12
            if redTrain4Turns == 12:
                redTrain4X -= .25
            if redTrain4Turns == 13:
                if redTrain4Rotation == 3:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 6
                    redTrain4Turns = 14
            if redTrain4Turns == 14:
                redTrain4Y += .25
            if redTrain4Y == 432 and redTrain4X == 470:
                redTrain4Turns = 15
            if redTrain4Turns == 15:
                if redTrain4Rotation == 6:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 7
                    redTrain4Turns = 16
            if redTrain4Turns == 16:
                redTrain4X -= .25

            #Third track
            if redTrain4Y == 432 and redTrain4X == 255:
                if track3Visible == 1:
                    redTrain4Turns = 17
                else:
                    redTrain4Turns = 21

            #going to yellow station
            if redTrain4Turns == 17:
                redTrain4X -= .25
            if redTrain4Y == 432 and redTrain4X == 18:
                redTrain4Turns = 18
            if redTrain4Turns == 18:
                if redTrain4Rotation == 7:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 8
                    redTrain4Turns = 19
            if redTrain4Turns == 19:
                redTrain4Y -= .25
            if redTrain4Y == 335 and redTrain4X == 18:
                if redTrain4Rotation == 8:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 9
                    redTrain4Turns = 20
            if redTrain4Turns == 20:
                redTrain4X += .25

            #going to purple station
            if redTrain4Turns == 21:
                if redTrain4Rotation == 7:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 10
                    redTrain4Turns = 22
            if redTrain4Turns == 22:
                redTrain4Y -= .25

            if redTrain4Turns == 23:
                if redTrain4Rotation == 1:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 11
                    redTrain4Turns = 24
            if redTrain4Turns == 24:
                redTrain4Y -= .25

            #fourth track
            if redTrain4X == 493 and redTrain4Y == 178:
                if track4Visible == 1:
                    redTrain4Turns = 29
                else:
                    redTrain4Turns = 25

            #going to green station
            if redTrain4Turns == 25:
                if redTrain4Rotation == 11:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 12
                    redTrain4Turns = 26
            if redTrain4Turns == 26:
                redTrain4X -= .25
            if redTrain4X == 335 and redTrain4Y == 178:
                if redTrain4Rotation == 12:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 13
                    redTrain4Turns = 27
            if redTrain4Turns == 27:
                redTrain4Y -= .25
            if redTrain4X == 335 and redTrain4Y == 100:
                if redTrain4Rotation == 13:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 14
                    redTrain4Turns = 28
            if redTrain4Turns == 28:
                redTrain4X += .25

            if redTrain4Turns == 29:
                redTrain4Y -= .25
            if redTrain4X == 493 and redTrain4Y == 27:
                if redTrain4Rotation == 11:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 15
                    redTrain4Turns = 30
            if redTrain4Turns == 30:
                redTrain4X -= .25

            #fifth track
            if redTrain4X == 165 and redTrain4Y == 27:
                if track5Visible == 1:
                    redTrain4Turns = 31
                else:
                    redTrain4Turns = 32

            #going to red station
            if redTrain4Turns == 31:
                redTrain4X -= .25

            #going to blue station
            if redTrain4Turns == 32:
                if redTrain4Rotation == 15:
                    redTrain4 = pygame.transform.rotate(redTrain4, 90)
                    redTrain4Rotation = 16
                    redTrain4Turns = 33
            if redTrain4Turns == 33:
                redTrain4Y += .25
            if redTrain4X == 165 and redTrain4Y == 257:
                if redTrain4Rotation == 16:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 17
                    redTrain4Turns = 34
            if redTrain4Turns == 34:
                redTrain4X -= .25
            if redTrain4X == 71 and redTrain4Y == 257:
                if redTrain4Rotation == 17:
                    redTrain4 = pygame.transform.rotate(redTrain4, 270)
                    redTrain4Rotation = 18
                    redTrain4Turns = 35
            if redTrain4Turns == 35:
                redTrain4Y -= .25


        if orangeTrainNum0 == 1:
            screen.blit(orangeTrain,[orangeTrainX,orangeTrainY])
            if orangeTrainTurns == 0:
                orangeTrainY -= .25
            if orangeTrainY == 270 and orangeTrainX == 578:
                orangeTrainTurns = 1
            if orangeTrainTurns == 1:
                if orangeTrainRotation == 0:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 1
                    orangeTrainTurns = 2
            if orangeTrainTurns == 2:
                orangeTrainX -= .25

            #first track
            if orangeTrainY == 270 and orangeTrainX == 493:
                if track1Visible == 1:
                    orangeTrainTurns = 3
                else:
                    orangeTrainTurns = 23
            if orangeTrainTurns == 3:
                orangeTrainX -= .25
            if orangeTrainX == 329 and orangeTrainY == 270:
                orangeTrainTurns = 4
            if orangeTrainTurns == 4:
                if orangeTrainRotation == 1:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 2
                    orangeTrainTurns = 5
            if orangeTrainTurns == 5:
                orangeTrainY += .25
            if orangeTrainX == 329 and orangeTrainY == 370:
                orangeTrainTurns = 6
            if orangeTrainTurns == 6:
                if orangeTrainRotation == 2:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 3
                    orangeTrainTurns = 7
            if orangeTrainTurns == 7:
                orangeTrainX += .25

            #second track
            if orangeTrainX == 470 and orangeTrainY == 370:
                if track2Visible == 1:
                    orangeTrainTurns = 8
                else:
                    orangeTrainTurns = 13

            #going to orange station
            if orangeTrainTurns == 8:
                orangeTrainX += .25
            if orangeTrainX == 530 and orangeTrainY == 370:
                orangeTrainTurns = 9
            if orangeTrainTurns == 9:
                if orangeTrainRotation == 3:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 4
                    orangeTrainTurns = 10
            if orangeTrainTurns == 10:
                orangeTrainY -= .25
            if orangeTrainX == 530 and orangeTrainY == 320:
                orangeTrainTurns = 11
            if orangeTrainTurns == 11:
                if orangeTrainRotation == 4:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 5
                    orangeTrainTurns = 12
            if orangeTrainTurns == 12:
                orangeTrainX -= .25
            if orangeTrainTurns == 13:
                if orangeTrainRotation == 3:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 6
                    orangeTrainTurns = 14
            if orangeTrainTurns == 14:
                orangeTrainY += .25
            if orangeTrainY == 432 and orangeTrainX == 470:
                orangeTrainTurns = 15
            if orangeTrainTurns == 15:
                if orangeTrainRotation == 6:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 7
                    orangeTrainTurns = 16
            if orangeTrainTurns == 16:
                orangeTrainX -= .25

            #Third track
            if orangeTrainY == 432 and orangeTrainX == 255:
                if track3Visible == 1:
                    orangeTrainTurns = 17
                else:
                    orangeTrainTurns = 21

            #going to yellow station
            if orangeTrainTurns == 17:
                orangeTrainX -= .25
            if orangeTrainY == 432 and orangeTrainX == 18:
                orangeTrainTurns = 18
            if orangeTrainTurns == 18:
                if orangeTrainRotation == 7:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 8
                    orangeTrainTurns = 19
            if orangeTrainTurns == 19:
                orangeTrainY -= .25
            if orangeTrainY == 335 and orangeTrainX == 18:
                if orangeTrainRotation == 8:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 9
                    orangeTrainTurns = 20
            if orangeTrainTurns == 20:
                orangeTrainX += .25

            #going to purple station
            if orangeTrainTurns == 21:
                if orangeTrainRotation == 7:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 10
                    orangeTrainTurns = 22
            if orangeTrainTurns == 22:
                orangeTrainY -= .25

            if orangeTrainTurns == 23:
                if orangeTrainRotation == 1:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 11
                    orangeTrainTurns = 24
            if orangeTrainTurns == 24:
                orangeTrainY -= .25

            #fourth track
            if orangeTrainX == 493 and orangeTrainY == 178:
                if track4Visible == 1:
                    orangeTrainTurns = 29
                else:
                    orangeTrainTurns = 25

            #going to green station
            if orangeTrainTurns == 25:
                if orangeTrainRotation == 11:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 12
                    orangeTrainTurns = 26
            if orangeTrainTurns == 26:
                orangeTrainX -= .25
            if orangeTrainX == 335 and orangeTrainY == 178:
                if orangeTrainRotation == 12:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 13
                    orangeTrainTurns = 27
            if orangeTrainTurns == 27:
                orangeTrainY -= .25
            if orangeTrainX == 335 and orangeTrainY == 100:
                if orangeTrainRotation == 13:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 14
                    orangeTrainTurns = 28
            if orangeTrainTurns == 28:
                orangeTrainX += .25

            if orangeTrainTurns == 29:
                orangeTrainY -= .25
            if orangeTrainX == 493 and orangeTrainY == 27:
                if orangeTrainRotation == 11:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 15
                    orangeTrainTurns = 30
            if orangeTrainTurns == 30:
                orangeTrainX -= .25

            #fifth track
            if orangeTrainX == 165 and orangeTrainY == 27:
                if track5Visible == 1:
                    orangeTrainTurns = 31
                else:
                    orangeTrainTurns = 32

            #going to red station
            if orangeTrainTurns == 31:
                orangeTrainX -= .25

            #going to blue station
            if orangeTrainTurns == 32:
                if orangeTrainRotation == 15:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 90)
                    orangeTrainRotation = 16
                    orangeTrainTurns = 33
            if orangeTrainTurns == 33:
                orangeTrainY += .25
            if orangeTrainX == 165 and orangeTrainY == 257:
                if orangeTrainRotation == 16:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 17
                    orangeTrainTurns = 34
            if orangeTrainTurns == 34:
                orangeTrainX -= .25
            if orangeTrainX == 71 and orangeTrainY == 257:
                if orangeTrainRotation == 17:
                    orangeTrain = pygame.transform.rotate(orangeTrain, 270)
                    orangeTrainRotation = 18
                    orangeTrainTurns = 35
            if orangeTrainTurns == 35:
                orangeTrainY -= .25

        if orangeTrainNum1 == 1:
            screen.blit(orangeTrain1,[orangeTrain1X,orangeTrain1Y])
            if orangeTrain1Turns == 0:
                orangeTrain1Y -= .25
            if orangeTrain1Y == 270 and orangeTrain1X == 578:
                orangeTrain1Turns = 1
            if orangeTrain1Turns == 1:
                if orangeTrain1Rotation == 0:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 1
                    orangeTrain1Turns = 2
            if orangeTrain1Turns == 2:
                orangeTrain1X -= .25

            #first track
            if orangeTrain1Y == 270 and orangeTrain1X == 493:
                if track1Visible == 1:
                    orangeTrain1Turns = 3
                else:
                    orangeTrain1Turns = 23
            if orangeTrain1Turns == 3:
                orangeTrain1X -= .25
            if orangeTrain1X == 329 and orangeTrain1Y == 270:
                orangeTrain1Turns = 4
            if orangeTrain1Turns == 4:
                if orangeTrain1Rotation == 1:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 2
                    orangeTrain1Turns = 5
            if orangeTrain1Turns == 5:
                orangeTrain1Y += .25
            if orangeTrain1X == 329 and orangeTrain1Y == 370:
                orangeTrain1Turns = 6
            if orangeTrain1Turns == 6:
                if orangeTrain1Rotation == 2:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 3
                    orangeTrain1Turns = 7
            if orangeTrain1Turns == 7:
                orangeTrain1X += .25

            #second track
            if orangeTrain1X == 470 and orangeTrain1Y == 370:
                if track2Visible == 1:
                    orangeTrain1Turns = 8
                else:
                    orangeTrain1Turns = 13

            #going to orange station
            if orangeTrain1Turns == 8:
                orangeTrain1X += .25
            if orangeTrain1X == 530 and orangeTrain1Y == 370:
                orangeTrain1Turns = 9
            if orangeTrain1Turns == 9:
                if orangeTrain1Rotation == 3:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 4
                    orangeTrain1Turns = 10
            if orangeTrain1Turns == 10:
                orangeTrain1Y -= .25
            if orangeTrain1X == 530 and orangeTrain1Y == 320:
                orangeTrain1Turns = 11
            if orangeTrain1Turns == 11:
                if orangeTrain1Rotation == 4:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 5
                    orangeTrain1Turns = 12
            if orangeTrain1Turns == 12:
                orangeTrain1X -= .25
            if orangeTrain1Turns == 13:
                if orangeTrain1Rotation == 3:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 6
                    orangeTrain1Turns = 14
            if orangeTrain1Turns == 14:
                orangeTrain1Y += .25
            if orangeTrain1Y == 432 and orangeTrain1X == 470:
                orangeTrain1Turns = 15
            if orangeTrain1Turns == 15:
                if orangeTrain1Rotation == 6:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 7
                    orangeTrain1Turns = 16
            if orangeTrain1Turns == 16:
                orangeTrain1X -= .25

            #Third track
            if orangeTrain1Y == 432 and orangeTrain1X == 255:
                if track3Visible == 1:
                    orangeTrain1Turns = 17
                else:
                    orangeTrain1Turns = 21

            #going to yellow station
            if orangeTrain1Turns == 17:
                orangeTrain1X -= .25
            if orangeTrain1Y == 432 and orangeTrain1X == 18:
                orangeTrain1Turns = 18
            if orangeTrain1Turns == 18:
                if orangeTrain1Rotation == 7:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 8
                    orangeTrain1Turns = 19
            if orangeTrain1Turns == 19:
                orangeTrain1Y -= .25
            if orangeTrain1Y == 335 and orangeTrain1X == 18:
                if orangeTrain1Rotation == 8:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 9
                    orangeTrain1Turns = 20
            if orangeTrain1Turns == 20:
                orangeTrain1X += .25

            #going to purple station
            if orangeTrain1Turns == 21:
                if orangeTrain1Rotation == 7:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 10
                    orangeTrain1Turns = 22
            if orangeTrain1Turns == 22:
                orangeTrain1Y -= .25

            if orangeTrain1Turns == 23:
                if orangeTrain1Rotation == 1:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 11
                    orangeTrain1Turns = 24
            if orangeTrain1Turns == 24:
                orangeTrain1Y -= .25

            #fourth track
            if orangeTrain1X == 493 and orangeTrain1Y == 178:
                if track4Visible == 1:
                    orangeTrain1Turns = 29
                else:
                    orangeTrain1Turns = 25

            #going to green station
            if orangeTrain1Turns == 25:
                if orangeTrain1Rotation == 11:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 12
                    orangeTrain1Turns = 26
            if orangeTrain1Turns == 26:
                orangeTrain1X -= .25
            if orangeTrain1X == 335 and orangeTrain1Y == 178:
                if orangeTrain1Rotation == 12:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 13
                    orangeTrain1Turns = 27
            if orangeTrain1Turns == 27:
                orangeTrain1Y -= .25
            if orangeTrain1X == 335 and orangeTrain1Y == 100:
                if orangeTrain1Rotation == 13:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 14
                    orangeTrain1Turns = 28
            if orangeTrain1Turns == 28:
                orangeTrain1X += .25

            if orangeTrain1Turns == 29:
                orangeTrain1Y -= .25
            if orangeTrain1X == 493 and orangeTrain1Y == 27:
                if orangeTrain1Rotation == 11:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 15
                    orangeTrain1Turns = 30
            if orangeTrain1Turns == 30:
                orangeTrain1X -= .25

            #fifth track
            if orangeTrain1X == 165 and orangeTrain1Y == 27:
                if track5Visible == 1:
                    orangeTrain1Turns = 31
                else:
                    orangeTrain1Turns = 32

            #going to red station
            if orangeTrain1Turns == 31:
                orangeTrain1X -= .25

            #going to blue station
            if orangeTrain1Turns == 32:
                if orangeTrain1Rotation == 15:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
                    orangeTrain1Rotation = 16
                    orangeTrain1Turns = 33
            if orangeTrain1Turns == 33:
                orangeTrain1Y += .25
            if orangeTrain1X == 165 and orangeTrain1Y == 257:
                if orangeTrain1Rotation == 16:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 17
                    orangeTrain1Turns = 34
            if orangeTrain1Turns == 34:
                orangeTrain1X -= .25
            if orangeTrain1X == 71 and orangeTrain1Y == 257:
                if orangeTrain1Rotation == 17:
                    orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
                    orangeTrain1Rotation = 18
                    orangeTrain1Turns = 35
            if orangeTrain1Turns == 35:
                orangeTrain1Y -= .25


        if orangeTrainNum2 == 1:
            screen.blit(orangeTrain2,[orangeTrain2X,orangeTrain2Y])
            if orangeTrain2Turns == 0:
                orangeTrain2Y -= .25
            if orangeTrain2Y == 270 and orangeTrain2X == 578:
                orangeTrain2Turns = 1
            if orangeTrain2Turns == 1:
                if orangeTrain2Rotation == 0:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 1
                    orangeTrain2Turns = 2
            if orangeTrain2Turns == 2:
                orangeTrain2X -= .25

            #first track
            if orangeTrain2Y == 270 and orangeTrain2X == 493:
                if track1Visible == 1:
                    orangeTrain2Turns = 3
                else:
                    orangeTrain2Turns = 23
            if orangeTrain2Turns == 3:
                orangeTrain2X -= .25
            if orangeTrain2X == 329 and orangeTrain2Y == 270:
                orangeTrain2Turns = 4
            if orangeTrain2Turns == 4:
                if orangeTrain2Rotation == 1:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 2
                    orangeTrain2Turns = 5
            if orangeTrain2Turns == 5:
                orangeTrain2Y += .25
            if orangeTrain2X == 329 and orangeTrain2Y == 370:
                orangeTrain2Turns = 6
            if orangeTrain2Turns == 6:
                if orangeTrain2Rotation == 2:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 3
                    orangeTrain2Turns = 7
            if orangeTrain2Turns == 7:
                orangeTrain2X += .25

            #second track
            if orangeTrain2X == 470 and orangeTrain2Y == 370:
                if track2Visible == 1:
                    orangeTrain2Turns = 8
                else:
                    orangeTrain2Turns = 13

            #going to orange station
            if orangeTrain2Turns == 8:
                orangeTrain2X += .25
            if orangeTrain2X == 530 and orangeTrain2Y == 370:
                orangeTrain2Turns = 9
            if orangeTrain2Turns == 9:
                if orangeTrain2Rotation == 3:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 4
                    orangeTrain2Turns = 10
            if orangeTrain2Turns == 10:
                orangeTrain2Y -= .25
            if orangeTrain2X == 530 and orangeTrain2Y == 320:
                orangeTrain2Turns = 11
            if orangeTrain2Turns == 11:
                if orangeTrain2Rotation == 4:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 5
                    orangeTrain2Turns = 12
            if orangeTrain2Turns == 12:
                orangeTrain2X -= .25
            if orangeTrain2Turns == 13:
                if orangeTrain2Rotation == 3:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 6
                    orangeTrain2Turns = 14
            if orangeTrain2Turns == 14:
                orangeTrain2Y += .25
            if orangeTrain2Y == 432 and orangeTrain2X == 470:
                orangeTrain2Turns = 15
            if orangeTrain2Turns == 15:
                if orangeTrain2Rotation == 6:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 7
                    orangeTrain2Turns = 16
            if orangeTrain2Turns == 16:
                orangeTrain2X -= .25

            #Third track
            if orangeTrain2Y == 432 and orangeTrain2X == 255:
                if track3Visible == 1:
                    orangeTrain2Turns = 17
                else:
                    orangeTrain2Turns = 21

            #going to yellow station
            if orangeTrain2Turns == 17:
                orangeTrain2X -= .25
            if orangeTrain2Y == 432 and orangeTrain2X == 18:
                orangeTrain2Turns = 18
            if orangeTrain2Turns == 18:
                if orangeTrain2Rotation == 7:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 8
                    orangeTrain2Turns = 19
            if orangeTrain2Turns == 19:
                orangeTrain2Y -= .25
            if orangeTrain2Y == 335 and orangeTrain2X == 18:
                if orangeTrain2Rotation == 8:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 9
                    orangeTrain2Turns = 20
            if orangeTrain2Turns == 20:
                orangeTrain2X += .25

            #going to purple station
            if orangeTrain2Turns == 21:
                if orangeTrain2Rotation == 7:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 10
                    orangeTrain2Turns = 22
            if orangeTrain2Turns == 22:
                orangeTrain2Y -= .25

            if orangeTrain2Turns == 23:
                if orangeTrain2Rotation == 1:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 11
                    orangeTrain2Turns = 24
            if orangeTrain2Turns == 24:
                orangeTrain2Y -= .25

            #fourth track
            if orangeTrain2X == 493 and orangeTrain2Y == 178:
                if track4Visible == 1:
                    orangeTrain2Turns = 29
                else:
                    orangeTrain2Turns = 25

            #going to green station
            if orangeTrain2Turns == 25:
                if orangeTrain2Rotation == 11:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 12
                    orangeTrain2Turns = 26
            if orangeTrain2Turns == 26:
                orangeTrain2X -= .25
            if orangeTrain2X == 335 and orangeTrain2Y == 178:
                if orangeTrain2Rotation == 12:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 13
                    orangeTrain2Turns = 27
            if orangeTrain2Turns == 27:
                orangeTrain2Y -= .25
            if orangeTrain2X == 335 and orangeTrain2Y == 100:
                if orangeTrain2Rotation == 13:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 14
                    orangeTrain2Turns = 28
            if orangeTrain2Turns == 28:
                orangeTrain2X += .25

            if orangeTrain2Turns == 29:
                orangeTrain2Y -= .25
            if orangeTrain2X == 493 and orangeTrain2Y == 27:
                if orangeTrain2Rotation == 11:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 15
                    orangeTrain2Turns = 30
            if orangeTrain2Turns == 30:
                orangeTrain2X -= .25

            #fifth track
            if orangeTrain2X == 165 and orangeTrain2Y == 27:
                if track5Visible == 1:
                    orangeTrain2Turns = 31
                else:
                    orangeTrain2Turns = 32

            #going to red station
            if orangeTrain2Turns == 31:
                orangeTrain2X -= .25

            #going to blue station
            if orangeTrain2Turns == 32:
                if orangeTrain2Rotation == 15:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
                    orangeTrain2Rotation = 16
                    orangeTrain2Turns = 33
            if orangeTrain2Turns == 33:
                orangeTrain2Y += .25
            if orangeTrain2X == 165 and orangeTrain2Y == 257:
                if orangeTrain2Rotation == 16:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 17
                    orangeTrain2Turns = 34
            if orangeTrain2Turns == 34:
                orangeTrain2X -= .25
            if orangeTrain2X == 71 and orangeTrain2Y == 257:
                if orangeTrain2Rotation == 17:
                    orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
                    orangeTrain2Rotation = 18
                    orangeTrain2Turns = 35
            if orangeTrain2Turns == 35:
                orangeTrain2Y -= .25

        if orangeTrainNum3 == 1:
            screen.blit(orangeTrain3,[orangeTrain3X,orangeTrain3Y])
            if orangeTrain3Turns == 0:
                orangeTrain3Y -= .25
            if orangeTrain3Y == 270 and orangeTrain3X == 578:
                orangeTrain3Turns = 1
            if orangeTrain3Turns == 1:
                if orangeTrain3Rotation == 0:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 1
                    orangeTrain3Turns = 2
            if orangeTrain3Turns == 2:
                orangeTrain3X -= .25

            #first track
            if orangeTrain3Y == 270 and orangeTrain3X == 493:
                if track1Visible == 1:
                    orangeTrain3Turns = 3
                else:
                    orangeTrain3Turns = 23
            if orangeTrain3Turns == 3:
                orangeTrain3X -= .25
            if orangeTrain3X == 329 and orangeTrain3Y == 270:
                orangeTrain3Turns = 4
            if orangeTrain3Turns == 4:
                if orangeTrain3Rotation == 1:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 2
                    orangeTrain3Turns = 5
            if orangeTrain3Turns == 5:
                orangeTrain3Y += .25
            if orangeTrain3X == 329 and orangeTrain3Y == 370:
                orangeTrain3Turns = 6
            if orangeTrain3Turns == 6:
                if orangeTrain3Rotation == 2:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 3
                    orangeTrain3Turns = 7
            if orangeTrain3Turns == 7:
                orangeTrain3X += .25

            #second track
            if orangeTrain3X == 470 and orangeTrain3Y == 370:
                if track2Visible == 1:
                    orangeTrain3Turns = 8
                else:
                    orangeTrain3Turns = 13

            #going to orange station
            if orangeTrain3Turns == 8:
                orangeTrain3X += .25
            if orangeTrain3X == 530 and orangeTrain3Y == 370:
                orangeTrain3Turns = 9
            if orangeTrain3Turns == 9:
                if orangeTrain3Rotation == 3:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 4
                    orangeTrain3Turns = 10
            if orangeTrain3Turns == 10:
                orangeTrain3Y -= .25
            if orangeTrain3X == 530 and orangeTrain3Y == 320:
                orangeTrain3Turns = 11
            if orangeTrain3Turns == 11:
                if orangeTrain3Rotation == 4:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 5
                    orangeTrain3Turns = 12
            if orangeTrain3Turns == 12:
                orangeTrain3X -= .25
            if orangeTrain3Turns == 13:
                if orangeTrain3Rotation == 3:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 6
                    orangeTrain3Turns = 14
            if orangeTrain3Turns == 14:
                orangeTrain3Y += .25
            if orangeTrain3Y == 432 and orangeTrain3X == 470:
                orangeTrain3Turns = 15
            if orangeTrain3Turns == 15:
                if orangeTrain3Rotation == 6:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 7
                    orangeTrain3Turns = 16
            if orangeTrain3Turns == 16:
                orangeTrain3X -= .25

            #Third track
            if orangeTrain3Y == 432 and orangeTrain3X == 255:
                if track3Visible == 1:
                    orangeTrain3Turns = 17
                else:
                    orangeTrain3Turns = 21

            #going to yellow station
            if orangeTrain3Turns == 17:
                orangeTrain3X -= .25
            if orangeTrain3Y == 432 and orangeTrain3X == 18:
                orangeTrain3Turns = 18
            if orangeTrain3Turns == 18:
                if orangeTrain3Rotation == 7:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 8
                    orangeTrain3Turns = 19
            if orangeTrain3Turns == 19:
                orangeTrain3Y -= .25
            if orangeTrain3Y == 335 and orangeTrain3X == 18:
                if orangeTrain3Rotation == 8:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 9
                    orangeTrain3Turns = 20
            if orangeTrain3Turns == 20:
                orangeTrain3X += .25

            #going to purple station
            if orangeTrain3Turns == 21:
                if orangeTrain3Rotation == 7:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 10
                    orangeTrain3Turns = 22
            if orangeTrain3Turns == 22:
                orangeTrain3Y -= .25

            if orangeTrain3Turns == 23:
                if orangeTrain3Rotation == 1:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 11
                    orangeTrain3Turns = 24
            if orangeTrain3Turns == 24:
                orangeTrain3Y -= .25

            #fourth track
            if orangeTrain3X == 493 and orangeTrain3Y == 178:
                if track4Visible == 1:
                    orangeTrain3Turns = 29
                else:
                    orangeTrain3Turns = 25

            #going to green station
            if orangeTrain3Turns == 25:
                if orangeTrain3Rotation == 11:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 12
                    orangeTrain3Turns = 26
            if orangeTrain3Turns == 26:
                orangeTrain3X -= .25
            if orangeTrain3X == 335 and orangeTrain3Y == 178:
                if orangeTrain3Rotation == 12:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 13
                    orangeTrain3Turns = 27
            if orangeTrain3Turns == 27:
                orangeTrain3Y -= .25
            if orangeTrain3X == 335 and orangeTrain3Y == 100:
                if orangeTrain3Rotation == 13:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 14
                    orangeTrain3Turns = 28
            if orangeTrain3Turns == 28:
                orangeTrain3X += .25

            if orangeTrain3Turns == 29:
                orangeTrain3Y -= .25
            if orangeTrain3X == 493 and orangeTrain3Y == 27:
                if orangeTrain3Rotation == 11:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 15
                    orangeTrain3Turns = 30
            if orangeTrain3Turns == 30:
                orangeTrain3X -= .25

            #fifth track
            if orangeTrain3X == 165 and orangeTrain3Y == 27:
                if track5Visible == 1:
                    orangeTrain3Turns = 31
                else:
                    orangeTrain3Turns = 32

            #going to red station
            if orangeTrain3Turns == 31:
                orangeTrain3X -= .25

            #going to blue station
            if orangeTrain3Turns == 32:
                if orangeTrain3Rotation == 15:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
                    orangeTrain3Rotation = 16
                    orangeTrain3Turns = 33
            if orangeTrain3Turns == 33:
                orangeTrain3Y += .25
            if orangeTrain3X == 165 and orangeTrain3Y == 257:
                if orangeTrain3Rotation == 16:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 17
                    orangeTrain3Turns = 34
            if orangeTrain3Turns == 34:
                orangeTrain3X -= .25
            if orangeTrain3X == 71 and orangeTrain3Y == 257:
                if orangeTrain3Rotation == 17:
                    orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
                    orangeTrain3Rotation = 18
                    orangeTrain3Turns = 35
            if orangeTrain3Turns == 35:
                orangeTrain3Y -= .25


        if orangeTrainNum4 == 1:
            screen.blit(orangeTrain4,[orangeTrain4X,orangeTrain4Y])
            if orangeTrain4Turns == 0:
                orangeTrain4Y -= .25
            if orangeTrain4Y == 270 and orangeTrain4X == 578:
                orangeTrain4Turns = 1
            if orangeTrain4Turns == 1:
                if orangeTrain4Rotation == 0:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 1
                    orangeTrain4Turns = 2
            if orangeTrain4Turns == 2:
                orangeTrain4X -= .25

            #first track
            if orangeTrain4Y == 270 and orangeTrain4X == 493:
                if track1Visible == 1:
                    orangeTrain4Turns = 3
                else:
                    orangeTrain4Turns = 23
            if orangeTrain4Turns == 3:
                orangeTrain4X -= .25
            if orangeTrain4X == 329 and orangeTrain4Y == 270:
                orangeTrain4Turns = 4
            if orangeTrain4Turns == 4:
                if orangeTrain4Rotation == 1:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 2
                    orangeTrain4Turns = 5
            if orangeTrain4Turns == 5:
                orangeTrain4Y += .25
            if orangeTrain4X == 329 and orangeTrain4Y == 370:
                orangeTrain4Turns = 6
            if orangeTrain4Turns == 6:
                if orangeTrain4Rotation == 2:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 3
                    orangeTrain4Turns = 7
            if orangeTrain4Turns == 7:
                orangeTrain4X += .25

            #second track
            if orangeTrain4X == 470 and orangeTrain4Y == 370:
                if track2Visible == 1:
                    orangeTrain4Turns = 8
                else:
                    orangeTrain4Turns = 13

            #going to orange station
            if orangeTrain4Turns == 8:
                orangeTrain4X += .25
            if orangeTrain4X == 530 and orangeTrain4Y == 370:
                orangeTrain4Turns = 9
            if orangeTrain4Turns == 9:
                if orangeTrain4Rotation == 3:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 4
                    orangeTrain4Turns = 10
            if orangeTrain4Turns == 10:
                orangeTrain4Y -= .25
            if orangeTrain4X == 530 and orangeTrain4Y == 320:
                orangeTrain4Turns = 11
            if orangeTrain4Turns == 11:
                if orangeTrain4Rotation == 4:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 5
                    orangeTrain4Turns = 12
            if orangeTrain4Turns == 12:
                orangeTrain4X -= .25
            if orangeTrain4Turns == 13:
                if orangeTrain4Rotation == 3:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 6
                    orangeTrain4Turns = 14
            if orangeTrain4Turns == 14:
                orangeTrain4Y += .25
            if orangeTrain4Y == 432 and orangeTrain4X == 470:
                orangeTrain4Turns = 15
            if orangeTrain4Turns == 15:
                if orangeTrain4Rotation == 6:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 7
                    orangeTrain4Turns = 16
            if orangeTrain4Turns == 16:
                orangeTrain4X -= .25

            #Third track
            if orangeTrain4Y == 432 and orangeTrain4X == 255:
                if track3Visible == 1:
                    orangeTrain4Turns = 17
                else:
                    orangeTrain4Turns = 21

            #going to yellow station
            if orangeTrain4Turns == 17:
                orangeTrain4X -= .25
            if orangeTrain4Y == 432 and orangeTrain4X == 18:
                orangeTrain4Turns = 18
            if orangeTrain4Turns == 18:
                if orangeTrain4Rotation == 7:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 8
                    orangeTrain4Turns = 19
            if orangeTrain4Turns == 19:
                orangeTrain4Y -= .25
            if orangeTrain4Y == 335 and orangeTrain4X == 18:
                if orangeTrain4Rotation == 8:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 9
                    orangeTrain4Turns = 20
            if orangeTrain4Turns == 20:
                orangeTrain4X += .25

            #going to purple station
            if orangeTrain4Turns == 21:
                if orangeTrain4Rotation == 7:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 10
                    orangeTrain4Turns = 22
            if orangeTrain4Turns == 22:
                orangeTrain4Y -= .25

            if orangeTrain4Turns == 23:
                if orangeTrain4Rotation == 1:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 11
                    orangeTrain4Turns = 24
            if orangeTrain4Turns == 24:
                orangeTrain4Y -= .25

            #fourth track
            if orangeTrain4X == 493 and orangeTrain4Y == 178:
                if track4Visible == 1:
                    orangeTrain4Turns = 29
                else:
                    orangeTrain4Turns = 25

            #going to green station
            if orangeTrain4Turns == 25:
                if orangeTrain4Rotation == 11:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 12
                    orangeTrain4Turns = 26
            if orangeTrain4Turns == 26:
                orangeTrain4X -= .25
            if orangeTrain4X == 335 and orangeTrain4Y == 178:
                if orangeTrain4Rotation == 12:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 13
                    orangeTrain4Turns = 27
            if orangeTrain4Turns == 27:
                orangeTrain4Y -= .25
            if orangeTrain4X == 335 and orangeTrain4Y == 100:
                if orangeTrain4Rotation == 13:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 14
                    orangeTrain4Turns = 28
            if orangeTrain4Turns == 28:
                orangeTrain4X += .25

            if orangeTrain4Turns == 29:
                orangeTrain4Y -= .25
            if orangeTrain4X == 493 and orangeTrain4Y == 27:
                if orangeTrain4Rotation == 11:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 15
                    orangeTrain4Turns = 30
            if orangeTrain4Turns == 30:
                orangeTrain4X -= .25

            #fifth track
            if orangeTrain4X == 165 and orangeTrain4Y == 27:
                if track5Visible == 1:
                    orangeTrain4Turns = 31
                else:
                    orangeTrain4Turns = 32

            #going to red station
            if orangeTrain4Turns == 31:
                orangeTrain4X -= .25

            #going to blue station
            if orangeTrain4Turns == 32:
                if orangeTrain4Rotation == 15:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
                    orangeTrain4Rotation = 16
                    orangeTrain4Turns = 33
            if orangeTrain4Turns == 33:
                orangeTrain4Y += .25
            if orangeTrain4X == 165 and orangeTrain4Y == 257:
                if orangeTrain4Rotation == 16:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 17
                    orangeTrain4Turns = 34
            if orangeTrain4Turns == 34:
                orangeTrain4X -= .25
            if orangeTrain4X == 71 and orangeTrain4Y == 257:
                if orangeTrain4Rotation == 17:
                    orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
                    orangeTrain4Rotation = 18
                    orangeTrain4Turns = 35
            if orangeTrain4Turns == 35:
                orangeTrain4Y -= .25


        if yellowTrainNum0 == 1:
            screen.blit(yellowTrain,[yellowTrainX,yellowTrainY])
            if yellowTrainTurns == 0:
                yellowTrainY -= .25
            if yellowTrainY == 270 and yellowTrainX == 578:
                yellowTrainTurns = 1
            if yellowTrainTurns == 1:
                if yellowTrainRotation == 0:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 1
                    yellowTrainTurns = 2
            if yellowTrainTurns == 2:
                yellowTrainX -= .25

            #first track
            if yellowTrainY == 270 and yellowTrainX == 493:
                if track1Visible == 1:
                    yellowTrainTurns = 3
                else:
                    yellowTrainTurns = 23
            if yellowTrainTurns == 3:
                yellowTrainX -= .25
            if yellowTrainX == 329 and yellowTrainY == 270:
                yellowTrainTurns = 4
            if yellowTrainTurns == 4:
                if yellowTrainRotation == 1:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 2
                    yellowTrainTurns = 5
            if yellowTrainTurns == 5:
                yellowTrainY += .25
            if yellowTrainX == 329 and yellowTrainY == 370:
                yellowTrainTurns = 6
            if yellowTrainTurns == 6:
                if yellowTrainRotation == 2:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 3
                    yellowTrainTurns = 7
            if yellowTrainTurns == 7:
                yellowTrainX += .25

            #second track
            if yellowTrainX == 470 and yellowTrainY == 370:
                if track2Visible == 1:
                    yellowTrainTurns = 8
                else:
                    yellowTrainTurns = 13

            #going to orange station
            if yellowTrainTurns == 8:
                yellowTrainX += .25
            if yellowTrainX == 530 and yellowTrainY == 370:
                yellowTrainTurns = 9
            if yellowTrainTurns == 9:
                if yellowTrainRotation == 3:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 4
                    yellowTrainTurns = 10
            if yellowTrainTurns == 10:
                yellowTrainY -= .25
            if yellowTrainX == 530 and yellowTrainY == 320:
                yellowTrainTurns = 11
            if yellowTrainTurns == 11:
                if yellowTrainRotation == 4:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 5
                    yellowTrainTurns = 12
            if yellowTrainTurns == 12:
                yellowTrainX -= .25
            if yellowTrainTurns == 13:
                if yellowTrainRotation == 3:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 6
                    yellowTrainTurns = 14
            if yellowTrainTurns == 14:
                yellowTrainY += .25
            if yellowTrainY == 432 and yellowTrainX == 470:
                yellowTrainTurns = 15
            if yellowTrainTurns == 15:
                if yellowTrainRotation == 6:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 7
                    yellowTrainTurns = 16
            if yellowTrainTurns == 16:
                yellowTrainX -= .25

            #Third track
            if yellowTrainY == 432 and yellowTrainX == 255:
                if track3Visible == 1:
                    yellowTrainTurns = 17
                else:
                    yellowTrainTurns = 21

            #going to yellow station
            if yellowTrainTurns == 17:
                yellowTrainX -= .25
            if yellowTrainY == 432 and yellowTrainX == 18:
                yellowTrainTurns = 18
            if yellowTrainTurns == 18:
                if yellowTrainRotation == 7:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 8
                    yellowTrainTurns = 19
            if yellowTrainTurns == 19:
                yellowTrainY -= .25
            if yellowTrainY == 335 and yellowTrainX == 18:
                if yellowTrainRotation == 8:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 9
                    yellowTrainTurns = 20
            if yellowTrainTurns == 20:
                yellowTrainX += .25

            #going to purple station
            if yellowTrainTurns == 21:
                if yellowTrainRotation == 7:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 10
                    yellowTrainTurns = 22
            if yellowTrainTurns == 22:
                yellowTrainY -= .25

            if yellowTrainTurns == 23:
                if yellowTrainRotation == 1:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 11
                    yellowTrainTurns = 24
            if yellowTrainTurns == 24:
                yellowTrainY -= .25

            #fourth track
            if yellowTrainX == 493 and yellowTrainY == 178:
                if track4Visible == 1:
                    yellowTrainTurns = 29
                else:
                    yellowTrainTurns = 25

            #going to green station
            if yellowTrainTurns == 25:
                if yellowTrainRotation == 11:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 12
                    yellowTrainTurns = 26
            if yellowTrainTurns == 26:
                yellowTrainX -= .25
            if yellowTrainX == 335 and yellowTrainY == 178:
                if yellowTrainRotation == 12:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 13
                    yellowTrainTurns = 27
            if yellowTrainTurns == 27:
                yellowTrainY -= .25
            if yellowTrainX == 335 and yellowTrainY == 100:
                if yellowTrainRotation == 13:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 14
                    yellowTrainTurns = 28
            if yellowTrainTurns == 28:
                yellowTrainX += .25

            if yellowTrainTurns == 29:
                yellowTrainY -= .25
            if yellowTrainX == 493 and yellowTrainY == 27:
                if yellowTrainRotation == 11:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 15
                    yellowTrainTurns = 30
            if yellowTrainTurns == 30:
                yellowTrainX -= .25

            #fifth track
            if yellowTrainX == 165 and yellowTrainY == 27:
                if track5Visible == 1:
                    yellowTrainTurns = 31
                else:
                    yellowTrainTurns = 32

            #going to red station
            if yellowTrainTurns == 31:
                yellowTrainX -= .25

            #going to blue station
            if yellowTrainTurns == 32:
                if yellowTrainRotation == 15:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 90)
                    yellowTrainRotation = 16
                    yellowTrainTurns = 33
            if yellowTrainTurns == 33:
                yellowTrainY += .25
            if yellowTrainX == 165 and yellowTrainY == 257:
                if yellowTrainRotation == 16:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 17
                    yellowTrainTurns = 34
            if yellowTrainTurns == 34:
                yellowTrainX -= .25
            if yellowTrainX == 71 and yellowTrainY == 257:
                if yellowTrainRotation == 17:
                    yellowTrain = pygame.transform.rotate(yellowTrain, 270)
                    yellowTrainRotation = 18
                    yellowTrainTurns = 35
            if yellowTrainTurns == 35:
                yellowTrainY -= .25

        if yellowTrainNum1 == 1:
            screen.blit(yellowTrain1,[yellowTrain1X,yellowTrain1Y])
            if yellowTrain1Turns == 0:
                yellowTrain1Y -= .25
            if yellowTrain1Y == 270 and yellowTrain1X == 578:
                yellowTrain1Turns = 1
            if yellowTrain1Turns == 1:
                if yellowTrain1Rotation == 0:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 1
                    yellowTrain1Turns = 2
            if yellowTrain1Turns == 2:
                yellowTrain1X -= .25

            #first track
            if yellowTrain1Y == 270 and yellowTrain1X == 493:
                if track1Visible == 1:
                    yellowTrain1Turns = 3
                else:
                    yellowTrain1Turns = 23
            if yellowTrain1Turns == 3:
                yellowTrain1X -= .25
            if yellowTrain1X == 329 and yellowTrain1Y == 270:
                yellowTrain1Turns = 4
            if yellowTrain1Turns == 4:
                if yellowTrain1Rotation == 1:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 2
                    yellowTrain1Turns = 5
            if yellowTrain1Turns == 5:
                yellowTrain1Y += .25
            if yellowTrain1X == 329 and yellowTrain1Y == 370:
                yellowTrain1Turns = 6
            if yellowTrain1Turns == 6:
                if yellowTrain1Rotation == 2:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 3
                    yellowTrain1Turns = 7
            if yellowTrain1Turns == 7:
                yellowTrain1X += .25

            #second track
            if yellowTrain1X == 470 and yellowTrain1Y == 370:
                if track2Visible == 1:
                    yellowTrain1Turns = 8
                else:
                    yellowTrain1Turns = 13

            #going to orange station
            if yellowTrain1Turns == 8:
                yellowTrain1X += .25
            if yellowTrain1X == 530 and yellowTrain1Y == 370:
                yellowTrain1Turns = 9
            if yellowTrain1Turns == 9:
                if yellowTrain1Rotation == 3:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 4
                    yellowTrain1Turns = 10
            if yellowTrain1Turns == 10:
                yellowTrain1Y -= .25
            if yellowTrain1X == 530 and yellowTrain1Y == 320:
                yellowTrain1Turns = 11
            if yellowTrain1Turns == 11:
                if yellowTrain1Rotation == 4:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 5
                    yellowTrain1Turns = 12
            if yellowTrain1Turns == 12:
                yellowTrain1X -= .25
            if yellowTrain1Turns == 13:
                if yellowTrain1Rotation == 3:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 6
                    yellowTrain1Turns = 14
            if yellowTrain1Turns == 14:
                yellowTrain1Y += .25
            if yellowTrain1Y == 432 and yellowTrain1X == 470:
                yellowTrain1Turns = 15
            if yellowTrain1Turns == 15:
                if yellowTrain1Rotation == 6:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 7
                    yellowTrain1Turns = 16
            if yellowTrain1Turns == 16:
                yellowTrain1X -= .25

            #Third track
            if yellowTrain1Y == 432 and yellowTrain1X == 255:
                if track3Visible == 1:
                    yellowTrain1Turns = 17
                else:
                    yellowTrain1Turns = 21

            #going to yellow station
            if yellowTrain1Turns == 17:
                yellowTrain1X -= .25
            if yellowTrain1Y == 432 and yellowTrain1X == 18:
                yellowTrain1Turns = 18
            if yellowTrain1Turns == 18:
                if yellowTrain1Rotation == 7:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 8
                    yellowTrain1Turns = 19
            if yellowTrain1Turns == 19:
                yellowTrain1Y -= .25
            if yellowTrain1Y == 335 and yellowTrain1X == 18:
                if yellowTrain1Rotation == 8:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 9
                    yellowTrain1Turns = 20
            if yellowTrain1Turns == 20:
                yellowTrain1X += .25

            #going to purple station
            if yellowTrain1Turns == 21:
                if yellowTrain1Rotation == 7:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 10
                    yellowTrain1Turns = 22
            if yellowTrain1Turns == 22:
                yellowTrain1Y -= .25

            if yellowTrain1Turns == 23:
                if yellowTrain1Rotation == 1:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 11
                    yellowTrain1Turns = 24
            if yellowTrain1Turns == 24:
                yellowTrain1Y -= .25

            #fourth track
            if yellowTrain1X == 493 and yellowTrain1Y == 178:
                if track4Visible == 1:
                    yellowTrain1Turns = 29
                else:
                    yellowTrain1Turns = 25

            #going to green station
            if yellowTrain1Turns == 25:
                if yellowTrain1Rotation == 11:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 12
                    yellowTrain1Turns = 26
            if yellowTrain1Turns == 26:
                yellowTrain1X -= .25
            if yellowTrain1X == 335 and yellowTrain1Y == 178:
                if yellowTrain1Rotation == 12:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 13
                    yellowTrain1Turns = 27
            if yellowTrain1Turns == 27:
                yellowTrain1Y -= .25
            if yellowTrain1X == 335 and yellowTrain1Y == 100:
                if yellowTrain1Rotation == 13:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 14
                    yellowTrain1Turns = 28
            if yellowTrain1Turns == 28:
                yellowTrain1X += .25

            if yellowTrain1Turns == 29:
                yellowTrain1Y -= .25
            if yellowTrain1X == 493 and yellowTrain1Y == 27:
                if yellowTrain1Rotation == 11:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 15
                    yellowTrain1Turns = 30
            if yellowTrain1Turns == 30:
                yellowTrain1X -= .25

            #fifth track
            if yellowTrain1X == 165 and yellowTrain1Y == 27:
                if track5Visible == 1:
                    yellowTrain1Turns = 31
                else:
                    yellowTrain1Turns = 32

            #going to red station
            if yellowTrain1Turns == 31:
                yellowTrain1X -= .25

            #going to blue station
            if yellowTrain1Turns == 32:
                if yellowTrain1Rotation == 15:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
                    yellowTrain1Rotation = 16
                    yellowTrain1Turns = 33
            if yellowTrain1Turns == 33:
                yellowTrain1Y += .25
            if yellowTrain1X == 165 and yellowTrain1Y == 257:
                if yellowTrain1Rotation == 16:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 17
                    yellowTrain1Turns = 34
            if yellowTrain1Turns == 34:
                yellowTrain1X -= .25
            if yellowTrain1X == 71 and yellowTrain1Y == 257:
                if yellowTrain1Rotation == 17:
                    yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
                    yellowTrain1Rotation = 18
                    yellowTrain1Turns = 35
            if yellowTrain1Turns == 35:
                yellowTrain1Y -= .25


        if yellowTrainNum2 == 1:
            screen.blit(yellowTrain2,[yellowTrain2X,yellowTrain2Y])
            if yellowTrain2Turns == 0:
                yellowTrain2Y -= .25
            if yellowTrain2Y == 270 and yellowTrain2X == 578:
                yellowTrain2Turns = 1
            if yellowTrain2Turns == 1:
                if yellowTrain2Rotation == 0:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 1
                    yellowTrain2Turns = 2
            if yellowTrain2Turns == 2:
                yellowTrain2X -= .25

            #first track
            if yellowTrain2Y == 270 and yellowTrain2X == 493:
                if track1Visible == 1:
                    yellowTrain2Turns = 3
                else:
                    yellowTrain2Turns = 23
            if yellowTrain2Turns == 3:
                yellowTrain2X -= .25
            if yellowTrain2X == 329 and yellowTrain2Y == 270:
                yellowTrain2Turns = 4
            if yellowTrain2Turns == 4:
                if yellowTrain2Rotation == 1:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 2
                    yellowTrain2Turns = 5
            if yellowTrain2Turns == 5:
                yellowTrain2Y += .25
            if yellowTrain2X == 329 and yellowTrain2Y == 370:
                yellowTrain2Turns = 6
            if yellowTrain2Turns == 6:
                if yellowTrain2Rotation == 2:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 3
                    yellowTrain2Turns = 7
            if yellowTrain2Turns == 7:
                yellowTrain2X += .25

            #second track
            if yellowTrain2X == 470 and yellowTrain2Y == 370:
                if track2Visible == 1:
                    yellowTrain2Turns = 8
                else:
                    yellowTrain2Turns = 13

            #going to orange station
            if yellowTrain2Turns == 8:
                yellowTrain2X += .25
            if yellowTrain2X == 530 and yellowTrain2Y == 370:
                yellowTrain2Turns = 9
            if yellowTrain2Turns == 9:
                if yellowTrain2Rotation == 3:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 4
                    yellowTrain2Turns = 10
            if yellowTrain2Turns == 10:
                yellowTrain2Y -= .25
            if yellowTrain2X == 530 and yellowTrain2Y == 320:
                yellowTrain2Turns = 11
            if yellowTrain2Turns == 11:
                if yellowTrain2Rotation == 4:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 5
                    yellowTrain2Turns = 12
            if yellowTrain2Turns == 12:
                yellowTrain2X -= .25
            if yellowTrain2Turns == 13:
                if yellowTrain2Rotation == 3:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 6
                    yellowTrain2Turns = 14
            if yellowTrain2Turns == 14:
                yellowTrain2Y += .25
            if yellowTrain2Y == 432 and yellowTrain2X == 470:
                yellowTrain2Turns = 15
            if yellowTrain2Turns == 15:
                if yellowTrain2Rotation == 6:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 7
                    yellowTrain2Turns = 16
            if yellowTrain2Turns == 16:
                yellowTrain2X -= .25

            #Third track
            if yellowTrain2Y == 432 and yellowTrain2X == 255:
                if track3Visible == 1:
                    yellowTrain2Turns = 17
                else:
                    yellowTrain2Turns = 21

            #going to yellow station
            if yellowTrain2Turns == 17:
                yellowTrain2X -= .25
            if yellowTrain2Y == 432 and yellowTrain2X == 18:
                yellowTrain2Turns = 18
            if yellowTrain2Turns == 18:
                if yellowTrain2Rotation == 7:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 8
                    yellowTrain2Turns = 19
            if yellowTrain2Turns == 19:
                yellowTrain2Y -= .25
            if yellowTrain2Y == 335 and yellowTrain2X == 18:
                if yellowTrain2Rotation == 8:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 9
                    yellowTrain2Turns = 20
            if yellowTrain2Turns == 20:
                yellowTrain2X += .25

            #going to purple station
            if yellowTrain2Turns == 21:
                if yellowTrain2Rotation == 7:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 10
                    yellowTrain2Turns = 22
            if yellowTrain2Turns == 22:
                yellowTrain2Y -= .25

            if yellowTrain2Turns == 23:
                if yellowTrain2Rotation == 1:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 11
                    yellowTrain2Turns = 24
            if yellowTrain2Turns == 24:
                yellowTrain2Y -= .25

            #fourth track
            if yellowTrain2X == 493 and yellowTrain2Y == 178:
                if track4Visible == 1:
                    yellowTrain2Turns = 29
                else:
                    yellowTrain2Turns = 25

            #going to green station
            if yellowTrain2Turns == 25:
                if yellowTrain2Rotation == 11:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 12
                    yellowTrain2Turns = 26
            if yellowTrain2Turns == 26:
                yellowTrain2X -= .25
            if yellowTrain2X == 335 and yellowTrain2Y == 178:
                if yellowTrain2Rotation == 12:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 13
                    yellowTrain2Turns = 27
            if yellowTrain2Turns == 27:
                yellowTrain2Y -= .25
            if yellowTrain2X == 335 and yellowTrain2Y == 100:
                if yellowTrain2Rotation == 13:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 14
                    yellowTrain2Turns = 28
            if yellowTrain2Turns == 28:
                yellowTrain2X += .25

            if yellowTrain2Turns == 29:
                yellowTrain2Y -= .25
            if yellowTrain2X == 493 and yellowTrain2Y == 27:
                if yellowTrain2Rotation == 11:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 15
                    yellowTrain2Turns = 30
            if yellowTrain2Turns == 30:
                yellowTrain2X -= .25

            #fifth track
            if yellowTrain2X == 165 and yellowTrain2Y == 27:
                if track5Visible == 1:
                    yellowTrain2Turns = 31
                else:
                    yellowTrain2Turns = 32

            #going to red station
            if yellowTrain2Turns == 31:
                yellowTrain2X -= .25

            #going to blue station
            if yellowTrain2Turns == 32:
                if yellowTrain2Rotation == 15:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
                    yellowTrain2Rotation = 16
                    yellowTrain2Turns = 33
            if yellowTrain2Turns == 33:
                yellowTrain2Y += .25
            if yellowTrain2X == 165 and yellowTrain2Y == 257:
                if yellowTrain2Rotation == 16:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 17
                    yellowTrain2Turns = 34
            if yellowTrain2Turns == 34:
                yellowTrain2X -= .25
            if yellowTrain2X == 71 and yellowTrain2Y == 257:
                if yellowTrain2Rotation == 17:
                    yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
                    yellowTrain2Rotation = 18
                    yellowTrain2Turns = 35
            if yellowTrain2Turns == 35:
                yellowTrain2Y -= .25

        if yellowTrainNum3 == 1:
            screen.blit(yellowTrain3,[yellowTrain3X,yellowTrain3Y])
            if yellowTrain3Turns == 0:
                yellowTrain3Y -= .25
            if yellowTrain3Y == 270 and yellowTrain3X == 578:
                yellowTrain3Turns = 1
            if yellowTrain3Turns == 1:
                if yellowTrain3Rotation == 0:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 1
                    yellowTrain3Turns = 2
            if yellowTrain3Turns == 2:
                yellowTrain3X -= .25

            #first track
            if yellowTrain3Y == 270 and yellowTrain3X == 493:
                if track1Visible == 1:
                    yellowTrain3Turns = 3
                else:
                    yellowTrain3Turns = 23
            if yellowTrain3Turns == 3:
                yellowTrain3X -= .25
            if yellowTrain3X == 329 and yellowTrain3Y == 270:
                yellowTrain3Turns = 4
            if yellowTrain3Turns == 4:
                if yellowTrain3Rotation == 1:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 2
                    yellowTrain3Turns = 5
            if yellowTrain3Turns == 5:
                yellowTrain3Y += .25
            if yellowTrain3X == 329 and yellowTrain3Y == 370:
                yellowTrain3Turns = 6
            if yellowTrain3Turns == 6:
                if yellowTrain3Rotation == 2:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 3
                    yellowTrain3Turns = 7
            if yellowTrain3Turns == 7:
                yellowTrain3X += .25

            #second track
            if yellowTrain3X == 470 and yellowTrain3Y == 370:
                if track2Visible == 1:
                    yellowTrain3Turns = 8
                else:
                    yellowTrain3Turns = 13

            #going to orange station
            if yellowTrain3Turns == 8:
                yellowTrain3X += .25
            if yellowTrain3X == 530 and yellowTrain3Y == 370:
                yellowTrain3Turns = 9
            if yellowTrain3Turns == 9:
                if yellowTrain3Rotation == 3:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 4
                    yellowTrain3Turns = 10
            if yellowTrain3Turns == 10:
                yellowTrain3Y -= .25
            if yellowTrain3X == 530 and yellowTrain3Y == 320:
                yellowTrain3Turns = 11
            if yellowTrain3Turns == 11:
                if yellowTrain3Rotation == 4:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 5
                    yellowTrain3Turns = 12
            if yellowTrain3Turns == 12:
                yellowTrain3X -= .25
            if yellowTrain3Turns == 13:
                if yellowTrain3Rotation == 3:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 6
                    yellowTrain3Turns = 14
            if yellowTrain3Turns == 14:
                yellowTrain3Y += .25
            if yellowTrain3Y == 432 and yellowTrain3X == 470:
                yellowTrain3Turns = 15
            if yellowTrain3Turns == 15:
                if yellowTrain3Rotation == 6:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 7
                    yellowTrain3Turns = 16
            if yellowTrain3Turns == 16:
                yellowTrain3X -= .25

            #Third track
            if yellowTrain3Y == 432 and yellowTrain3X == 255:
                if track3Visible == 1:
                    yellowTrain3Turns = 17
                else:
                    yellowTrain3Turns = 21

            #going to yellow station
            if yellowTrain3Turns == 17:
                yellowTrain3X -= .25
            if yellowTrain3Y == 432 and yellowTrain3X == 18:
                yellowTrain3Turns = 18
            if yellowTrain3Turns == 18:
                if yellowTrain3Rotation == 7:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 8
                    yellowTrain3Turns = 19
            if yellowTrain3Turns == 19:
                yellowTrain3Y -= .25
            if yellowTrain3Y == 335 and yellowTrain3X == 18:
                if yellowTrain3Rotation == 8:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 9
                    yellowTrain3Turns = 20
            if yellowTrain3Turns == 20:
                yellowTrain3X += .25

            #going to purple station
            if yellowTrain3Turns == 21:
                if yellowTrain3Rotation == 7:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 10
                    yellowTrain3Turns = 22
            if yellowTrain3Turns == 22:
                yellowTrain3Y -= .25

            if yellowTrain3Turns == 23:
                if yellowTrain3Rotation == 1:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 11
                    yellowTrain3Turns = 24
            if yellowTrain3Turns == 24:
                yellowTrain3Y -= .25

            #fourth track
            if yellowTrain3X == 493 and yellowTrain3Y == 178:
                if track4Visible == 1:
                    yellowTrain3Turns = 29
                else:
                    yellowTrain3Turns = 25

            #going to green station
            if yellowTrain3Turns == 25:
                if yellowTrain3Rotation == 11:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 12
                    yellowTrain3Turns = 26
            if yellowTrain3Turns == 26:
                yellowTrain3X -= .25
            if yellowTrain3X == 335 and yellowTrain3Y == 178:
                if yellowTrain3Rotation == 12:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 13
                    yellowTrain3Turns = 27
            if yellowTrain3Turns == 27:
                yellowTrain3Y -= .25
            if yellowTrain3X == 335 and yellowTrain3Y == 100:
                if yellowTrain3Rotation == 13:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 14
                    yellowTrain3Turns = 28
            if yellowTrain3Turns == 28:
                yellowTrain3X += .25

            if yellowTrain3Turns == 29:
                yellowTrain3Y -= .25
            if yellowTrain3X == 493 and yellowTrain3Y == 27:
                if yellowTrain3Rotation == 11:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 15
                    yellowTrain3Turns = 30
            if yellowTrain3Turns == 30:
                yellowTrain3X -= .25

            #fifth track
            if yellowTrain3X == 165 and yellowTrain3Y == 27:
                if track5Visible == 1:
                    yellowTrain3Turns = 31
                else:
                    yellowTrain3Turns = 32

            #going to red station
            if yellowTrain3Turns == 31:
                yellowTrain3X -= .25

            #going to blue station
            if yellowTrain3Turns == 32:
                if yellowTrain3Rotation == 15:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
                    yellowTrain3Rotation = 16
                    yellowTrain3Turns = 33
            if yellowTrain3Turns == 33:
                yellowTrain3Y += .25
            if yellowTrain3X == 165 and yellowTrain3Y == 257:
                if yellowTrain3Rotation == 16:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 17
                    yellowTrain3Turns = 34
            if yellowTrain3Turns == 34:
                yellowTrain3X -= .25
            if yellowTrain3X == 71 and yellowTrain3Y == 257:
                if yellowTrain3Rotation == 17:
                    yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
                    yellowTrain3Rotation = 18
                    yellowTrain3Turns = 35
            if yellowTrain3Turns == 35:
                yellowTrain3Y -= .25


        if yellowTrainNum4 == 1:
            screen.blit(yellowTrain4,[yellowTrain4X,yellowTrain4Y])
            if yellowTrain4Turns == 0:
                yellowTrain4Y -= .25
            if yellowTrain4Y == 270 and yellowTrain4X == 578:
                yellowTrain4Turns = 1
            if yellowTrain4Turns == 1:
                if yellowTrain4Rotation == 0:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 1
                    yellowTrain4Turns = 2
            if yellowTrain4Turns == 2:
                yellowTrain4X -= .25

            #first track
            if yellowTrain4Y == 270 and yellowTrain4X == 493:
                if track1Visible == 1:
                    yellowTrain4Turns = 3
                else:
                    yellowTrain4Turns = 23
            if yellowTrain4Turns == 3:
                yellowTrain4X -= .25
            if yellowTrain4X == 329 and yellowTrain4Y == 270:
                yellowTrain4Turns = 4
            if yellowTrain4Turns == 4:
                if yellowTrain4Rotation == 1:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 2
                    yellowTrain4Turns = 5
            if yellowTrain4Turns == 5:
                yellowTrain4Y += .25
            if yellowTrain4X == 329 and yellowTrain4Y == 370:
                yellowTrain4Turns = 6
            if yellowTrain4Turns == 6:
                if yellowTrain4Rotation == 2:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 3
                    yellowTrain4Turns = 7
            if yellowTrain4Turns == 7:
                yellowTrain4X += .25

            #second track
            if yellowTrain4X == 470 and yellowTrain4Y == 370:
                if track2Visible == 1:
                    yellowTrain4Turns = 8
                else:
                    yellowTrain4Turns = 13

            #going to orange station
            if yellowTrain4Turns == 8:
                yellowTrain4X += .25
            if yellowTrain4X == 530 and yellowTrain4Y == 370:
                yellowTrain4Turns = 9
            if yellowTrain4Turns == 9:
                if yellowTrain4Rotation == 3:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 4
                    yellowTrain4Turns = 10
            if yellowTrain4Turns == 10:
                yellowTrain4Y -= .25
            if yellowTrain4X == 530 and yellowTrain4Y == 320:
                yellowTrain4Turns = 11
            if yellowTrain4Turns == 11:
                if yellowTrain4Rotation == 4:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 5
                    yellowTrain4Turns = 12
            if yellowTrain4Turns == 12:
                yellowTrain4X -= .25
            if yellowTrain4Turns == 13:
                if yellowTrain4Rotation == 3:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 6
                    yellowTrain4Turns = 14
            if yellowTrain4Turns == 14:
                yellowTrain4Y += .25
            if yellowTrain4Y == 432 and yellowTrain4X == 470:
                yellowTrain4Turns = 15
            if yellowTrain4Turns == 15:
                if yellowTrain4Rotation == 6:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 7
                    yellowTrain4Turns = 16
            if yellowTrain4Turns == 16:
                yellowTrain4X -= .25

            #Third track
            if yellowTrain4Y == 432 and yellowTrain4X == 255:
                if track3Visible == 1:
                    yellowTrain4Turns = 17
                else:
                    yellowTrain4Turns = 21

            #going to yellow station
            if yellowTrain4Turns == 17:
                yellowTrain4X -= .25
            if yellowTrain4Y == 432 and yellowTrain4X == 18:
                yellowTrain4Turns = 18
            if yellowTrain4Turns == 18:
                if yellowTrain4Rotation == 7:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 8
                    yellowTrain4Turns = 19
            if yellowTrain4Turns == 19:
                yellowTrain4Y -= .25
            if yellowTrain4Y == 335 and yellowTrain4X == 18:
                if yellowTrain4Rotation == 8:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 9
                    yellowTrain4Turns = 20
            if yellowTrain4Turns == 20:
                yellowTrain4X += .25

            #going to purple station
            if yellowTrain4Turns == 21:
                if yellowTrain4Rotation == 7:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 10
                    yellowTrain4Turns = 22
            if yellowTrain4Turns == 22:
                yellowTrain4Y -= .25

            if yellowTrain4Turns == 23:
                if yellowTrain4Rotation == 1:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 11
                    yellowTrain4Turns = 24
            if yellowTrain4Turns == 24:
                yellowTrain4Y -= .25

            #fourth track
            if yellowTrain4X == 493 and yellowTrain4Y == 178:
                if track4Visible == 1:
                    yellowTrain4Turns = 29
                else:
                    yellowTrain4Turns = 25

            #going to green station
            if yellowTrain4Turns == 25:
                if yellowTrain4Rotation == 11:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 12
                    yellowTrain4Turns = 26
            if yellowTrain4Turns == 26:
                yellowTrain4X -= .25
            if yellowTrain4X == 335 and yellowTrain4Y == 178:
                if yellowTrain4Rotation == 12:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 13
                    yellowTrain4Turns = 27
            if yellowTrain4Turns == 27:
                yellowTrain4Y -= .25
            if yellowTrain4X == 335 and yellowTrain4Y == 100:
                if yellowTrain4Rotation == 13:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 14
                    yellowTrain4Turns = 28
            if yellowTrain4Turns == 28:
                yellowTrain4X += .25

            if yellowTrain4Turns == 29:
                yellowTrain4Y -= .25
            if yellowTrain4X == 493 and yellowTrain4Y == 27:
                if yellowTrain4Rotation == 11:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 15
                    yellowTrain4Turns = 30
            if yellowTrain4Turns == 30:
                yellowTrain4X -= .25

            #fifth track
            if yellowTrain4X == 165 and yellowTrain4Y == 27:
                if track5Visible == 1:
                    yellowTrain4Turns = 31
                else:
                    yellowTrain4Turns = 32

            #going to red station
            if yellowTrain4Turns == 31:
                yellowTrain4X -= .25

            #going to blue station
            if yellowTrain4Turns == 32:
                if yellowTrain4Rotation == 15:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
                    yellowTrain4Rotation = 16
                    yellowTrain4Turns = 33
            if yellowTrain4Turns == 33:
                yellowTrain4Y += .25
            if yellowTrain4X == 165 and yellowTrain4Y == 257:
                if yellowTrain4Rotation == 16:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 17
                    yellowTrain4Turns = 34
            if yellowTrain4Turns == 34:
                yellowTrain4X -= .25
            if yellowTrain4X == 71 and yellowTrain4Y == 257:
                if yellowTrain4Rotation == 17:
                    yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
                    yellowTrain4Rotation = 18
                    yellowTrain4Turns = 35
            if yellowTrain4Turns == 35:
                yellowTrain4Y -= .25


        if greenTrainNum0 == 1:
            screen.blit(greenTrain,[greenTrainX,greenTrainY])
            if greenTrainTurns == 0:
                greenTrainY -= .25
            if greenTrainY == 270 and greenTrainX == 578:
                greenTrainTurns = 1
            if greenTrainTurns == 1:
                if greenTrainRotation == 0:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 1
                    greenTrainTurns = 2
            if greenTrainTurns == 2:
                greenTrainX -= .25

            #first track
            if greenTrainY == 270 and greenTrainX == 493:
                if track1Visible == 1:
                    greenTrainTurns = 3
                else:
                    greenTrainTurns = 23
            if greenTrainTurns == 3:
                greenTrainX -= .25
            if greenTrainX == 329 and greenTrainY == 270:
                greenTrainTurns = 4
            if greenTrainTurns == 4:
                if greenTrainRotation == 1:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 2
                    greenTrainTurns = 5
            if greenTrainTurns == 5:
                greenTrainY += .25
            if greenTrainX == 329 and greenTrainY == 370:
                greenTrainTurns = 6
            if greenTrainTurns == 6:
                if greenTrainRotation == 2:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 3
                    greenTrainTurns = 7
            if greenTrainTurns == 7:
                greenTrainX += .25

            #second track
            if greenTrainX == 470 and greenTrainY == 370:
                if track2Visible == 1:
                    greenTrainTurns = 8
                else:
                    greenTrainTurns = 13

            #going to orange station
            if greenTrainTurns == 8:
                greenTrainX += .25
            if greenTrainX == 530 and greenTrainY == 370:
                greenTrainTurns = 9
            if greenTrainTurns == 9:
                if greenTrainRotation == 3:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 4
                    greenTrainTurns = 10
            if greenTrainTurns == 10:
                greenTrainY -= .25
            if greenTrainX == 530 and greenTrainY == 320:
                greenTrainTurns = 11
            if greenTrainTurns == 11:
                if greenTrainRotation == 4:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 5
                    greenTrainTurns = 12
            if greenTrainTurns == 12:
                greenTrainX -= .25
            if greenTrainTurns == 13:
                if greenTrainRotation == 3:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 6
                    greenTrainTurns = 14
            if greenTrainTurns == 14:
                greenTrainY += .25
            if greenTrainY == 432 and greenTrainX == 470:
                greenTrainTurns = 15
            if greenTrainTurns == 15:
                if greenTrainRotation == 6:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 7
                    greenTrainTurns = 16
            if greenTrainTurns == 16:
                greenTrainX -= .25

            #Third track
            if greenTrainY == 432 and greenTrainX == 255:
                if track3Visible == 1:
                    greenTrainTurns = 17
                else:
                    greenTrainTurns = 21

            #going to yellow station
            if greenTrainTurns == 17:
                greenTrainX -= .25
            if greenTrainY == 432 and greenTrainX == 18:
                greenTrainTurns = 18
            if greenTrainTurns == 18:
                if greenTrainRotation == 7:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 8
                    greenTrainTurns = 19
            if greenTrainTurns == 19:
                greenTrainY -= .25
            if greenTrainY == 335 and greenTrainX == 18:
                if greenTrainRotation == 8:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 9
                    greenTrainTurns = 20
            if greenTrainTurns == 20:
                greenTrainX += .25

            #going to purple station
            if greenTrainTurns == 21:
                if greenTrainRotation == 7:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 10
                    greenTrainTurns = 22
            if greenTrainTurns == 22:
                greenTrainY -= .25

            if greenTrainTurns == 23:
                if greenTrainRotation == 1:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 11
                    greenTrainTurns = 24
            if greenTrainTurns == 24:
                greenTrainY -= .25

            #fourth track
            if greenTrainX == 493 and greenTrainY == 178:
                if track4Visible == 1:
                    greenTrainTurns = 29
                else:
                    greenTrainTurns = 25

            #going to green station
            if greenTrainTurns == 25:
                if greenTrainRotation == 11:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 12
                    greenTrainTurns = 26
            if greenTrainTurns == 26:
                greenTrainX -= .25
            if greenTrainX == 335 and greenTrainY == 178:
                if greenTrainRotation == 12:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 13
                    greenTrainTurns = 27
            if greenTrainTurns == 27:
                greenTrainY -= .25
            if greenTrainX == 335 and greenTrainY == 100:
                if greenTrainRotation == 13:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 14
                    greenTrainTurns = 28
            if greenTrainTurns == 28:
                greenTrainX += .25

            if greenTrainTurns == 29:
                greenTrainY -= .25
            if greenTrainX == 493 and greenTrainY == 27:
                if greenTrainRotation == 11:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 15
                    greenTrainTurns = 30
            if greenTrainTurns == 30:
                greenTrainX -= .25

            #fifth track
            if greenTrainX == 165 and greenTrainY == 27:
                if track5Visible == 1:
                    greenTrainTurns = 31
                else:
                    greenTrainTurns = 32

            #going to red station
            if greenTrainTurns == 31:
                greenTrainX -= .25

            #going to blue station
            if greenTrainTurns == 32:
                if greenTrainRotation == 15:
                    greenTrain = pygame.transform.rotate(greenTrain, 90)
                    greenTrainRotation = 16
                    greenTrainTurns = 33
            if greenTrainTurns == 33:
                greenTrainY += .25
            if greenTrainX == 165 and greenTrainY == 257:
                if greenTrainRotation == 16:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 17
                    greenTrainTurns = 34
            if greenTrainTurns == 34:
                greenTrainX -= .25
            if greenTrainX == 71 and greenTrainY == 257:
                if greenTrainRotation == 17:
                    greenTrain = pygame.transform.rotate(greenTrain, 270)
                    greenTrainRotation = 18
                    greenTrainTurns = 35
            if greenTrainTurns == 35:
                greenTrainY -= .25

        if greenTrainNum1 == 1:
            screen.blit(greenTrain1,[greenTrain1X,greenTrain1Y])
            if greenTrain1Turns == 0:
                greenTrain1Y -= .25
            if greenTrain1Y == 270 and greenTrain1X == 578:
                greenTrain1Turns = 1
            if greenTrain1Turns == 1:
                if greenTrain1Rotation == 0:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 1
                    greenTrain1Turns = 2
            if greenTrain1Turns == 2:
                greenTrain1X -= .25

            #first track
            if greenTrain1Y == 270 and greenTrain1X == 493:
                if track1Visible == 1:
                    greenTrain1Turns = 3
                else:
                    greenTrain1Turns = 23
            if greenTrain1Turns == 3:
                greenTrain1X -= .25
            if greenTrain1X == 329 and greenTrain1Y == 270:
                greenTrain1Turns = 4
            if greenTrain1Turns == 4:
                if greenTrain1Rotation == 1:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 2
                    greenTrain1Turns = 5
            if greenTrain1Turns == 5:
                greenTrain1Y += .25
            if greenTrain1X == 329 and greenTrain1Y == 370:
                greenTrain1Turns = 6
            if greenTrain1Turns == 6:
                if greenTrain1Rotation == 2:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 3
                    greenTrain1Turns = 7
            if greenTrain1Turns == 7:
                greenTrain1X += .25

            #second track
            if greenTrain1X == 470 and greenTrain1Y == 370:
                if track2Visible == 1:
                    greenTrain1Turns = 8
                else:
                    greenTrain1Turns = 13

            #going to orange station
            if greenTrain1Turns == 8:
                greenTrain1X += .25
            if greenTrain1X == 530 and greenTrain1Y == 370:
                greenTrain1Turns = 9
            if greenTrain1Turns == 9:
                if greenTrain1Rotation == 3:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 4
                    greenTrain1Turns = 10
            if greenTrain1Turns == 10:
                greenTrain1Y -= .25
            if greenTrain1X == 530 and greenTrain1Y == 320:
                greenTrain1Turns = 11
            if greenTrain1Turns == 11:
                if greenTrain1Rotation == 4:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 5
                    greenTrain1Turns = 12
            if greenTrain1Turns == 12:
                greenTrain1X -= .25
            if greenTrain1Turns == 13:
                if greenTrain1Rotation == 3:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 6
                    greenTrain1Turns = 14
            if greenTrain1Turns == 14:
                greenTrain1Y += .25
            if greenTrain1Y == 432 and greenTrain1X == 470:
                greenTrain1Turns = 15
            if greenTrain1Turns == 15:
                if greenTrain1Rotation == 6:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 7
                    greenTrain1Turns = 16
            if greenTrain1Turns == 16:
                greenTrain1X -= .25

            #Third track
            if greenTrain1Y == 432 and greenTrain1X == 255:
                if track3Visible == 1:
                    greenTrain1Turns = 17
                else:
                    greenTrain1Turns = 21

            #going to yellow station
            if greenTrain1Turns == 17:
                greenTrain1X -= .25
            if greenTrain1Y == 432 and greenTrain1X == 18:
                greenTrain1Turns = 18
            if greenTrain1Turns == 18:
                if greenTrain1Rotation == 7:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 8
                    greenTrain1Turns = 19
            if greenTrain1Turns == 19:
                greenTrain1Y -= .25
            if greenTrain1Y == 335 and greenTrain1X == 18:
                if greenTrain1Rotation == 8:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 9
                    greenTrain1Turns = 20
            if greenTrain1Turns == 20:
                greenTrain1X += .25

            #going to purple station
            if greenTrain1Turns == 21:
                if greenTrain1Rotation == 7:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 10
                    greenTrain1Turns = 22
            if greenTrain1Turns == 22:
                greenTrain1Y -= .25

            if greenTrain1Turns == 23:
                if greenTrain1Rotation == 1:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 11
                    greenTrain1Turns = 24
            if greenTrain1Turns == 24:
                greenTrain1Y -= .25

            #fourth track
            if greenTrain1X == 493 and greenTrain1Y == 178:
                if track4Visible == 1:
                    greenTrain1Turns = 29
                else:
                    greenTrain1Turns = 25

            #going to green station
            if greenTrain1Turns == 25:
                if greenTrain1Rotation == 11:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 12
                    greenTrain1Turns = 26
            if greenTrain1Turns == 26:
                greenTrain1X -= .25
            if greenTrain1X == 335 and greenTrain1Y == 178:
                if greenTrain1Rotation == 12:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 13
                    greenTrain1Turns = 27
            if greenTrain1Turns == 27:
                greenTrain1Y -= .25
            if greenTrain1X == 335 and greenTrain1Y == 100:
                if greenTrain1Rotation == 13:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 14
                    greenTrain1Turns = 28
            if greenTrain1Turns == 28:
                greenTrain1X += .25

            if greenTrain1Turns == 29:
                greenTrain1Y -= .25
            if greenTrain1X == 493 and greenTrain1Y == 27:
                if greenTrain1Rotation == 11:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 15
                    greenTrain1Turns = 30
            if greenTrain1Turns == 30:
                greenTrain1X -= .25

            #fifth track
            if greenTrain1X == 165 and greenTrain1Y == 27:
                if track5Visible == 1:
                    greenTrain1Turns = 31
                else:
                    greenTrain1Turns = 32

            #going to red station
            if greenTrain1Turns == 31:
                greenTrain1X -= .25

            #going to blue station
            if greenTrain1Turns == 32:
                if greenTrain1Rotation == 15:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
                    greenTrain1Rotation = 16
                    greenTrain1Turns = 33
            if greenTrain1Turns == 33:
                greenTrain1Y += .25
            if greenTrain1X == 165 and greenTrain1Y == 257:
                if greenTrain1Rotation == 16:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 17
                    greenTrain1Turns = 34
            if greenTrain1Turns == 34:
                greenTrain1X -= .25
            if greenTrain1X == 71 and greenTrain1Y == 257:
                if greenTrain1Rotation == 17:
                    greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
                    greenTrain1Rotation = 18
                    greenTrain1Turns = 35
            if greenTrain1Turns == 35:
                greenTrain1Y -= .25


        if greenTrainNum2 == 1:
            screen.blit(greenTrain2,[greenTrain2X,greenTrain2Y])
            if greenTrain2Turns == 0:
                greenTrain2Y -= .25
            if greenTrain2Y == 270 and greenTrain2X == 578:
                greenTrain2Turns = 1
            if greenTrain2Turns == 1:
                if greenTrain2Rotation == 0:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 1
                    greenTrain2Turns = 2
            if greenTrain2Turns == 2:
                greenTrain2X -= .25

            #first track
            if greenTrain2Y == 270 and greenTrain2X == 493:
                if track1Visible == 1:
                    greenTrain2Turns = 3
                else:
                    greenTrain2Turns = 23
            if greenTrain2Turns == 3:
                greenTrain2X -= .25
            if greenTrain2X == 329 and greenTrain2Y == 270:
                greenTrain2Turns = 4
            if greenTrain2Turns == 4:
                if greenTrain2Rotation == 1:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 2
                    greenTrain2Turns = 5
            if greenTrain2Turns == 5:
                greenTrain2Y += .25
            if greenTrain2X == 329 and greenTrain2Y == 370:
                greenTrain2Turns = 6
            if greenTrain2Turns == 6:
                if greenTrain2Rotation == 2:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 3
                    greenTrain2Turns = 7
            if greenTrain2Turns == 7:
                greenTrain2X += .25

            #second track
            if greenTrain2X == 470 and greenTrain2Y == 370:
                if track2Visible == 1:
                    greenTrain2Turns = 8
                else:
                    greenTrain2Turns = 13

            #going to orange station
            if greenTrain2Turns == 8:
                greenTrain2X += .25
            if greenTrain2X == 530 and greenTrain2Y == 370:
                greenTrain2Turns = 9
            if greenTrain2Turns == 9:
                if greenTrain2Rotation == 3:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 4
                    greenTrain2Turns = 10
            if greenTrain2Turns == 10:
                greenTrain2Y -= .25
            if greenTrain2X == 530 and greenTrain2Y == 320:
                greenTrain2Turns = 11
            if greenTrain2Turns == 11:
                if greenTrain2Rotation == 4:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 5
                    greenTrain2Turns = 12
            if greenTrain2Turns == 12:
                greenTrain2X -= .25
            if greenTrain2Turns == 13:
                if greenTrain2Rotation == 3:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 6
                    greenTrain2Turns = 14
            if greenTrain2Turns == 14:
                greenTrain2Y += .25
            if greenTrain2Y == 432 and greenTrain2X == 470:
                greenTrain2Turns = 15
            if greenTrain2Turns == 15:
                if greenTrain2Rotation == 6:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 7
                    greenTrain2Turns = 16
            if greenTrain2Turns == 16:
                greenTrain2X -= .25

            #Third track
            if greenTrain2Y == 432 and greenTrain2X == 255:
                if track3Visible == 1:
                    greenTrain2Turns = 17
                else:
                    greenTrain2Turns = 21

            #going to yellow station
            if greenTrain2Turns == 17:
                greenTrain2X -= .25
            if greenTrain2Y == 432 and greenTrain2X == 18:
                greenTrain2Turns = 18
            if greenTrain2Turns == 18:
                if greenTrain2Rotation == 7:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 8
                    greenTrain2Turns = 19
            if greenTrain2Turns == 19:
                greenTrain2Y -= .25
            if greenTrain2Y == 335 and greenTrain2X == 18:
                if greenTrain2Rotation == 8:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 9
                    greenTrain2Turns = 20
            if greenTrain2Turns == 20:
                greenTrain2X += .25

            #going to purple station
            if greenTrain2Turns == 21:
                if greenTrain2Rotation == 7:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 10
                    greenTrain2Turns = 22
            if greenTrain2Turns == 22:
                greenTrain2Y -= .25

            if greenTrain2Turns == 23:
                if greenTrain2Rotation == 1:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 11
                    greenTrain2Turns = 24
            if greenTrain2Turns == 24:
                greenTrain2Y -= .25

            #fourth track
            if greenTrain2X == 493 and greenTrain2Y == 178:
                if track4Visible == 1:
                    greenTrain2Turns = 29
                else:
                    greenTrain2Turns = 25

            #going to green station
            if greenTrain2Turns == 25:
                if greenTrain2Rotation == 11:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 12
                    greenTrain2Turns = 26
            if greenTrain2Turns == 26:
                greenTrain2X -= .25
            if greenTrain2X == 335 and greenTrain2Y == 178:
                if greenTrain2Rotation == 12:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 13
                    greenTrain2Turns = 27
            if greenTrain2Turns == 27:
                greenTrain2Y -= .25
            if greenTrain2X == 335 and greenTrain2Y == 100:
                if greenTrain2Rotation == 13:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 14
                    greenTrain2Turns = 28
            if greenTrain2Turns == 28:
                greenTrain2X += .25

            if greenTrain2Turns == 29:
                greenTrain2Y -= .25
            if greenTrain2X == 493 and greenTrain2Y == 27:
                if greenTrain2Rotation == 11:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 15
                    greenTrain2Turns = 30
            if greenTrain2Turns == 30:
                greenTrain2X -= .25

            #fifth track
            if greenTrain2X == 165 and greenTrain2Y == 27:
                if track5Visible == 1:
                    greenTrain2Turns = 31
                else:
                    greenTrain2Turns = 32

            #going to red station
            if greenTrain2Turns == 31:
                greenTrain2X -= .25

            #going to blue station
            if greenTrain2Turns == 32:
                if greenTrain2Rotation == 15:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
                    greenTrain2Rotation = 16
                    greenTrain2Turns = 33
            if greenTrain2Turns == 33:
                greenTrain2Y += .25
            if greenTrain2X == 165 and greenTrain2Y == 257:
                if greenTrain2Rotation == 16:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 17
                    greenTrain2Turns = 34
            if greenTrain2Turns == 34:
                greenTrain2X -= .25
            if greenTrain2X == 71 and greenTrain2Y == 257:
                if greenTrain2Rotation == 17:
                    greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
                    greenTrain2Rotation = 18
                    greenTrain2Turns = 35
            if greenTrain2Turns == 35:
                greenTrain2Y -= .25

        if greenTrainNum3 == 1:
            screen.blit(greenTrain3,[greenTrain3X,greenTrain3Y])
            if greenTrain3Turns == 0:
                greenTrain3Y -= .25
            if greenTrain3Y == 270 and greenTrain3X == 578:
                greenTrain3Turns = 1
            if greenTrain3Turns == 1:
                if greenTrain3Rotation == 0:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 1
                    greenTrain3Turns = 2
            if greenTrain3Turns == 2:
                greenTrain3X -= .25

            #first track
            if greenTrain3Y == 270 and greenTrain3X == 493:
                if track1Visible == 1:
                    greenTrain3Turns = 3
                else:
                    greenTrain3Turns = 23
            if greenTrain3Turns == 3:
                greenTrain3X -= .25
            if greenTrain3X == 329 and greenTrain3Y == 270:
                greenTrain3Turns = 4
            if greenTrain3Turns == 4:
                if greenTrain3Rotation == 1:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 2
                    greenTrain3Turns = 5
            if greenTrain3Turns == 5:
                greenTrain3Y += .25
            if greenTrain3X == 329 and greenTrain3Y == 370:
                greenTrain3Turns = 6
            if greenTrain3Turns == 6:
                if greenTrain3Rotation == 2:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 3
                    greenTrain3Turns = 7
            if greenTrain3Turns == 7:
                greenTrain3X += .25

            #second track
            if greenTrain3X == 470 and greenTrain3Y == 370:
                if track2Visible == 1:
                    greenTrain3Turns = 8
                else:
                    greenTrain3Turns = 13

            #going to orange station
            if greenTrain3Turns == 8:
                greenTrain3X += .25
            if greenTrain3X == 530 and greenTrain3Y == 370:
                greenTrain3Turns = 9
            if greenTrain3Turns == 9:
                if greenTrain3Rotation == 3:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 4
                    greenTrain3Turns = 10
            if greenTrain3Turns == 10:
                greenTrain3Y -= .25
            if greenTrain3X == 530 and greenTrain3Y == 320:
                greenTrain3Turns = 11
            if greenTrain3Turns == 11:
                if greenTrain3Rotation == 4:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 5
                    greenTrain3Turns = 12
            if greenTrain3Turns == 12:
                greenTrain3X -= .25
            if greenTrain3Turns == 13:
                if greenTrain3Rotation == 3:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 6
                    greenTrain3Turns = 14
            if greenTrain3Turns == 14:
                greenTrain3Y += .25
            if greenTrain3Y == 432 and greenTrain3X == 470:
                greenTrain3Turns = 15
            if greenTrain3Turns == 15:
                if greenTrain3Rotation == 6:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 7
                    greenTrain3Turns = 16
            if greenTrain3Turns == 16:
                greenTrain3X -= .25

            #Third track
            if greenTrain3Y == 432 and greenTrain3X == 255:
                if track3Visible == 1:
                    greenTrain3Turns = 17
                else:
                    greenTrain3Turns = 21

            #going to yellow station
            if greenTrain3Turns == 17:
                greenTrain3X -= .25
            if greenTrain3Y == 432 and greenTrain3X == 18:
                greenTrain3Turns = 18
            if greenTrain3Turns == 18:
                if greenTrain3Rotation == 7:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 8
                    greenTrain3Turns = 19
            if greenTrain3Turns == 19:
                greenTrain3Y -= .25
            if greenTrain3Y == 335 and greenTrain3X == 18:
                if greenTrain3Rotation == 8:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 9
                    greenTrain3Turns = 20
            if greenTrain3Turns == 20:
                greenTrain3X += .25

            #going to purple station
            if greenTrain3Turns == 21:
                if greenTrain3Rotation == 7:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 10
                    greenTrain3Turns = 22
            if greenTrain3Turns == 22:
                greenTrain3Y -= .25

            if greenTrain3Turns == 23:
                if greenTrain3Rotation == 1:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 11
                    greenTrain3Turns = 24
            if greenTrain3Turns == 24:
                greenTrain3Y -= .25

            #fourth track
            if greenTrain3X == 493 and greenTrain3Y == 178:
                if track4Visible == 1:
                    greenTrain3Turns = 29
                else:
                    greenTrain3Turns = 25

            #going to green station
            if greenTrain3Turns == 25:
                if greenTrain3Rotation == 11:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 12
                    greenTrain3Turns = 26
            if greenTrain3Turns == 26:
                greenTrain3X -= .25
            if greenTrain3X == 335 and greenTrain3Y == 178:
                if greenTrain3Rotation == 12:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 13
                    greenTrain3Turns = 27
            if greenTrain3Turns == 27:
                greenTrain3Y -= .25
            if greenTrain3X == 335 and greenTrain3Y == 100:
                if greenTrain3Rotation == 13:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 14
                    greenTrain3Turns = 28
            if greenTrain3Turns == 28:
                greenTrain3X += .25

            if greenTrain3Turns == 29:
                greenTrain3Y -= .25
            if greenTrain3X == 493 and greenTrain3Y == 27:
                if greenTrain3Rotation == 11:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 15
                    greenTrain3Turns = 30
            if greenTrain3Turns == 30:
                greenTrain3X -= .25

            #fifth track
            if greenTrain3X == 165 and greenTrain3Y == 27:
                if track5Visible == 1:
                    greenTrain3Turns = 31
                else:
                    greenTrain3Turns = 32

            #going to red station
            if greenTrain3Turns == 31:
                greenTrain3X -= .25

            #going to blue station
            if greenTrain3Turns == 32:
                if greenTrain3Rotation == 15:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
                    greenTrain3Rotation = 16
                    greenTrain3Turns = 33
            if greenTrain3Turns == 33:
                greenTrain3Y += .25
            if greenTrain3X == 165 and greenTrain3Y == 257:
                if greenTrain3Rotation == 16:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 17
                    greenTrain3Turns = 34
            if greenTrain3Turns == 34:
                greenTrain3X -= .25
            if greenTrain3X == 71 and greenTrain3Y == 257:
                if greenTrain3Rotation == 17:
                    greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
                    greenTrain3Rotation = 18
                    greenTrain3Turns = 35
            if greenTrain3Turns == 35:
                greenTrain3Y -= .25


        if greenTrainNum4 == 1:
            screen.blit(greenTrain4,[greenTrain4X,greenTrain4Y])
            if greenTrain4Turns == 0:
                greenTrain4Y -= .25
            if greenTrain4Y == 270 and greenTrain4X == 578:
                greenTrain4Turns = 1
            if greenTrain4Turns == 1:
                if greenTrain4Rotation == 0:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 1
                    greenTrain4Turns = 2
            if greenTrain4Turns == 2:
                greenTrain4X -= .25

            #first track
            if greenTrain4Y == 270 and greenTrain4X == 493:
                if track1Visible == 1:
                    greenTrain4Turns = 3
                else:
                    greenTrain4Turns = 23
            if greenTrain4Turns == 3:
                greenTrain4X -= .25
            if greenTrain4X == 329 and greenTrain4Y == 270:
                greenTrain4Turns = 4
            if greenTrain4Turns == 4:
                if greenTrain4Rotation == 1:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 2
                    greenTrain4Turns = 5
            if greenTrain4Turns == 5:
                greenTrain4Y += .25
            if greenTrain4X == 329 and greenTrain4Y == 370:
                greenTrain4Turns = 6
            if greenTrain4Turns == 6:
                if greenTrain4Rotation == 2:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 3
                    greenTrain4Turns = 7
            if greenTrain4Turns == 7:
                greenTrain4X += .25

            #second track
            if greenTrain4X == 470 and greenTrain4Y == 370:
                if track2Visible == 1:
                    greenTrain4Turns = 8
                else:
                    greenTrain4Turns = 13

            #going to orange station
            if greenTrain4Turns == 8:
                greenTrain4X += .25
            if greenTrain4X == 530 and greenTrain4Y == 370:
                greenTrain4Turns = 9
            if greenTrain4Turns == 9:
                if greenTrain4Rotation == 3:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 4
                    greenTrain4Turns = 10
            if greenTrain4Turns == 10:
                greenTrain4Y -= .25
            if greenTrain4X == 530 and greenTrain4Y == 320:
                greenTrain4Turns = 11
            if greenTrain4Turns == 11:
                if greenTrain4Rotation == 4:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 5
                    greenTrain4Turns = 12
            if greenTrain4Turns == 12:
                greenTrain4X -= .25
            if greenTrain4Turns == 13:
                if greenTrain4Rotation == 3:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 6
                    greenTrain4Turns = 14
            if greenTrain4Turns == 14:
                greenTrain4Y += .25
            if greenTrain4Y == 432 and greenTrain4X == 470:
                greenTrain4Turns = 15
            if greenTrain4Turns == 15:
                if greenTrain4Rotation == 6:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 7
                    greenTrain4Turns = 16
            if greenTrain4Turns == 16:
                greenTrain4X -= .25

            #Third track
            if greenTrain4Y == 432 and greenTrain4X == 255:
                if track3Visible == 1:
                    greenTrain4Turns = 17
                else:
                    greenTrain4Turns = 21

            #going to yellow station
            if greenTrain4Turns == 17:
                greenTrain4X -= .25
            if greenTrain4Y == 432 and greenTrain4X == 18:
                greenTrain4Turns = 18
            if greenTrain4Turns == 18:
                if greenTrain4Rotation == 7:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 8
                    greenTrain4Turns = 19
            if greenTrain4Turns == 19:
                greenTrain4Y -= .25
            if greenTrain4Y == 335 and greenTrain4X == 18:
                if greenTrain4Rotation == 8:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 9
                    greenTrain4Turns = 20
            if greenTrain4Turns == 20:
                greenTrain4X += .25

            #going to purple station
            if greenTrain4Turns == 21:
                if greenTrain4Rotation == 7:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 10
                    greenTrain4Turns = 22
            if greenTrain4Turns == 22:
                greenTrain4Y -= .25

            if greenTrain4Turns == 23:
                if greenTrain4Rotation == 1:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 11
                    greenTrain4Turns = 24
            if greenTrain4Turns == 24:
                greenTrain4Y -= .25

            #fourth track
            if greenTrain4X == 493 and greenTrain4Y == 178:
                if track4Visible == 1:
                    greenTrain4Turns = 29
                else:
                    greenTrain4Turns = 25

            #going to green station
            if greenTrain4Turns == 25:
                if greenTrain4Rotation == 11:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 12
                    greenTrain4Turns = 26
            if greenTrain4Turns == 26:
                greenTrain4X -= .25
            if greenTrain4X == 335 and greenTrain4Y == 178:
                if greenTrain4Rotation == 12:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 13
                    greenTrain4Turns = 27
            if greenTrain4Turns == 27:
                greenTrain4Y -= .25
            if greenTrain4X == 335 and greenTrain4Y == 100:
                if greenTrain4Rotation == 13:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 14
                    greenTrain4Turns = 28
            if greenTrain4Turns == 28:
                greenTrain4X += .25

            if greenTrain4Turns == 29:
                greenTrain4Y -= .25
            if greenTrain4X == 493 and greenTrain4Y == 27:
                if greenTrain4Rotation == 11:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 15
                    greenTrain4Turns = 30
            if greenTrain4Turns == 30:
                greenTrain4X -= .25

            #fifth track
            if greenTrain4X == 165 and greenTrain4Y == 27:
                if track5Visible == 1:
                    greenTrain4Turns = 31
                else:
                    greenTrain4Turns = 32

            #going to red station
            if greenTrain4Turns == 31:
                greenTrain4X -= .25

            #going to blue station
            if greenTrain4Turns == 32:
                if greenTrain4Rotation == 15:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
                    greenTrain4Rotation = 16
                    greenTrain4Turns = 33
            if greenTrain4Turns == 33:
                greenTrain4Y += .25
            if greenTrain4X == 165 and greenTrain4Y == 257:
                if greenTrain4Rotation == 16:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 17
                    greenTrain4Turns = 34
            if greenTrain4Turns == 34:
                greenTrain4X -= .25
            if greenTrain4X == 71 and greenTrain4Y == 257:
                if greenTrain4Rotation == 17:
                    greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
                    greenTrain4Rotation = 18
                    greenTrain4Turns = 35
            if greenTrain4Turns == 35:
                greenTrain4Y -= .25


        if blueTrainNum0 == 1:
            screen.blit(blueTrain,[blueTrainX,blueTrainY])
            if blueTrainTurns == 0:
                blueTrainY -= .25
            if blueTrainY == 270 and blueTrainX == 578:
                blueTrainTurns = 1
            if blueTrainTurns == 1:
                if blueTrainRotation == 0:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 1
                    blueTrainTurns = 2
            if blueTrainTurns == 2:
                blueTrainX -= .25

            #first track
            if blueTrainY == 270 and blueTrainX == 493:
                if track1Visible == 1:
                    blueTrainTurns = 3
                else:
                    blueTrainTurns = 23
            if blueTrainTurns == 3:
                blueTrainX -= .25
            if blueTrainX == 329 and blueTrainY == 270:
                blueTrainTurns = 4
            if blueTrainTurns == 4:
                if blueTrainRotation == 1:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 2
                    blueTrainTurns = 5
            if blueTrainTurns == 5:
                blueTrainY += .25
            if blueTrainX == 329 and blueTrainY == 370:
                blueTrainTurns = 6
            if blueTrainTurns == 6:
                if blueTrainRotation == 2:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 3
                    blueTrainTurns = 7
            if blueTrainTurns == 7:
                blueTrainX += .25

            #second track
            if blueTrainX == 470 and blueTrainY == 370:
                if track2Visible == 1:
                    blueTrainTurns = 8
                else:
                    blueTrainTurns = 13

            #going to orange station
            if blueTrainTurns == 8:
                blueTrainX += .25
            if blueTrainX == 530 and blueTrainY == 370:
                blueTrainTurns = 9
            if blueTrainTurns == 9:
                if blueTrainRotation == 3:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 4
                    blueTrainTurns = 10
            if blueTrainTurns == 10:
                blueTrainY -= .25
            if blueTrainX == 530 and blueTrainY == 320:
                blueTrainTurns = 11
            if blueTrainTurns == 11:
                if blueTrainRotation == 4:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 5
                    blueTrainTurns = 12
            if blueTrainTurns == 12:
                blueTrainX -= .25
            if blueTrainTurns == 13:
                if blueTrainRotation == 3:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 6
                    blueTrainTurns = 14
            if blueTrainTurns == 14:
                blueTrainY += .25
            if blueTrainY == 432 and blueTrainX == 470:
                blueTrainTurns = 15
            if blueTrainTurns == 15:
                if blueTrainRotation == 6:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 7
                    blueTrainTurns = 16
            if blueTrainTurns == 16:
                blueTrainX -= .25

            #Third track
            if blueTrainY == 432 and blueTrainX == 255:
                if track3Visible == 1:
                    blueTrainTurns = 17
                else:
                    blueTrainTurns = 21

            #going to yellow station
            if blueTrainTurns == 17:
                blueTrainX -= .25
            if blueTrainY == 432 and blueTrainX == 18:
                blueTrainTurns = 18
            if blueTrainTurns == 18:
                if blueTrainRotation == 7:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 8
                    blueTrainTurns = 19
            if blueTrainTurns == 19:
                blueTrainY -= .25
            if blueTrainY == 335 and blueTrainX == 18:
                if blueTrainRotation == 8:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 9
                    blueTrainTurns = 20
            if blueTrainTurns == 20:
                blueTrainX += .25

            #going to purple station
            if blueTrainTurns == 21:
                if blueTrainRotation == 7:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 10
                    blueTrainTurns = 22
            if blueTrainTurns == 22:
                blueTrainY -= .25

            if blueTrainTurns == 23:
                if blueTrainRotation == 1:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 11
                    blueTrainTurns = 24
            if blueTrainTurns == 24:
                blueTrainY -= .25

            #fourth track
            if blueTrainX == 493 and blueTrainY == 178:
                if track4Visible == 1:
                    blueTrainTurns = 29
                else:
                    blueTrainTurns = 25

            #going to green station
            if blueTrainTurns == 25:
                if blueTrainRotation == 11:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 12
                    blueTrainTurns = 26
            if blueTrainTurns == 26:
                blueTrainX -= .25
            if blueTrainX == 335 and blueTrainY == 178:
                if blueTrainRotation == 12:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 13
                    blueTrainTurns = 27
            if blueTrainTurns == 27:
                blueTrainY -= .25
            if blueTrainX == 335 and blueTrainY == 100:
                if blueTrainRotation == 13:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 14
                    blueTrainTurns = 28
            if blueTrainTurns == 28:
                blueTrainX += .25

            if blueTrainTurns == 29:
                blueTrainY -= .25
            if blueTrainX == 493 and blueTrainY == 27:
                if blueTrainRotation == 11:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 15
                    blueTrainTurns = 30
            if blueTrainTurns == 30:
                blueTrainX -= .25

            #fifth track
            if blueTrainX == 165 and blueTrainY == 27:
                if track5Visible == 1:
                    blueTrainTurns = 31
                else:
                    blueTrainTurns = 32

            #going to red station
            if blueTrainTurns == 31:
                blueTrainX -= .25

            #going to blue station
            if blueTrainTurns == 32:
                if blueTrainRotation == 15:
                    blueTrain = pygame.transform.rotate(blueTrain, 90)
                    blueTrainRotation = 16
                    blueTrainTurns = 33
            if blueTrainTurns == 33:
                blueTrainY += .25
            if blueTrainX == 165 and blueTrainY == 257:
                if blueTrainRotation == 16:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 17
                    blueTrainTurns = 34
            if blueTrainTurns == 34:
                blueTrainX -= .25
            if blueTrainX == 71 and blueTrainY == 257:
                if blueTrainRotation == 17:
                    blueTrain = pygame.transform.rotate(blueTrain, 270)
                    blueTrainRotation = 18
                    blueTrainTurns = 35
            if blueTrainTurns == 35:
                blueTrainY -= .25

        if blueTrainNum1 == 1:
            screen.blit(blueTrain1,[blueTrain1X,blueTrain1Y])
            if blueTrain1Turns == 0:
                blueTrain1Y -= .25
            if blueTrain1Y == 270 and blueTrain1X == 578:
                blueTrain1Turns = 1
            if blueTrain1Turns == 1:
                if blueTrain1Rotation == 0:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 1
                    blueTrain1Turns = 2
            if blueTrain1Turns == 2:
                blueTrain1X -= .25

            #first track
            if blueTrain1Y == 270 and blueTrain1X == 493:
                if track1Visible == 1:
                    blueTrain1Turns = 3
                else:
                    blueTrain1Turns = 23
            if blueTrain1Turns == 3:
                blueTrain1X -= .25
            if blueTrain1X == 329 and blueTrain1Y == 270:
                blueTrain1Turns = 4
            if blueTrain1Turns == 4:
                if blueTrain1Rotation == 1:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 2
                    blueTrain1Turns = 5
            if blueTrain1Turns == 5:
                blueTrain1Y += .25
            if blueTrain1X == 329 and blueTrain1Y == 370:
                blueTrain1Turns = 6
            if blueTrain1Turns == 6:
                if blueTrain1Rotation == 2:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 3
                    blueTrain1Turns = 7
            if blueTrain1Turns == 7:
                blueTrain1X += .25

            #second track
            if blueTrain1X == 470 and blueTrain1Y == 370:
                if track2Visible == 1:
                    blueTrain1Turns = 8
                else:
                    blueTrain1Turns = 13

            #going to orange station
            if blueTrain1Turns == 8:
                blueTrain1X += .25
            if blueTrain1X == 530 and blueTrain1Y == 370:
                blueTrain1Turns = 9
            if blueTrain1Turns == 9:
                if blueTrain1Rotation == 3:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 4
                    blueTrain1Turns = 10
            if blueTrain1Turns == 10:
                blueTrain1Y -= .25
            if blueTrain1X == 530 and blueTrain1Y == 320:
                blueTrain1Turns = 11
            if blueTrain1Turns == 11:
                if blueTrain1Rotation == 4:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 5
                    blueTrain1Turns = 12
            if blueTrain1Turns == 12:
                blueTrain1X -= .25
            if blueTrain1Turns == 13:
                if blueTrain1Rotation == 3:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 6
                    blueTrain1Turns = 14
            if blueTrain1Turns == 14:
                blueTrain1Y += .25
            if blueTrain1Y == 432 and blueTrain1X == 470:
                blueTrain1Turns = 15
            if blueTrain1Turns == 15:
                if blueTrain1Rotation == 6:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 7
                    blueTrain1Turns = 16
            if blueTrain1Turns == 16:
                blueTrain1X -= .25

            #Third track
            if blueTrain1Y == 432 and blueTrain1X == 255:
                if track3Visible == 1:
                    blueTrain1Turns = 17
                else:
                    blueTrain1Turns = 21

            #going to yellow station
            if blueTrain1Turns == 17:
                blueTrain1X -= .25
            if blueTrain1Y == 432 and blueTrain1X == 18:
                blueTrain1Turns = 18
            if blueTrain1Turns == 18:
                if blueTrain1Rotation == 7:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 8
                    blueTrain1Turns = 19
            if blueTrain1Turns == 19:
                blueTrain1Y -= .25
            if blueTrain1Y == 335 and blueTrain1X == 18:
                if blueTrain1Rotation == 8:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 9
                    blueTrain1Turns = 20
            if blueTrain1Turns == 20:
                blueTrain1X += .25

            #going to purple station
            if blueTrain1Turns == 21:
                if blueTrain1Rotation == 7:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 10
                    blueTrain1Turns = 22
            if blueTrain1Turns == 22:
                blueTrain1Y -= .25

            if blueTrain1Turns == 23:
                if blueTrain1Rotation == 1:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 11
                    blueTrain1Turns = 24
            if blueTrain1Turns == 24:
                blueTrain1Y -= .25

            #fourth track
            if blueTrain1X == 493 and blueTrain1Y == 178:
                if track4Visible == 1:
                    blueTrain1Turns = 29
                else:
                    blueTrain1Turns = 25

            #going to green station
            if blueTrain1Turns == 25:
                if blueTrain1Rotation == 11:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 12
                    blueTrain1Turns = 26
            if blueTrain1Turns == 26:
                blueTrain1X -= .25
            if blueTrain1X == 335 and blueTrain1Y == 178:
                if blueTrain1Rotation == 12:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 13
                    blueTrain1Turns = 27
            if blueTrain1Turns == 27:
                blueTrain1Y -= .25
            if blueTrain1X == 335 and blueTrain1Y == 100:
                if blueTrain1Rotation == 13:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 14
                    blueTrain1Turns = 28
            if blueTrain1Turns == 28:
                blueTrain1X += .25

            if blueTrain1Turns == 29:
                blueTrain1Y -= .25
            if blueTrain1X == 493 and blueTrain1Y == 27:
                if blueTrain1Rotation == 11:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 15
                    blueTrain1Turns = 30
            if blueTrain1Turns == 30:
                blueTrain1X -= .25

            #fifth track
            if blueTrain1X == 165 and blueTrain1Y == 27:
                if track5Visible == 1:
                    blueTrain1Turns = 31
                else:
                    blueTrain1Turns = 32

            #going to red station
            if blueTrain1Turns == 31:
                blueTrain1X -= .25

            #going to blue station
            if blueTrain1Turns == 32:
                if blueTrain1Rotation == 15:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
                    blueTrain1Rotation = 16
                    blueTrain1Turns = 33
            if blueTrain1Turns == 33:
                blueTrain1Y += .25
            if blueTrain1X == 165 and blueTrain1Y == 257:
                if blueTrain1Rotation == 16:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 17
                    blueTrain1Turns = 34
            if blueTrain1Turns == 34:
                blueTrain1X -= .25
            if blueTrain1X == 71 and blueTrain1Y == 257:
                if blueTrain1Rotation == 17:
                    blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
                    blueTrain1Rotation = 18
                    blueTrain1Turns = 35
            if blueTrain1Turns == 35:
                blueTrain1Y -= .25


        if blueTrainNum2 == 1:
            screen.blit(blueTrain2,[blueTrain2X,blueTrain2Y])
            if blueTrain2Turns == 0:
                blueTrain2Y -= .25
            if blueTrain2Y == 270 and blueTrain2X == 578:
                blueTrain2Turns = 1
            if blueTrain2Turns == 1:
                if blueTrain2Rotation == 0:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 1
                    blueTrain2Turns = 2
            if blueTrain2Turns == 2:
                blueTrain2X -= .25

            #first track
            if blueTrain2Y == 270 and blueTrain2X == 493:
                if track1Visible == 1:
                    blueTrain2Turns = 3
                else:
                    blueTrain2Turns = 23
            if blueTrain2Turns == 3:
                blueTrain2X -= .25
            if blueTrain2X == 329 and blueTrain2Y == 270:
                blueTrain2Turns = 4
            if blueTrain2Turns == 4:
                if blueTrain2Rotation == 1:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 2
                    blueTrain2Turns = 5
            if blueTrain2Turns == 5:
                blueTrain2Y += .25
            if blueTrain2X == 329 and blueTrain2Y == 370:
                blueTrain2Turns = 6
            if blueTrain2Turns == 6:
                if blueTrain2Rotation == 2:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 3
                    blueTrain2Turns = 7
            if blueTrain2Turns == 7:
                blueTrain2X += .25

            #second track
            if blueTrain2X == 470 and blueTrain2Y == 370:
                if track2Visible == 1:
                    blueTrain2Turns = 8
                else:
                    blueTrain2Turns = 13

            #going to orange station
            if blueTrain2Turns == 8:
                blueTrain2X += .25
            if blueTrain2X == 530 and blueTrain2Y == 370:
                blueTrain2Turns = 9
            if blueTrain2Turns == 9:
                if blueTrain2Rotation == 3:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 4
                    blueTrain2Turns = 10
            if blueTrain2Turns == 10:
                blueTrain2Y -= .25
            if blueTrain2X == 530 and blueTrain2Y == 320:
                blueTrain2Turns = 11
            if blueTrain2Turns == 11:
                if blueTrain2Rotation == 4:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 5
                    blueTrain2Turns = 12
            if blueTrain2Turns == 12:
                blueTrain2X -= .25
            if blueTrain2Turns == 13:
                if blueTrain2Rotation == 3:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 6
                    blueTrain2Turns = 14
            if blueTrain2Turns == 14:
                blueTrain2Y += .25
            if blueTrain2Y == 432 and blueTrain2X == 470:
                blueTrain2Turns = 15
            if blueTrain2Turns == 15:
                if blueTrain2Rotation == 6:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 7
                    blueTrain2Turns = 16
            if blueTrain2Turns == 16:
                blueTrain2X -= .25

            #Third track
            if blueTrain2Y == 432 and blueTrain2X == 255:
                if track3Visible == 1:
                    blueTrain2Turns = 17
                else:
                    blueTrain2Turns = 21

            #going to yellow station
            if blueTrain2Turns == 17:
                blueTrain2X -= .25
            if blueTrain2Y == 432 and blueTrain2X == 18:
                blueTrain2Turns = 18
            if blueTrain2Turns == 18:
                if blueTrain2Rotation == 7:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 8
                    blueTrain2Turns = 19
            if blueTrain2Turns == 19:
                blueTrain2Y -= .25
            if blueTrain2Y == 335 and blueTrain2X == 18:
                if blueTrain2Rotation == 8:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 9
                    blueTrain2Turns = 20
            if blueTrain2Turns == 20:
                blueTrain2X += .25

            #going to purple station
            if blueTrain2Turns == 21:
                if blueTrain2Rotation == 7:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 10
                    blueTrain2Turns = 22
            if blueTrain2Turns == 22:
                blueTrain2Y -= .25

            if blueTrain2Turns == 23:
                if blueTrain2Rotation == 1:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 11
                    blueTrain2Turns = 24
            if blueTrain2Turns == 24:
                blueTrain2Y -= .25

            #fourth track
            if blueTrain2X == 493 and blueTrain2Y == 178:
                if track4Visible == 1:
                    blueTrain2Turns = 29
                else:
                    blueTrain2Turns = 25

            #going to green station
            if blueTrain2Turns == 25:
                if blueTrain2Rotation == 11:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 12
                    blueTrain2Turns = 26
            if blueTrain2Turns == 26:
                blueTrain2X -= .25
            if blueTrain2X == 335 and blueTrain2Y == 178:
                if blueTrain2Rotation == 12:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 13
                    blueTrain2Turns = 27
            if blueTrain2Turns == 27:
                blueTrain2Y -= .25
            if blueTrain2X == 335 and blueTrain2Y == 100:
                if blueTrain2Rotation == 13:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 14
                    blueTrain2Turns = 28
            if blueTrain2Turns == 28:
                blueTrain2X += .25

            if blueTrain2Turns == 29:
                blueTrain2Y -= .25
            if blueTrain2X == 493 and blueTrain2Y == 27:
                if blueTrain2Rotation == 11:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 15
                    blueTrain2Turns = 30
            if blueTrain2Turns == 30:
                blueTrain2X -= .25

            #fifth track
            if blueTrain2X == 165 and blueTrain2Y == 27:
                if track5Visible == 1:
                    blueTrain2Turns = 31
                else:
                    blueTrain2Turns = 32

            #going to red station
            if blueTrain2Turns == 31:
                blueTrain2X -= .25

            #going to blue station
            if blueTrain2Turns == 32:
                if blueTrain2Rotation == 15:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
                    blueTrain2Rotation = 16
                    blueTrain2Turns = 33
            if blueTrain2Turns == 33:
                blueTrain2Y += .25
            if blueTrain2X == 165 and blueTrain2Y == 257:
                if blueTrain2Rotation == 16:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 17
                    blueTrain2Turns = 34
            if blueTrain2Turns == 34:
                blueTrain2X -= .25
            if blueTrain2X == 71 and blueTrain2Y == 257:
                if blueTrain2Rotation == 17:
                    blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
                    blueTrain2Rotation = 18
                    blueTrain2Turns = 35
            if blueTrain2Turns == 35:
                blueTrain2Y -= .25

        if blueTrainNum3 == 1:
            screen.blit(blueTrain3,[blueTrain3X,blueTrain3Y])
            if blueTrain3Turns == 0:
                blueTrain3Y -= .25
            if blueTrain3Y == 270 and blueTrain3X == 578:
                blueTrain3Turns = 1
            if blueTrain3Turns == 1:
                if blueTrain3Rotation == 0:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 1
                    blueTrain3Turns = 2
            if blueTrain3Turns == 2:
                blueTrain3X -= .25

            #first track
            if blueTrain3Y == 270 and blueTrain3X == 493:
                if track1Visible == 1:
                    blueTrain3Turns = 3
                else:
                    blueTrain3Turns = 23
            if blueTrain3Turns == 3:
                blueTrain3X -= .25
            if blueTrain3X == 329 and blueTrain3Y == 270:
                blueTrain3Turns = 4
            if blueTrain3Turns == 4:
                if blueTrain3Rotation == 1:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 2
                    blueTrain3Turns = 5
            if blueTrain3Turns == 5:
                blueTrain3Y += .25
            if blueTrain3X == 329 and blueTrain3Y == 370:
                blueTrain3Turns = 6
            if blueTrain3Turns == 6:
                if blueTrain3Rotation == 2:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 3
                    blueTrain3Turns = 7
            if blueTrain3Turns == 7:
                blueTrain3X += .25

            #second track
            if blueTrain3X == 470 and blueTrain3Y == 370:
                if track2Visible == 1:
                    blueTrain3Turns = 8
                else:
                    blueTrain3Turns = 13

            #going to orange station
            if blueTrain3Turns == 8:
                blueTrain3X += .25
            if blueTrain3X == 530 and blueTrain3Y == 370:
                blueTrain3Turns = 9
            if blueTrain3Turns == 9:
                if blueTrain3Rotation == 3:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 4
                    blueTrain3Turns = 10
            if blueTrain3Turns == 10:
                blueTrain3Y -= .25
            if blueTrain3X == 530 and blueTrain3Y == 320:
                blueTrain3Turns = 11
            if blueTrain3Turns == 11:
                if blueTrain3Rotation == 4:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 5
                    blueTrain3Turns = 12
            if blueTrain3Turns == 12:
                blueTrain3X -= .25
            if blueTrain3Turns == 13:
                if blueTrain3Rotation == 3:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 6
                    blueTrain3Turns = 14
            if blueTrain3Turns == 14:
                blueTrain3Y += .25
            if blueTrain3Y == 432 and blueTrain3X == 470:
                blueTrain3Turns = 15
            if blueTrain3Turns == 15:
                if blueTrain3Rotation == 6:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 7
                    blueTrain3Turns = 16
            if blueTrain3Turns == 16:
                blueTrain3X -= .25

            #Third track
            if blueTrain3Y == 432 and blueTrain3X == 255:
                if track3Visible == 1:
                    blueTrain3Turns = 17
                else:
                    blueTrain3Turns = 21

            #going to yellow station
            if blueTrain3Turns == 17:
                blueTrain3X -= .25
            if blueTrain3Y == 432 and blueTrain3X == 18:
                blueTrain3Turns = 18
            if blueTrain3Turns == 18:
                if blueTrain3Rotation == 7:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 8
                    blueTrain3Turns = 19
            if blueTrain3Turns == 19:
                blueTrain3Y -= .25
            if blueTrain3Y == 335 and blueTrain3X == 18:
                if blueTrain3Rotation == 8:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 9
                    blueTrain3Turns = 20
            if blueTrain3Turns == 20:
                blueTrain3X += .25

            #going to purple station
            if blueTrain3Turns == 21:
                if blueTrain3Rotation == 7:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 10
                    blueTrain3Turns = 22
            if blueTrain3Turns == 22:
                blueTrain3Y -= .25

            if blueTrain3Turns == 23:
                if blueTrain3Rotation == 1:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 11
                    blueTrain3Turns = 24
            if blueTrain3Turns == 24:
                blueTrain3Y -= .25

            #fourth track
            if blueTrain3X == 493 and blueTrain3Y == 178:
                if track4Visible == 1:
                    blueTrain3Turns = 29
                else:
                    blueTrain3Turns = 25

            #going to green station
            if blueTrain3Turns == 25:
                if blueTrain3Rotation == 11:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 12
                    blueTrain3Turns = 26
            if blueTrain3Turns == 26:
                blueTrain3X -= .25
            if blueTrain3X == 335 and blueTrain3Y == 178:
                if blueTrain3Rotation == 12:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 13
                    blueTrain3Turns = 27
            if blueTrain3Turns == 27:
                blueTrain3Y -= .25
            if blueTrain3X == 335 and blueTrain3Y == 100:
                if blueTrain3Rotation == 13:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 14
                    blueTrain3Turns = 28
            if blueTrain3Turns == 28:
                blueTrain3X += .25

            if blueTrain3Turns == 29:
                blueTrain3Y -= .25
            if blueTrain3X == 493 and blueTrain3Y == 27:
                if blueTrain3Rotation == 11:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 15
                    blueTrain3Turns = 30
            if blueTrain3Turns == 30:
                blueTrain3X -= .25

            #fifth track
            if blueTrain3X == 165 and blueTrain3Y == 27:
                if track5Visible == 1:
                    blueTrain3Turns = 31
                else:
                    blueTrain3Turns = 32

            #going to red station
            if blueTrain3Turns == 31:
                blueTrain3X -= .25

            #going to blue station
            if blueTrain3Turns == 32:
                if blueTrain3Rotation == 15:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
                    blueTrain3Rotation = 16
                    blueTrain3Turns = 33
            if blueTrain3Turns == 33:
                blueTrain3Y += .25
            if blueTrain3X == 165 and blueTrain3Y == 257:
                if blueTrain3Rotation == 16:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 17
                    blueTrain3Turns = 34
            if blueTrain3Turns == 34:
                blueTrain3X -= .25
            if blueTrain3X == 71 and blueTrain3Y == 257:
                if blueTrain3Rotation == 17:
                    blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
                    blueTrain3Rotation = 18
                    blueTrain3Turns = 35
            if blueTrain3Turns == 35:
                blueTrain3Y -= .25


        if blueTrainNum4 == 1:
            screen.blit(blueTrain4,[blueTrain4X,blueTrain4Y])
            if blueTrain4Turns == 0:
                blueTrain4Y -= .25
            if blueTrain4Y == 270 and blueTrain4X == 578:
                blueTrain4Turns = 1
            if blueTrain4Turns == 1:
                if blueTrain4Rotation == 0:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 1
                    blueTrain4Turns = 2
            if blueTrain4Turns == 2:
                blueTrain4X -= .25

            #first track
            if blueTrain4Y == 270 and blueTrain4X == 493:
                if track1Visible == 1:
                    blueTrain4Turns = 3
                else:
                    blueTrain4Turns = 23
            if blueTrain4Turns == 3:
                blueTrain4X -= .25
            if blueTrain4X == 329 and blueTrain4Y == 270:
                blueTrain4Turns = 4
            if blueTrain4Turns == 4:
                if blueTrain4Rotation == 1:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 2
                    blueTrain4Turns = 5
            if blueTrain4Turns == 5:
                blueTrain4Y += .25
            if blueTrain4X == 329 and blueTrain4Y == 370:
                blueTrain4Turns = 6
            if blueTrain4Turns == 6:
                if blueTrain4Rotation == 2:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 3
                    blueTrain4Turns = 7
            if blueTrain4Turns == 7:
                blueTrain4X += .25

            #second track
            if blueTrain4X == 470 and blueTrain4Y == 370:
                if track2Visible == 1:
                    blueTrain4Turns = 8
                else:
                    blueTrain4Turns = 13

            #going to orange station
            if blueTrain4Turns == 8:
                blueTrain4X += .25
            if blueTrain4X == 530 and blueTrain4Y == 370:
                blueTrain4Turns = 9
            if blueTrain4Turns == 9:
                if blueTrain4Rotation == 3:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 4
                    blueTrain4Turns = 10
            if blueTrain4Turns == 10:
                blueTrain4Y -= .25
            if blueTrain4X == 530 and blueTrain4Y == 320:
                blueTrain4Turns = 11
            if blueTrain4Turns == 11:
                if blueTrain4Rotation == 4:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 5
                    blueTrain4Turns = 12
            if blueTrain4Turns == 12:
                blueTrain4X -= .25
            if blueTrain4Turns == 13:
                if blueTrain4Rotation == 3:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 6
                    blueTrain4Turns = 14
            if blueTrain4Turns == 14:
                blueTrain4Y += .25
            if blueTrain4Y == 432 and blueTrain4X == 470:
                blueTrain4Turns = 15
            if blueTrain4Turns == 15:
                if blueTrain4Rotation == 6:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 7
                    blueTrain4Turns = 16
            if blueTrain4Turns == 16:
                blueTrain4X -= .25

            #Third track
            if blueTrain4Y == 432 and blueTrain4X == 255:
                if track3Visible == 1:
                    blueTrain4Turns = 17
                else:
                    blueTrain4Turns = 21

            #going to yellow station
            if blueTrain4Turns == 17:
                blueTrain4X -= .25
            if blueTrain4Y == 432 and blueTrain4X == 18:
                blueTrain4Turns = 18
            if blueTrain4Turns == 18:
                if blueTrain4Rotation == 7:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 8
                    blueTrain4Turns = 19
            if blueTrain4Turns == 19:
                blueTrain4Y -= .25
            if blueTrain4Y == 335 and blueTrain4X == 18:
                if blueTrain4Rotation == 8:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 9
                    blueTrain4Turns = 20
            if blueTrain4Turns == 20:
                blueTrain4X += .25

            #going to purple station
            if blueTrain4Turns == 21:
                if blueTrain4Rotation == 7:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 10
                    blueTrain4Turns = 22
            if blueTrain4Turns == 22:
                blueTrain4Y -= .25

            if blueTrain4Turns == 23:
                if blueTrain4Rotation == 1:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 11
                    blueTrain4Turns = 24
            if blueTrain4Turns == 24:
                blueTrain4Y -= .25

            #fourth track
            if blueTrain4X == 493 and blueTrain4Y == 178:
                if track4Visible == 1:
                    blueTrain4Turns = 29
                else:
                    blueTrain4Turns = 25

            #going to green station
            if blueTrain4Turns == 25:
                if blueTrain4Rotation == 11:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 12
                    blueTrain4Turns = 26
            if blueTrain4Turns == 26:
                blueTrain4X -= .25
            if blueTrain4X == 335 and blueTrain4Y == 178:
                if blueTrain4Rotation == 12:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 13
                    blueTrain4Turns = 27
            if blueTrain4Turns == 27:
                blueTrain4Y -= .25
            if blueTrain4X == 335 and blueTrain4Y == 100:
                if blueTrain4Rotation == 13:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 14
                    blueTrain4Turns = 28
            if blueTrain4Turns == 28:
                blueTrain4X += .25

            if blueTrain4Turns == 29:
                blueTrain4Y -= .25
            if blueTrain4X == 493 and blueTrain4Y == 27:
                if blueTrain4Rotation == 11:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 15
                    blueTrain4Turns = 30
            if blueTrain4Turns == 30:
                blueTrain4X -= .25

            #fifth track
            if blueTrain4X == 165 and blueTrain4Y == 27:
                if track5Visible == 1:
                    blueTrain4Turns = 31
                else:
                    blueTrain4Turns = 32

            #going to red station
            if blueTrain4Turns == 31:
                blueTrain4X -= .25

            #going to blue station
            if blueTrain4Turns == 32:
                if blueTrain4Rotation == 15:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
                    blueTrain4Rotation = 16
                    blueTrain4Turns = 33
            if blueTrain4Turns == 33:
                blueTrain4Y += .25
            if blueTrain4X == 165 and blueTrain4Y == 257:
                if blueTrain4Rotation == 16:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 17
                    blueTrain4Turns = 34
            if blueTrain4Turns == 34:
                blueTrain4X -= .25
            if blueTrain4X == 71 and blueTrain4Y == 257:
                if blueTrain4Rotation == 17:
                    blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
                    blueTrain4Rotation = 18
                    blueTrain4Turns = 35
            if blueTrain4Turns == 35:
                blueTrain4Y -= .25



        if purpleTrainNum0 == 1:
            screen.blit(purpleTrain,[purpleTrainX,purpleTrainY])
            if purpleTrainTurns == 0:
                purpleTrainY -= .25
            if purpleTrainY == 270 and purpleTrainX == 578:
                purpleTrainTurns = 1
            if purpleTrainTurns == 1:
                if purpleTrainRotation == 0:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 1
                    purpleTrainTurns = 2
            if purpleTrainTurns == 2:
                purpleTrainX -= .25

            #first track
            if purpleTrainY == 270 and purpleTrainX == 493:
                if track1Visible == 1:
                    purpleTrainTurns = 3
                else:
                    purpleTrainTurns = 23
            if purpleTrainTurns == 3:
                purpleTrainX -= .25
            if purpleTrainX == 329 and purpleTrainY == 270:
                purpleTrainTurns = 4
            if purpleTrainTurns == 4:
                if purpleTrainRotation == 1:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 2
                    purpleTrainTurns = 5
            if purpleTrainTurns == 5:
                purpleTrainY += .25
            if purpleTrainX == 329 and purpleTrainY == 370:
                purpleTrainTurns = 6
            if purpleTrainTurns == 6:
                if purpleTrainRotation == 2:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 3
                    purpleTrainTurns = 7
            if purpleTrainTurns == 7:
                purpleTrainX += .25

            #second track
            if purpleTrainX == 470 and purpleTrainY == 370:
                if track2Visible == 1:
                    purpleTrainTurns = 8
                else:
                    purpleTrainTurns = 13

            #going to orange station
            if purpleTrainTurns == 8:
                purpleTrainX += .25
            if purpleTrainX == 530 and purpleTrainY == 370:
                purpleTrainTurns = 9
            if purpleTrainTurns == 9:
                if purpleTrainRotation == 3:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 4
                    purpleTrainTurns = 10
            if purpleTrainTurns == 10:
                purpleTrainY -= .25
            if purpleTrainX == 530 and purpleTrainY == 320:
                purpleTrainTurns = 11
            if purpleTrainTurns == 11:
                if purpleTrainRotation == 4:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 5
                    purpleTrainTurns = 12
            if purpleTrainTurns == 12:
                purpleTrainX -= .25
            if purpleTrainTurns == 13:
                if purpleTrainRotation == 3:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 6
                    purpleTrainTurns = 14
            if purpleTrainTurns == 14:
                purpleTrainY += .25
            if purpleTrainY == 432 and purpleTrainX == 470:
                purpleTrainTurns = 15
            if purpleTrainTurns == 15:
                if purpleTrainRotation == 6:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 7
                    purpleTrainTurns = 16
            if purpleTrainTurns == 16:
                purpleTrainX -= .25

            #Third track
            if purpleTrainY == 432 and purpleTrainX == 255:
                if track3Visible == 1:
                    purpleTrainTurns = 17
                else:
                    purpleTrainTurns = 21

            #going to yellow station
            if purpleTrainTurns == 17:
                purpleTrainX -= .25
            if purpleTrainY == 432 and purpleTrainX == 18:
                purpleTrainTurns = 18
            if purpleTrainTurns == 18:
                if purpleTrainRotation == 7:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 8
                    purpleTrainTurns = 19
            if purpleTrainTurns == 19:
                purpleTrainY -= .25
            if purpleTrainY == 335 and purpleTrainX == 18:
                if purpleTrainRotation == 8:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 9
                    purpleTrainTurns = 20
            if purpleTrainTurns == 20:
                purpleTrainX += .25

            #going to purple station
            if purpleTrainTurns == 21:
                if purpleTrainRotation == 7:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 10
                    purpleTrainTurns = 22
            if purpleTrainTurns == 22:
                purpleTrainY -= .25

            if purpleTrainTurns == 23:
                if purpleTrainRotation == 1:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 11
                    purpleTrainTurns = 24
            if purpleTrainTurns == 24:
                purpleTrainY -= .25

            #fourth track
            if purpleTrainX == 493 and purpleTrainY == 178:
                if track4Visible == 1:
                    purpleTrainTurns = 29
                else:
                    purpleTrainTurns = 25

            #going to green station
            if purpleTrainTurns == 25:
                if purpleTrainRotation == 11:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 12
                    purpleTrainTurns = 26
            if purpleTrainTurns == 26:
                purpleTrainX -= .25
            if purpleTrainX == 335 and purpleTrainY == 178:
                if purpleTrainRotation == 12:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 13
                    purpleTrainTurns = 27
            if purpleTrainTurns == 27:
                purpleTrainY -= .25
            if purpleTrainX == 335 and purpleTrainY == 100:
                if purpleTrainRotation == 13:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 14
                    purpleTrainTurns = 28
            if purpleTrainTurns == 28:
                purpleTrainX += .25

            if purpleTrainTurns == 29:
                purpleTrainY -= .25
            if purpleTrainX == 493 and purpleTrainY == 27:
                if purpleTrainRotation == 11:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 15
                    purpleTrainTurns = 30
            if purpleTrainTurns == 30:
                purpleTrainX -= .25

            #fifth track
            if purpleTrainX == 165 and purpleTrainY == 27:
                if track5Visible == 1:
                    purpleTrainTurns = 31
                else:
                    purpleTrainTurns = 32

            #going to red station
            if purpleTrainTurns == 31:
                purpleTrainX -= .25

            #going to blue station
            if purpleTrainTurns == 32:
                if purpleTrainRotation == 15:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 90)
                    purpleTrainRotation = 16
                    purpleTrainTurns = 33
            if purpleTrainTurns == 33:
                purpleTrainY += .25
            if purpleTrainX == 165 and purpleTrainY == 257:
                if purpleTrainRotation == 16:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 17
                    purpleTrainTurns = 34
            if purpleTrainTurns == 34:
                purpleTrainX -= .25
            if purpleTrainX == 71 and purpleTrainY == 257:
                if purpleTrainRotation == 17:
                    purpleTrain = pygame.transform.rotate(purpleTrain, 270)
                    purpleTrainRotation = 18
                    purpleTrainTurns = 35
            if purpleTrainTurns == 35:
                purpleTrainY -= .25

        if purpleTrainNum1 == 1:
            screen.blit(purpleTrain1,[purpleTrain1X,purpleTrain1Y])
            if purpleTrain1Turns == 0:
                purpleTrain1Y -= .25
            if purpleTrain1Y == 270 and purpleTrain1X == 578:
                purpleTrain1Turns = 1
            if purpleTrain1Turns == 1:
                if purpleTrain1Rotation == 0:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 1
                    purpleTrain1Turns = 2
            if purpleTrain1Turns == 2:
                purpleTrain1X -= .25

            #first track
            if purpleTrain1Y == 270 and purpleTrain1X == 493:
                if track1Visible == 1:
                    purpleTrain1Turns = 3
                else:
                    purpleTrain1Turns = 23
            if purpleTrain1Turns == 3:
                purpleTrain1X -= .25
            if purpleTrain1X == 329 and purpleTrain1Y == 270:
                purpleTrain1Turns = 4
            if purpleTrain1Turns == 4:
                if purpleTrain1Rotation == 1:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 2
                    purpleTrain1Turns = 5
            if purpleTrain1Turns == 5:
                purpleTrain1Y += .25
            if purpleTrain1X == 329 and purpleTrain1Y == 370:
                purpleTrain1Turns = 6
            if purpleTrain1Turns == 6:
                if purpleTrain1Rotation == 2:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 3
                    purpleTrain1Turns = 7
            if purpleTrain1Turns == 7:
                purpleTrain1X += .25

            #second track
            if purpleTrain1X == 470 and purpleTrain1Y == 370:
                if track2Visible == 1:
                    purpleTrain1Turns = 8
                else:
                    purpleTrain1Turns = 13

            #going to orange station
            if purpleTrain1Turns == 8:
                purpleTrain1X += .25
            if purpleTrain1X == 530 and purpleTrain1Y == 370:
                purpleTrain1Turns = 9
            if purpleTrain1Turns == 9:
                if purpleTrain1Rotation == 3:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 4
                    purpleTrain1Turns = 10
            if purpleTrain1Turns == 10:
                purpleTrain1Y -= .25
            if purpleTrain1X == 530 and purpleTrain1Y == 320:
                purpleTrain1Turns = 11
            if purpleTrain1Turns == 11:
                if purpleTrain1Rotation == 4:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 5
                    purpleTrain1Turns = 12
            if purpleTrain1Turns == 12:
                purpleTrain1X -= .25
            if purpleTrain1Turns == 13:
                if purpleTrain1Rotation == 3:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 6
                    purpleTrain1Turns = 14
            if purpleTrain1Turns == 14:
                purpleTrain1Y += .25
            if purpleTrain1Y == 432 and purpleTrain1X == 470:
                purpleTrain1Turns = 15
            if purpleTrain1Turns == 15:
                if purpleTrain1Rotation == 6:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 7
                    purpleTrain1Turns = 16
            if purpleTrain1Turns == 16:
                purpleTrain1X -= .25

            #Third track
            if purpleTrain1Y == 432 and purpleTrain1X == 255:
                if track3Visible == 1:
                    purpleTrain1Turns = 17
                else:
                    purpleTrain1Turns = 21

            #going to yellow station
            if purpleTrain1Turns == 17:
                purpleTrain1X -= .25
            if purpleTrain1Y == 432 and purpleTrain1X == 18:
                purpleTrain1Turns = 18
            if purpleTrain1Turns == 18:
                if purpleTrain1Rotation == 7:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 8
                    purpleTrain1Turns = 19
            if purpleTrain1Turns == 19:
                purpleTrain1Y -= .25
            if purpleTrain1Y == 335 and purpleTrain1X == 18:
                if purpleTrain1Rotation == 8:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 9
                    purpleTrain1Turns = 20
            if purpleTrain1Turns == 20:
                purpleTrain1X += .25

            #going to purple station
            if purpleTrain1Turns == 21:
                if purpleTrain1Rotation == 7:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 10
                    purpleTrain1Turns = 22
            if purpleTrain1Turns == 22:
                purpleTrain1Y -= .25

            if purpleTrain1Turns == 23:
                if purpleTrain1Rotation == 1:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 11
                    purpleTrain1Turns = 24
            if purpleTrain1Turns == 24:
                purpleTrain1Y -= .25

            #fourth track
            if purpleTrain1X == 493 and purpleTrain1Y == 178:
                if track4Visible == 1:
                    purpleTrain1Turns = 29
                else:
                    purpleTrain1Turns = 25

            #going to green station
            if purpleTrain1Turns == 25:
                if purpleTrain1Rotation == 11:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 12
                    purpleTrain1Turns = 26
            if purpleTrain1Turns == 26:
                purpleTrain1X -= .25
            if purpleTrain1X == 335 and purpleTrain1Y == 178:
                if purpleTrain1Rotation == 12:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 13
                    purpleTrain1Turns = 27
            if purpleTrain1Turns == 27:
                purpleTrain1Y -= .25
            if purpleTrain1X == 335 and purpleTrain1Y == 100:
                if purpleTrain1Rotation == 13:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 14
                    purpleTrain1Turns = 28
            if purpleTrain1Turns == 28:
                purpleTrain1X += .25

            if purpleTrain1Turns == 29:
                purpleTrain1Y -= .25
            if purpleTrain1X == 493 and purpleTrain1Y == 27:
                if purpleTrain1Rotation == 11:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 15
                    purpleTrain1Turns = 30
            if purpleTrain1Turns == 30:
                purpleTrain1X -= .25

            #fifth track
            if purpleTrain1X == 165 and purpleTrain1Y == 27:
                if track5Visible == 1:
                    purpleTrain1Turns = 31
                else:
                    purpleTrain1Turns = 32

            #going to red station
            if purpleTrain1Turns == 31:
                purpleTrain1X -= .25

            #going to blue station
            if purpleTrain1Turns == 32:
                if purpleTrain1Rotation == 15:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
                    purpleTrain1Rotation = 16
                    purpleTrain1Turns = 33
            if purpleTrain1Turns == 33:
                purpleTrain1Y += .25
            if purpleTrain1X == 165 and purpleTrain1Y == 257:
                if purpleTrain1Rotation == 16:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 17
                    purpleTrain1Turns = 34
            if purpleTrain1Turns == 34:
                purpleTrain1X -= .25
            if purpleTrain1X == 71 and purpleTrain1Y == 257:
                if purpleTrain1Rotation == 17:
                    purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
                    purpleTrain1Rotation = 18
                    purpleTrain1Turns = 35
            if purpleTrain1Turns == 35:
                purpleTrain1Y -= .25


        if purpleTrainNum2 == 1:
            screen.blit(purpleTrain2,[purpleTrain2X,purpleTrain2Y])
            if purpleTrain2Turns == 0:
                purpleTrain2Y -= .25
            if purpleTrain2Y == 270 and purpleTrain2X == 578:
                purpleTrain2Turns = 1
            if purpleTrain2Turns == 1:
                if purpleTrain2Rotation == 0:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 1
                    purpleTrain2Turns = 2
            if purpleTrain2Turns == 2:
                purpleTrain2X -= .25

            #first track
            if purpleTrain2Y == 270 and purpleTrain2X == 493:
                if track1Visible == 1:
                    purpleTrain2Turns = 3
                else:
                    purpleTrain2Turns = 23
            if purpleTrain2Turns == 3:
                purpleTrain2X -= .25
            if purpleTrain2X == 329 and purpleTrain2Y == 270:
                purpleTrain2Turns = 4
            if purpleTrain2Turns == 4:
                if purpleTrain2Rotation == 1:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 2
                    purpleTrain2Turns = 5
            if purpleTrain2Turns == 5:
                purpleTrain2Y += .25
            if purpleTrain2X == 329 and purpleTrain2Y == 370:
                purpleTrain2Turns = 6
            if purpleTrain2Turns == 6:
                if purpleTrain2Rotation == 2:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 3
                    purpleTrain2Turns = 7
            if purpleTrain2Turns == 7:
                purpleTrain2X += .25

            #second track
            if purpleTrain2X == 470 and purpleTrain2Y == 370:
                if track2Visible == 1:
                    purpleTrain2Turns = 8
                else:
                    purpleTrain2Turns = 13

            #going to orange station
            if purpleTrain2Turns == 8:
                purpleTrain2X += .25
            if purpleTrain2X == 530 and purpleTrain2Y == 370:
                purpleTrain2Turns = 9
            if purpleTrain2Turns == 9:
                if purpleTrain2Rotation == 3:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 4
                    purpleTrain2Turns = 10
            if purpleTrain2Turns == 10:
                purpleTrain2Y -= .25
            if purpleTrain2X == 530 and purpleTrain2Y == 320:
                purpleTrain2Turns = 11
            if purpleTrain2Turns == 11:
                if purpleTrain2Rotation == 4:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 5
                    purpleTrain2Turns = 12
            if purpleTrain2Turns == 12:
                purpleTrain2X -= .25
            if purpleTrain2Turns == 13:
                if purpleTrain2Rotation == 3:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 6
                    purpleTrain2Turns = 14
            if purpleTrain2Turns == 14:
                purpleTrain2Y += .25
            if purpleTrain2Y == 432 and purpleTrain2X == 470:
                purpleTrain2Turns = 15
            if purpleTrain2Turns == 15:
                if purpleTrain2Rotation == 6:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 7
                    purpleTrain2Turns = 16
            if purpleTrain2Turns == 16:
                purpleTrain2X -= .25

            #Third track
            if purpleTrain2Y == 432 and purpleTrain2X == 255:
                if track3Visible == 1:
                    purpleTrain2Turns = 17
                else:
                    purpleTrain2Turns = 21

            #going to yellow station
            if purpleTrain2Turns == 17:
                purpleTrain2X -= .25
            if purpleTrain2Y == 432 and purpleTrain2X == 18:
                purpleTrain2Turns = 18
            if purpleTrain2Turns == 18:
                if purpleTrain2Rotation == 7:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 8
                    purpleTrain2Turns = 19
            if purpleTrain2Turns == 19:
                purpleTrain2Y -= .25
            if purpleTrain2Y == 335 and purpleTrain2X == 18:
                if purpleTrain2Rotation == 8:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 9
                    purpleTrain2Turns = 20
            if purpleTrain2Turns == 20:
                purpleTrain2X += .25

            #going to purple station
            if purpleTrain2Turns == 21:
                if purpleTrain2Rotation == 7:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 10
                    purpleTrain2Turns = 22
            if purpleTrain2Turns == 22:
                purpleTrain2Y -= .25

            if purpleTrain2Turns == 23:
                if purpleTrain2Rotation == 1:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 11
                    purpleTrain2Turns = 24
            if purpleTrain2Turns == 24:
                purpleTrain2Y -= .25

            #fourth track
            if purpleTrain2X == 493 and purpleTrain2Y == 178:
                if track4Visible == 1:
                    purpleTrain2Turns = 29
                else:
                    purpleTrain2Turns = 25

            #going to green station
            if purpleTrain2Turns == 25:
                if purpleTrain2Rotation == 11:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 12
                    purpleTrain2Turns = 26
            if purpleTrain2Turns == 26:
                purpleTrain2X -= .25
            if purpleTrain2X == 335 and purpleTrain2Y == 178:
                if purpleTrain2Rotation == 12:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 13
                    purpleTrain2Turns = 27
            if purpleTrain2Turns == 27:
                purpleTrain2Y -= .25
            if purpleTrain2X == 335 and purpleTrain2Y == 100:
                if purpleTrain2Rotation == 13:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 14
                    purpleTrain2Turns = 28
            if purpleTrain2Turns == 28:
                purpleTrain2X += .25

            if purpleTrain2Turns == 29:
                purpleTrain2Y -= .25
            if purpleTrain2X == 493 and purpleTrain2Y == 27:
                if purpleTrain2Rotation == 11:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 15
                    purpleTrain2Turns = 30
            if purpleTrain2Turns == 30:
                purpleTrain2X -= .25

            #fifth track
            if purpleTrain2X == 165 and purpleTrain2Y == 27:
                if track5Visible == 1:
                    purpleTrain2Turns = 31
                else:
                    purpleTrain2Turns = 32

            #going to red station
            if purpleTrain2Turns == 31:
                purpleTrain2X -= .25

            #going to blue station
            if purpleTrain2Turns == 32:
                if purpleTrain2Rotation == 15:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
                    purpleTrain2Rotation = 16
                    purpleTrain2Turns = 33
            if purpleTrain2Turns == 33:
                purpleTrain2Y += .25
            if purpleTrain2X == 165 and purpleTrain2Y == 257:
                if purpleTrain2Rotation == 16:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 17
                    purpleTrain2Turns = 34
            if purpleTrain2Turns == 34:
                purpleTrain2X -= .25
            if purpleTrain2X == 71 and purpleTrain2Y == 257:
                if purpleTrain2Rotation == 17:
                    purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
                    purpleTrain2Rotation = 18
                    purpleTrain2Turns = 35
            if purpleTrain2Turns == 35:
                purpleTrain2Y -= .25

        if purpleTrainNum3 == 1:
            screen.blit(purpleTrain3,[purpleTrain3X,purpleTrain3Y])
            if purpleTrain3Turns == 0:
                purpleTrain3Y -= .25
            if purpleTrain3Y == 270 and purpleTrain3X == 578:
                purpleTrain3Turns = 1
            if purpleTrain3Turns == 1:
                if purpleTrain3Rotation == 0:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 1
                    purpleTrain3Turns = 2
            if purpleTrain3Turns == 2:
                purpleTrain3X -= .25

            #first track
            if purpleTrain3Y == 270 and purpleTrain3X == 493:
                if track1Visible == 1:
                    purpleTrain3Turns = 3
                else:
                    purpleTrain3Turns = 23
            if purpleTrain3Turns == 3:
                purpleTrain3X -= .25
            if purpleTrain3X == 329 and purpleTrain3Y == 270:
                purpleTrain3Turns = 4
            if purpleTrain3Turns == 4:
                if purpleTrain3Rotation == 1:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 2
                    purpleTrain3Turns = 5
            if purpleTrain3Turns == 5:
                purpleTrain3Y += .25
            if purpleTrain3X == 329 and purpleTrain3Y == 370:
                purpleTrain3Turns = 6
            if purpleTrain3Turns == 6:
                if purpleTrain3Rotation == 2:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 3
                    purpleTrain3Turns = 7
            if purpleTrain3Turns == 7:
                purpleTrain3X += .25

            #second track
            if purpleTrain3X == 470 and purpleTrain3Y == 370:
                if track2Visible == 1:
                    purpleTrain3Turns = 8
                else:
                    purpleTrain3Turns = 13

            #going to orange station
            if purpleTrain3Turns == 8:
                purpleTrain3X += .25
            if purpleTrain3X == 530 and purpleTrain3Y == 370:
                purpleTrain3Turns = 9
            if purpleTrain3Turns == 9:
                if purpleTrain3Rotation == 3:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 4
                    purpleTrain3Turns = 10
            if purpleTrain3Turns == 10:
                purpleTrain3Y -= .25
            if purpleTrain3X == 530 and purpleTrain3Y == 320:
                purpleTrain3Turns = 11
            if purpleTrain3Turns == 11:
                if purpleTrain3Rotation == 4:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 5
                    purpleTrain3Turns = 12
            if purpleTrain3Turns == 12:
                purpleTrain3X -= .25
            if purpleTrain3Turns == 13:
                if purpleTrain3Rotation == 3:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 6
                    purpleTrain3Turns = 14
            if purpleTrain3Turns == 14:
                purpleTrain3Y += .25
            if purpleTrain3Y == 432 and purpleTrain3X == 470:
                purpleTrain3Turns = 15
            if purpleTrain3Turns == 15:
                if purpleTrain3Rotation == 6:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 7
                    purpleTrain3Turns = 16
            if purpleTrain3Turns == 16:
                purpleTrain3X -= .25

            #Third track
            if purpleTrain3Y == 432 and purpleTrain3X == 255:
                if track3Visible == 1:
                    purpleTrain3Turns = 17
                else:
                    purpleTrain3Turns = 21

            #going to yellow station
            if purpleTrain3Turns == 17:
                purpleTrain3X -= .25
            if purpleTrain3Y == 432 and purpleTrain3X == 18:
                purpleTrain3Turns = 18
            if purpleTrain3Turns == 18:
                if purpleTrain3Rotation == 7:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 8
                    purpleTrain3Turns = 19
            if purpleTrain3Turns == 19:
                purpleTrain3Y -= .25
            if purpleTrain3Y == 335 and purpleTrain3X == 18:
                if purpleTrain3Rotation == 8:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 9
                    purpleTrain3Turns = 20
            if purpleTrain3Turns == 20:
                purpleTrain3X += .25

            #going to purple station
            if purpleTrain3Turns == 21:
                if purpleTrain3Rotation == 7:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 10
                    purpleTrain3Turns = 22
            if purpleTrain3Turns == 22:
                purpleTrain3Y -= .25

            if purpleTrain3Turns == 23:
                if purpleTrain3Rotation == 1:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 11
                    purpleTrain3Turns = 24
            if purpleTrain3Turns == 24:
                purpleTrain3Y -= .25

            #fourth track
            if purpleTrain3X == 493 and purpleTrain3Y == 178:
                if track4Visible == 1:
                    purpleTrain3Turns = 29
                else:
                    purpleTrain3Turns = 25

            #going to green station
            if purpleTrain3Turns == 25:
                if purpleTrain3Rotation == 11:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 12
                    purpleTrain3Turns = 26
            if purpleTrain3Turns == 26:
                purpleTrain3X -= .25
            if purpleTrain3X == 335 and purpleTrain3Y == 178:
                if purpleTrain3Rotation == 12:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 13
                    purpleTrain3Turns = 27
            if purpleTrain3Turns == 27:
                purpleTrain3Y -= .25
            if purpleTrain3X == 335 and purpleTrain3Y == 100:
                if purpleTrain3Rotation == 13:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 14
                    purpleTrain3Turns = 28
            if purpleTrain3Turns == 28:
                purpleTrain3X += .25

            if purpleTrain3Turns == 29:
                purpleTrain3Y -= .25
            if purpleTrain3X == 493 and purpleTrain3Y == 27:
                if purpleTrain3Rotation == 11:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 15
                    purpleTrain3Turns = 30
            if purpleTrain3Turns == 30:
                purpleTrain3X -= .25

            #fifth track
            if purpleTrain3X == 165 and purpleTrain3Y == 27:
                if track5Visible == 1:
                    purpleTrain3Turns = 31
                else:
                    purpleTrain3Turns = 32

            #going to red station
            if purpleTrain3Turns == 31:
                purpleTrain3X -= .25

            #going to blue station
            if purpleTrain3Turns == 32:
                if purpleTrain3Rotation == 15:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
                    purpleTrain3Rotation = 16
                    purpleTrain3Turns = 33
            if purpleTrain3Turns == 33:
                purpleTrain3Y += .25
            if purpleTrain3X == 165 and purpleTrain3Y == 257:
                if purpleTrain3Rotation == 16:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 17
                    purpleTrain3Turns = 34
            if purpleTrain3Turns == 34:
                purpleTrain3X -= .25
            if purpleTrain3X == 71 and purpleTrain3Y == 257:
                if purpleTrain3Rotation == 17:
                    purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
                    purpleTrain3Rotation = 18
                    purpleTrain3Turns = 35
            if purpleTrain3Turns == 35:
                purpleTrain3Y -= .25


        if purpleTrainNum4 == 1:
            screen.blit(purpleTrain4,[purpleTrain4X,purpleTrain4Y])
            if purpleTrain4Turns == 0:
                purpleTrain4Y -= .25
            if purpleTrain4Y == 270 and purpleTrain4X == 578:
                purpleTrain4Turns = 1
            if purpleTrain4Turns == 1:
                if purpleTrain4Rotation == 0:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 1
                    purpleTrain4Turns = 2
            if purpleTrain4Turns == 2:
                purpleTrain4X -= .25

            #first track
            if purpleTrain4Y == 270 and purpleTrain4X == 493:
                if track1Visible == 1:
                    purpleTrain4Turns = 3
                else:
                    purpleTrain4Turns = 23
            if purpleTrain4Turns == 3:
                purpleTrain4X -= .25
            if purpleTrain4X == 329 and purpleTrain4Y == 270:
                purpleTrain4Turns = 4
            if purpleTrain4Turns == 4:
                if purpleTrain4Rotation == 1:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 2
                    purpleTrain4Turns = 5
            if purpleTrain4Turns == 5:
                purpleTrain4Y += .25
            if purpleTrain4X == 329 and purpleTrain4Y == 370:
                purpleTrain4Turns = 6
            if purpleTrain4Turns == 6:
                if purpleTrain4Rotation == 2:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 3
                    purpleTrain4Turns = 7
            if purpleTrain4Turns == 7:
                purpleTrain4X += .25

            #second track
            if purpleTrain4X == 470 and purpleTrain4Y == 370:
                if track2Visible == 1:
                    purpleTrain4Turns = 8
                else:
                    purpleTrain4Turns = 13

            #going to orange station
            if purpleTrain4Turns == 8:
                purpleTrain4X += .25
            if purpleTrain4X == 530 and purpleTrain4Y == 370:
                purpleTrain4Turns = 9
            if purpleTrain4Turns == 9:
                if purpleTrain4Rotation == 3:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 4
                    purpleTrain4Turns = 10
            if purpleTrain4Turns == 10:
                purpleTrain4Y -= .25
            if purpleTrain4X == 530 and purpleTrain4Y == 320:
                purpleTrain4Turns = 11
            if purpleTrain4Turns == 11:
                if purpleTrain4Rotation == 4:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 5
                    purpleTrain4Turns = 12
            if purpleTrain4Turns == 12:
                purpleTrain4X -= .25
            if purpleTrain4Turns == 13:
                if purpleTrain4Rotation == 3:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 6
                    purpleTrain4Turns = 14
            if purpleTrain4Turns == 14:
                purpleTrain4Y += .25
            if purpleTrain4Y == 432 and purpleTrain4X == 470:
                purpleTrain4Turns = 15
            if purpleTrain4Turns == 15:
                if purpleTrain4Rotation == 6:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 7
                    purpleTrain4Turns = 16
            if purpleTrain4Turns == 16:
                purpleTrain4X -= .25

            #Third track
            if purpleTrain4Y == 432 and purpleTrain4X == 255:
                if track3Visible == 1:
                    purpleTrain4Turns = 17
                else:
                    purpleTrain4Turns = 21

            #going to yellow station
            if purpleTrain4Turns == 17:
                purpleTrain4X -= .25
            if purpleTrain4Y == 432 and purpleTrain4X == 18:
                purpleTrain4Turns = 18
            if purpleTrain4Turns == 18:
                if purpleTrain4Rotation == 7:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 8
                    purpleTrain4Turns = 19
            if purpleTrain4Turns == 19:
                purpleTrain4Y -= .25
            if purpleTrain4Y == 335 and purpleTrain4X == 18:
                if purpleTrain4Rotation == 8:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 9
                    purpleTrain4Turns = 20
            if purpleTrain4Turns == 20:
                purpleTrain4X += .25

            #going to purple station
            if purpleTrain4Turns == 21:
                if purpleTrain4Rotation == 7:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 10
                    purpleTrain4Turns = 22
            if purpleTrain4Turns == 22:
                purpleTrain4Y -= .25

            if purpleTrain4Turns == 23:
                if purpleTrain4Rotation == 1:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 11
                    purpleTrain4Turns = 24
            if purpleTrain4Turns == 24:
                purpleTrain4Y -= .25

            #fourth track
            if purpleTrain4X == 493 and purpleTrain4Y == 178:
                if track4Visible == 1:
                    purpleTrain4Turns = 29
                else:
                    purpleTrain4Turns = 25

            #going to green station
            if purpleTrain4Turns == 25:
                if purpleTrain4Rotation == 11:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 12
                    purpleTrain4Turns = 26
            if purpleTrain4Turns == 26:
                purpleTrain4X -= .25
            if purpleTrain4X == 335 and purpleTrain4Y == 178:
                if purpleTrain4Rotation == 12:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 13
                    purpleTrain4Turns = 27
            if purpleTrain4Turns == 27:
                purpleTrain4Y -= .25
            if purpleTrain4X == 335 and purpleTrain4Y == 100:
                if purpleTrain4Rotation == 13:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 14
                    purpleTrain4Turns = 28
            if purpleTrain4Turns == 28:
                purpleTrain4X += .25

            if purpleTrain4Turns == 29:
                purpleTrain4Y -= .25
            if purpleTrain4X == 493 and purpleTrain4Y == 27:
                if purpleTrain4Rotation == 11:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 15
                    purpleTrain4Turns = 30
            if purpleTrain4Turns == 30:
                purpleTrain4X -= .25

            #fifth track
            if purpleTrain4X == 165 and purpleTrain4Y == 27:
                if track5Visible == 1:
                    purpleTrain4Turns = 31
                else:
                    purpleTrain4Turns = 32

            #going to red station
            if purpleTrain4Turns == 31:
                purpleTrain4X -= .25

            #going to blue station
            if purpleTrain4Turns == 32:
                if purpleTrain4Rotation == 15:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
                    purpleTrain4Rotation = 16
                    purpleTrain4Turns = 33
            if purpleTrain4Turns == 33:
                purpleTrain4Y += .25
            if purpleTrain4X == 165 and purpleTrain4Y == 257:
                if purpleTrain4Rotation == 16:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 17
                    purpleTrain4Turns = 34
            if purpleTrain4Turns == 34:
                purpleTrain4X -= .25
            if purpleTrain4X == 71 and purpleTrain4Y == 257:
                if purpleTrain4Rotation == 17:
                    purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
                    purpleTrain4Rotation = 18
                    purpleTrain4Turns = 35
            if purpleTrain4Turns == 35:
                purpleTrain4Y -= .25


        #Checking if trains reach station and assigning points
        #Red Train
        #red station
        if redTrainCollider.colliderect(redStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            redTrain = pygame.transform.rotate(redTrain, 270)
            trainsBack += 1
        if redTrain1Collider.colliderect(redStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            redTrain1 = pygame.transform.rotate(redTrain1, 270)
            trainsBack += 1
        if redTrain2Collider.colliderect(redStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            redTrain2 = pygame.transform.rotate(redTrain2, 270)
            trainsBack += 1
        if redTrain3Collider.colliderect(redStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            redTrain3 = pygame.transform.rotate(redTrain3, 270)
            trainsBack += 1
        if redTrain4Collider.colliderect(redStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            redTrain4 = pygame.transform.rotate(redTrain4, 270)
            trainsBack += 1

            #orange station
        if redTrainCollider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            redTrain = pygame.transform.rotate(redTrain, 270)
            trainsBack += 1
        if redTrain1Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            redTrain1 = pygame.transform.rotate(redTrain1, 270)
            trainsBack += 1
        if redTrain2Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            redTrain2 = pygame.transform.rotate(redTrain2, 270)
            trainsBack += 1
        if redTrain3Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            redTrain3 = pygame.transform.rotate(redTrain3, 270)
            trainsBack += 1
        if redTrain4Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            redTrain4 = pygame.transform.rotate(redTrain4, 270)
            trainsBack += 1

            #Yellow station
        if redTrainCollider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            redTrain = pygame.transform.rotate(redTrain, 90)
            trainsBack += 1
        if redTrain1Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            redTrain1 = pygame.transform.rotate(redTrain1, 90)
            trainsBack += 1
        if redTrain2Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            redTrain2 = pygame.transform.rotate(redTrain2, 90)
            trainsBack += 1
        if redTrain3Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            redTrain3 = pygame.transform.rotate(redTrain3, 90)
            trainsBack += 1
        if redTrain4Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            redTrain4 = pygame.transform.rotate(redTrain4, 90)
            trainsBack += 1

            #Green station
        if redTrainCollider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            redTrain = pygame.transform.rotate(redTrain, 90)
            trainsBack += 1
        if redTrain1Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            redTrain1 = pygame.transform.rotate(redTrain1, 90)
            trainsBack += 1
        if redTrain2Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            redTrain2 = pygame.transform.rotate(redTrain2, 90)
            trainsBack += 1
        if redTrain3Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            redTrain3 = pygame.transform.rotate(redTrain3, 90)
            trainsBack += 1
        if redTrain4Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            redTrain4 = pygame.transform.rotate(redTrain4, 90)
            trainsBack += 1

            #blue station
        if redTrainCollider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            trainsBack += 1
        if redTrain1Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            trainsBack += 1
        if redTrain2Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            trainsBack += 1
        if redTrain3Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            trainsBack += 1
        if redTrain4Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if redTrainCollider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrainX = 578
            redTrainY = 500
            redTrainNum0 = 0
            redTrainTurns = 0
            redTrainRotation = 0
            trainsBack += 1
        if redTrain1Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain1X = 578
            redTrain1Y = 500
            redTrainNum1 = 0
            redTrain1Turns = 0
            redTrain1Rotation = 0
            trainsBack += 1
        if redTrain2Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain2X = 578
            redTrain2Y = 500
            redTrainNum2 = 0
            redTrain2Turns = 0
            redTrain2Rotation = 0
            trainsBack += 1
        if redTrain3Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain3X = 578
            redTrain3Y = 500
            redTrainNum3 = 0
            redTrain3Turns = 0
            redTrain3Rotation = 0
            trainsBack += 1
        if redTrain4Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            redTrain4X = 578
            redTrain4Y = 500
            redTrainNum4 = 0
            redTrain4Turns = 0
            redTrain4Rotation = 0
            trainsBack += 1

        #Orange Train
        #red station
        if orangeTrainCollider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            orangeTrain = pygame.transform.rotate(orangeTrain, 270)
            trainsBack += 1
        if orangeTrain1Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
            trainsBack += 1
        if orangeTrain2Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
            trainsBack += 1
        if orangeTrain3Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
            trainsBack += 1
        if orangeTrain4Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
            trainsBack += 1

            #orange station
        if orangeTrainCollider.colliderect(orangeStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            orangeTrain = pygame.transform.rotate(orangeTrain, 270)
            trainsBack += 1
        if orangeTrain1Collider.colliderect(orangeStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            orangeTrain1 = pygame.transform.rotate(orangeTrain1, 270)
            trainsBack += 1
        if orangeTrain2Collider.colliderect(orangeStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            orangeTrain2 = pygame.transform.rotate(orangeTrain2, 270)
            trainsBack += 1
        if orangeTrain3Collider.colliderect(orangeStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            orangeTrain3 = pygame.transform.rotate(orangeTrain3, 270)
            trainsBack += 1
        if orangeTrain4Collider.colliderect(orangeStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            orangeTrain4 = pygame.transform.rotate(orangeTrain4, 270)
            trainsBack += 1

            #Yellow station
        if orangeTrainCollider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            orangeTrain = pygame.transform.rotate(orangeTrain, 90)
            trainsBack += 1
        if orangeTrain1Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
            trainsBack += 1
        if orangeTrain2Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
            trainsBack += 1
        if orangeTrain3Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
            trainsBack += 1
        if orangeTrain4Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
            trainsBack += 1

            #Green station
        if orangeTrainCollider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            orangeTrain = pygame.transform.rotate(orangeTrain, 90)
            trainsBack += 1
        if orangeTrain1Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            orangeTrain1 = pygame.transform.rotate(orangeTrain1, 90)
            trainsBack += 1
        if orangeTrain2Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            orangeTrain2 = pygame.transform.rotate(orangeTrain2, 90)
            trainsBack += 1
        if orangeTrain3Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            orangeTrain3 = pygame.transform.rotate(orangeTrain3, 90)
            trainsBack += 1
        if orangeTrain4Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            orangeTrain4 = pygame.transform.rotate(orangeTrain4, 90)
            trainsBack += 1

            #blue station
        if orangeTrainCollider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            trainsBack += 1
        if orangeTrain1Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            trainsBack += 1
        if orangeTrain2Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            trainsBack += 1
        if orangeTrain3Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            trainsBack += 1
        if orangeTrain4Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if orangeTrainCollider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrainX = 578
            orangeTrainY = 500
            orangeTrainNum0 = 0
            orangeTrainTurns = 0
            orangeTrainRotation = 0
            trainsBack += 1
        if orangeTrain1Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain1X = 578
            orangeTrain1Y = 500
            orangeTrainNum1 = 0
            orangeTrain1Turns = 0
            orangeTrain1Rotation = 0
            trainsBack += 1
        if orangeTrain2Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain2X = 578
            orangeTrain2Y = 500
            orangeTrainNum2 = 0
            orangeTrain2Turns = 0
            orangeTrain2Rotation = 0
            trainsBack += 1
        if orangeTrain3Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain3X = 578
            orangeTrain3Y = 500
            orangeTrainNum3 = 0
            orangeTrain3Turns = 0
            orangeTrain3Rotation = 0
            trainsBack += 1
        if orangeTrain4Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            orangeTrain4X = 578
            orangeTrain4Y = 500
            orangeTrainNum4 = 0
            orangeTrain4Turns = 0
            orangeTrain4Rotation = 0
            trainsBack += 1


        #Yellow Train
        #red station
        if yellowTrainCollider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            yellowTrain = pygame.transform.rotate(yellowTrain, 270)
            trainsBack += 1
        if yellowTrain1Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
            trainsBack += 1
        if yellowTrain2Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
            trainsBack += 1
        if yellowTrain3Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
            trainsBack += 1
        if yellowTrain4Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
            trainsBack += 1

            #orange station
        if yellowTrainCollider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            yellowTrain = pygame.transform.rotate(yellowTrain, 270)
            trainsBack += 1
        if yellowTrain1Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            yellowTrain1 = pygame.transform.rotate(yellowTrain1, 270)
            trainsBack += 1
        if yellowTrain2Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            yellowTrain2 = pygame.transform.rotate(yellowTrain2, 270)
            trainsBack += 1
        if yellowTrain3Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            yellowTrain3 = pygame.transform.rotate(yellowTrain3, 270)
            trainsBack += 1
        if yellowTrain4Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            yellowTrain4 = pygame.transform.rotate(yellowTrain4, 270)
            trainsBack += 1

            #Yellow station
        if yellowTrainCollider.colliderect(yellowStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            yellowTrain = pygame.transform.rotate(yellowTrain, 90)
            trainsBack += 1
        if yellowTrain1Collider.colliderect(yellowStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
            trainsBack += 1
        if yellowTrain2Collider.colliderect(yellowStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
            trainsBack += 1
        if yellowTrain3Collider.colliderect(yellowStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
            trainsBack += 1
        if yellowTrain4Collider.colliderect(yellowStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
            trainsBack += 1

            #Green station
        if yellowTrainCollider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            yellowTrain = pygame.transform.rotate(yellowTrain, 90)
            trainsBack += 1
        if yellowTrain1Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            yellowTrain1 = pygame.transform.rotate(yellowTrain1, 90)
            trainsBack += 1
        if yellowTrain2Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            yellowTrain2 = pygame.transform.rotate(yellowTrain2, 90)
            trainsBack += 1
        if yellowTrain3Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            yellowTrain3 = pygame.transform.rotate(yellowTrain3, 90)
            trainsBack += 1
        if yellowTrain4Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            yellowTrain4 = pygame.transform.rotate(yellowTrain4, 90)
            trainsBack += 1

            #blue station
        if yellowTrainCollider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            trainsBack += 1
        if yellowTrain1Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            trainsBack += 1
        if yellowTrain2Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            trainsBack += 1
        if yellowTrain3Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            trainsBack += 1
        if yellowTrain4Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if yellowTrainCollider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrainX = 578
            yellowTrainY = 500
            yellowTrainNum0 = 0
            yellowTrainTurns = 0
            yellowTrainRotation = 0
            trainsBack += 1
        if yellowTrain1Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain1X = 578
            yellowTrain1Y = 500
            yellowTrainNum1 = 0
            yellowTrain1Turns = 0
            yellowTrain1Rotation = 0
            trainsBack += 1
        if yellowTrain2Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain2X = 578
            yellowTrain2Y = 500
            yellowTrainNum2 = 0
            yellowTrain2Turns = 0
            yellowTrain2Rotation = 0
            trainsBack += 1
        if yellowTrain3Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain3X = 578
            yellowTrain3Y = 500
            yellowTrainNum3 = 0
            yellowTrain3Turns = 0
            yellowTrain3Rotation = 0
            trainsBack += 1
        if yellowTrain4Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            yellowTrain4X = 578
            yellowTrain4Y = 500
            yellowTrainNum4 = 0
            yellowTrain4Turns = 0
            yellowTrain4Rotation = 0
            trainsBack += 1


        #Green train
        #red station
        if greenTrainCollider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            greenTrain = pygame.transform.rotate(greenTrain, 270)
            trainsBack += 1
        if greenTrain1Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
            trainsBack += 1
        if greenTrain2Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
            trainsBack += 1
        if greenTrain3Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
            trainsBack += 1
        if greenTrain4Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
            trainsBack += 1

            #orange station
        if greenTrainCollider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            greenTrain = pygame.transform.rotate(greenTrain, 270)
            trainsBack += 1
        if greenTrain1Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            greenTrain1 = pygame.transform.rotate(greenTrain1, 270)
            trainsBack += 1
        if greenTrain2Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            greenTrain2 = pygame.transform.rotate(greenTrain2, 270)
            trainsBack += 1
        if greenTrain3Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            greenTrain3 = pygame.transform.rotate(greenTrain3, 270)
            trainsBack += 1
        if greenTrain4Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            greenTrain4 = pygame.transform.rotate(greenTrain4, 270)
            trainsBack += 1

            #Yellow station
        if greenTrainCollider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            greenTrain = pygame.transform.rotate(greenTrain, 90)
            trainsBack += 1
        if greenTrain1Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
            trainsBack += 1
        if greenTrain2Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
            trainsBack += 1
        if greenTrain3Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
            trainsBack += 1
        if greenTrain4Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
            trainsBack += 1

            #Green station
        if greenTrainCollider.colliderect(greenStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            greenTrain = pygame.transform.rotate(greenTrain, 90)
            trainsBack += 1
        if greenTrain1Collider.colliderect(greenStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            greenTrain1 = pygame.transform.rotate(greenTrain1, 90)
            trainsBack += 1
        if greenTrain2Collider.colliderect(greenStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            greenTrain2 = pygame.transform.rotate(greenTrain2, 90)
            trainsBack += 1
        if greenTrain3Collider.colliderect(greenStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            greenTrain3 = pygame.transform.rotate(greenTrain3, 90)
            trainsBack += 1
        if greenTrain4Collider.colliderect(greenStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            greenTrain4 = pygame.transform.rotate(greenTrain4, 90)
            trainsBack += 1

            #blue station
        if greenTrainCollider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            trainsBack += 1
        if greenTrain1Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            trainsBack += 1
        if greenTrain2Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            trainsBack += 1
        if greenTrain3Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            trainsBack += 1
        if greenTrain4Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if greenTrainCollider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrainX = 578
            greenTrainY = 500
            greenTrainNum0 = 0
            greenTrainTurns = 0
            greenTrainRotation = 0
            trainsBack += 1
        if greenTrain1Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain1X = 578
            greenTrain1Y = 500
            greenTrainNum1 = 0
            greenTrain1Turns = 0
            greenTrain1Rotation = 0
            trainsBack += 1
        if greenTrain2Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain2X = 578
            greenTrain2Y = 500
            greenTrainNum2 = 0
            greenTrain2Turns = 0
            greenTrain2Rotation = 0
            trainsBack += 1
        if greenTrain3Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain3X = 578
            greenTrain3Y = 500
            greenTrainNum3 = 0
            greenTrain3Turns = 0
            greenTrain3Rotation = 0
            trainsBack += 1
        if greenTrain4Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            greenTrain4X = 578
            greenTrain4Y = 500
            greenTrainNum4 = 0
            greenTrain4Turns = 0
            greenTrain4Rotation = 0
            trainsBack += 1

        #Blue train
        #red station
        if blueTrainCollider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            blueTrain = pygame.transform.rotate(blueTrain, 270)
            trainsBack += 1
        if blueTrain1Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
            trainsBack += 1
        if blueTrain2Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
            trainsBack += 1
        if blueTrain3Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
            trainsBack += 1
        if blueTrain4Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
            trainsBack += 1

            #orange station
        if blueTrainCollider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            blueTrain = pygame.transform.rotate(blueTrain, 270)
            trainsBack += 1
        if blueTrain1Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            blueTrain1 = pygame.transform.rotate(blueTrain1, 270)
            trainsBack += 1
        if blueTrain2Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            blueTrain2 = pygame.transform.rotate(blueTrain2, 270)
            trainsBack += 1
        if blueTrain3Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            blueTrain3 = pygame.transform.rotate(blueTrain3, 270)
            trainsBack += 1
        if blueTrain4Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            blueTrain4 = pygame.transform.rotate(blueTrain4, 270)
            trainsBack += 1

            #Yellow station
        if blueTrainCollider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            blueTrain = pygame.transform.rotate(blueTrain, 90)
            trainsBack += 1
        if blueTrain1Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
            trainsBack += 1
        if blueTrain2Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
            trainsBack += 1
        if blueTrain3Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
            trainsBack += 1
        if blueTrain4Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
            trainsBack += 1

            #Green station
        if blueTrainCollider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            blueTrain = pygame.transform.rotate(blueTrain, 90)
            trainsBack += 1
        if blueTrain1Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            blueTrain1 = pygame.transform.rotate(blueTrain1, 90)
            trainsBack += 1
        if blueTrain2Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            blueTrain2 = pygame.transform.rotate(blueTrain2, 90)
            trainsBack += 1
        if blueTrain3Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            blueTrain3 = pygame.transform.rotate(blueTrain3, 90)
            trainsBack += 1
        if blueTrain4Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            blueTrain4 = pygame.transform.rotate(blueTrain4, 90)
            trainsBack += 1

            #blue station
        if blueTrainCollider.colliderect(blueStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            trainsBack += 1
        if blueTrain1Collider.colliderect(blueStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            trainsBack += 1
        if blueTrain2Collider.colliderect(blueStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            trainsBack += 1
        if blueTrain3Collider.colliderect(blueStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            trainsBack += 1
        if blueTrain4Collider.colliderect(blueStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if blueTrainCollider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrainX = 578
            blueTrainY = 500
            blueTrainNum0 = 0
            blueTrainTurns = 0
            blueTrainRotation = 0
            trainsBack += 1
        if blueTrain1Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain1X = 578
            blueTrain1Y = 500
            blueTrainNum1 = 0
            blueTrain1Turns = 0
            blueTrain1Rotation = 0
            trainsBack += 1
        if blueTrain2Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain2X = 578
            blueTrain2Y = 500
            blueTrainNum2 = 0
            blueTrain2Turns = 0
            blueTrain2Rotation = 0
            trainsBack += 1
        if blueTrain3Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain3X = 578
            blueTrain3Y = 500
            blueTrainNum3 = 0
            blueTrain3Turns = 0
            blueTrain3Rotation = 0
            trainsBack += 1
        if blueTrain4Collider.colliderect(purpleStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            blueTrain4X = 578
            blueTrain4Y = 500
            blueTrainNum4 = 0
            blueTrain4Turns = 0
            blueTrain4Rotation = 0
            trainsBack += 1


        #Purple Train
        #red station
        if purpleTrainCollider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            purpleTrain = pygame.transform.rotate(purpleTrain, 270)
            trainsBack += 1
        if purpleTrain1Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
            trainsBack += 1
        if purpleTrain2Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
            trainsBack += 1
        if purpleTrain3Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
            trainsBack += 1
        if purpleTrain4Collider.colliderect(redStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
            trainsBack += 1

            #orange station
        if purpleTrainCollider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            purpleTrain = pygame.transform.rotate(purpleTrain, 270)
            trainsBack += 1
        if purpleTrain1Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            purpleTrain1 = pygame.transform.rotate(purpleTrain1, 270)
            trainsBack += 1
        if purpleTrain2Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            purpleTrain2 = pygame.transform.rotate(purpleTrain2, 270)
            trainsBack += 1
        if purpleTrain3Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            purpleTrain3 = pygame.transform.rotate(purpleTrain3, 270)
            trainsBack += 1
        if purpleTrain4Collider.colliderect(orangeStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            purpleTrain4 = pygame.transform.rotate(purpleTrain4, 270)
            trainsBack += 1

            #Yellow station
        if purpleTrainCollider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            purpleTrain = pygame.transform.rotate(purpleTrain, 90)
            trainsBack += 1
        if purpleTrain1Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
            trainsBack += 1
        if purpleTrain2Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
            trainsBack += 1
        if purpleTrain3Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
            trainsBack += 1
        if purpleTrain4Collider.colliderect(yellowStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
            trainsBack += 1

            #Green station
        if purpleTrainCollider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            purpleTrain = pygame.transform.rotate(purpleTrain, 90)
            trainsBack += 1
        if purpleTrain1Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            purpleTrain1 = pygame.transform.rotate(purpleTrain1, 90)
            trainsBack += 1
        if purpleTrain2Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            purpleTrain2 = pygame.transform.rotate(purpleTrain2, 90)
            trainsBack += 1
        if purpleTrain3Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            purpleTrain3 = pygame.transform.rotate(purpleTrain3, 90)
            trainsBack += 1
        if purpleTrain4Collider.colliderect(greenStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            purpleTrain4 = pygame.transform.rotate(purpleTrain4, 90)
            trainsBack += 1

            #blue station
        if purpleTrainCollider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            trainsBack += 1
        if purpleTrain1Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            trainsBack += 1
        if purpleTrain2Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            trainsBack += 1
        if purpleTrain3Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            trainsBack += 1
        if purpleTrain4Collider.colliderect(blueStationCollider):
            lives -= 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            trainsBack += 1

            #purple station
        if purpleTrainCollider.colliderect(purpleStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            purpleTrainX = 578
            purpleTrainY = 500
            purpleTrainNum0 = 0
            purpleTrainTurns = 0
            purpleTrainRotation = 0
            trainsBack += 1
        if purpleTrain1Collider.colliderect(purpleStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            purpleTrain1X = 578
            purpleTrain1Y = 500
            purpleTrainNum1 = 0
            purpleTrain1Turns = 0
            purpleTrain1Rotation = 0
            trainsBack += 1
        if purpleTrain2Collider.colliderect(purpleStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            purpleTrain2X = 578
            purpleTrain2Y = 500
            purpleTrainNum2 = 0
            purpleTrain2Turns = 0
            purpleTrain2Rotation = 0
            trainsBack += 1
        if purpleTrain3Collider.colliderect(purpleStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            purpleTrain3X = 578
            purpleTrain3Y = 500
            purpleTrainNum3 = 0
            purpleTrain3Turns = 0
            purpleTrain3Rotation = 0
            trainsBack += 1
        if purpleTrain4Collider.colliderect(purpleStationCollider):
            trainsIn += 1
            screen.blit(background,[0,0])
            purpleTrain4X = 578
            purpleTrain4Y = 500
            purpleTrainNum4 = 0
            purpleTrain4Turns = 0
            purpleTrain4Rotation = 0
            trainsBack += 1


        if lives <= 0:
            gameOn = False
            gameOver = True

        pygame.display.flip()
        clock.tick(60)



    while gameOver:
        menuButton1 = pygame.Rect(160, 290, 300, 50)
        pygame.draw.rect(screen, black, (75, 75, 490, 330))
        screen.blit(quitButtonText, (270, 360))
        screen.blit(scoreText, (275, 150))
        pygame.draw.rect(screen, white, quitButton)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if quitButton.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))
                    pygame.quit()
                    exit


        pygame.display.flip()
        clock.tick(60)