#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Snake - v1.0
# License CC BY 4.0
# Thomas Le Menestrel - 2019.09.18

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Importing the external libraries we need for this 

from pygame.locals import *
from random import randint
import time
import pygame
import sys

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Declaring the main variables

# Main booleans 

playing = True
moveUp = moveDown = moveRight = moveLeft = move_init = False

# Other int variables

step = 23
score = 0
length = 2
speed = 75

# Lists to store the coordinates of the snake

x_snake_position = [0]
y_snake_position = [0]

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Increasing the size of the list to potentially have 1000 sections for the snake

for i in range(0,1000):

    x_snake_position.append(-100)
    y_snake_position.append(-100)
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Function to check if the snake hits something like fruits or itself

def collision(x_coordinates_1,y_coordinates_1,x_coordinates_2,y_coordinates_2, size_snake, size_fruit):

    if ((x_coordinates_1 + size_snake >= x_coordinates_2) or (x_coordinates_1 >= x_coordinates_2)) and x_coordinates_1 <= x_coordinates_2 + size_fruit:
        if ((y_coordinates_1 >= y_coordinates_2) or (y_coordinates_1 + size_snake >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
            return True
        return False

# Function to display the player's score

def disp_score(score):
    
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (0, 0, 0))
    window.blit(text,(400,0))
    
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Initialising pygame

pygame.init()

# Creating the main window and giving it a name

window = pygame.display.set_mode((500, 500))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")

# Blitting an image on the main window

cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((250, 250, 250))
window.blit(cover, (0,0))

# Refreshing the screen to display everything

pygame.display.flip()

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
 
# Loading the main images on the game window

head = pygame.image.load("head.png").convert_alpha() # The head
head = pygame.transform.scale(head, (35,35))

body_part_1 = pygame.image.load("body.png").convert_alpha() # The body
body_part_1 = pygame.transform.scale(body_part_1, (25,25))

fruit = pygame.image.load("fruit.png").convert_alpha() # The fruit
fruit = pygame.transform.scale(fruit, (35,35))

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
 
# Storing the head and fruit's coordinates in variables

position_1 = head.get_rect()
position_fruit = fruit.get_rect()

# Storing the variables in the list variables created before

x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y

# Giving random coordinates to the first fruit of the game

position_fruit.x = randint(2,10)*step
position_fruit.y = randint(2,10)*step

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

# Main loop for the game

while (playing == True):
    
    # Collecting all the events

    for event in pygame.event.get(): 
        
        # Checking if the user quits the game
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            
            playing = False
     
        # Checking if the user presses a key
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if moveUp == False and move_init == True:#Vérification que la direction soit différente et annonce que les déplacement on débutés
                    if moveDown == True:# Empêchement d'aller dans la direction opposée
                        moveUp == False
                        
                    else:
                        
                        moveDown = moveRight = moveLeft = False #Changement de la variable de déplacement
                        moveUp = move_init = True

            if event.key == pygame.K_DOWN:

                if moveDown == False:# Empêchement d'aller dans la direction opposée
                    if moveUp == True:
                        moveDown == False
                        
                    else:
                        
                        moveRight = moveLeft = moveUp = False #Changement de la variable de déplacement
                        moveDown = move_init = True

            if event.key == pygame.K_RIGHT:

                if moveRight == False: # Empêchement d'aller dans la direction opposée
                    if moveLeft == True:
                        moveRight == False
                        
                    else:
                        
                        moveLeft = moveUp = moveDown = False #Changement de la variable de déplacement
                        moveRight = move_init = True

            if event.key == pygame.K_LEFT:
       
                if moveLeft == False:
                    if moveRight == True:# Empêchement d'aller dans la direction opposée
                        moveLeft == False
                        
                    else:
                        
                        moveRight = moveDown = moveUp = False #Changement de la variable de déplacement
                        moveLeft = move_init = True
                            
                        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

    # Blitting the head and the first part of the body

    window.blit(body_part_1, (-5,5))
    window.blit(head, (0,0))

    # Moving each part of the body by giving them new coordinates

    for i in range(length-1,0,-1):

        x_snake_position[i] = x_snake_position[(i-1)]

        y_snake_position[i] = y_snake_position[(i-1)]
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

    # Filling the window with white to erase the different parts of the snake
    
    cover.fill((250, 250, 250)) 
    
    # Blitting the parts of the snake on the screen
    
    for i in range(1,length):

        cover.blit(body_part_1, (x_snake_position[i], y_snake_position[i]))
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
    
    # Moving the snake in a certain direction if the user presses a key
    
    if moveUp:

        y_snake_position[0] = y_snake_position[0] - step 
        window.blit(cover, (0,0)) 
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveDown:

        y_snake_position[0] = y_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveRight:

        x_snake_position[0] = x_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveLeft:

        x_snake_position[0] = x_snake_position[0] - step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

    # Calling the collision function to check if the snake hits the edges of the window

    if x_snake_position[0] < window_rect.left:

        playing = False

    if x_snake_position[0] + 35 > window_rect.right:

        playing = False

    if y_snake_position[0] < window_rect.top:

        playing = False
    
    if y_snake_position[0] + 35 > window_rect.bottom:

        playing = False
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
    
    # Calling the collision function to check if the snake hits itself

    if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i], y_snake_position[i],0,0) and (move_init == True):
        
        playing = False
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
  
    # Blitting the fruit
    
    window.blit(fruit, position_fruit)

    # Calling the collision function to check if the snake hits the fruit
    
    if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y,35,25):
        
        # Giving new coordinates to the fruit when the snake eats it

        position_fruit.x = randint(1,20)*step   
        position_fruit.y = randint(1,20)*step
    
        # Giving new coordinates to the fruit if the ones given above are the same as the snake's ones
        
        for j in range(0,length):

            while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j],35,25):

                position_fruit.x = randint(1,20)*step   
                position_fruit.y = randint(1,20)*step
        
        # Increasing the size of the snake and the score
        
        length = length + 1
        score = score + 1
        
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
 
    # Displaying the score
    
    disp_score(score)
    
    # Flipping to add everything on the board

    pygame.display.flip()

    # Delaying the game to make the snake move fluently
    
    time.sleep (speed / 1000)

##################################################################################################################################################################
##################################################################################################################################################################
################################################################################################################################################################## 
    
# Exiting the game

pygame.quit()
exit()