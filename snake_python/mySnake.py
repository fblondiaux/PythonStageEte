# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:46:10 2018

@author: Quentin
"""
from pygame.locals import *
from random import randint
import pygame
import time
from random import randint
from snake import *

def wallCollision(x,y,width,height):
    # Retourne True si le serpent touche le mur, False sinon
    return False # modifier
    
def valid_pos(app, x, y):
    # Retourne False si la position (x,y) se trouve sur le serpent, True sinon
    return False # a modifier
    
def isCollision(x1,y1,x2,y2):
    # Retourne True si (x1,y1) et (x2,y2) sont sur la même position, False sinon
    return False # a modifier

def movePlayer(player, keys):
    # exemple: si keys[K_RIGHT] player.moveRight()
    return None # a modifier (pas de return)

def snakeSpeed(length):
    # augmente la vitesse en fonction de la longeur du serpent
    return 1 # a modifier
    
def setLevel(app, level):
    # defini le niveau de dificulté au départ
    return None # a modifier (pas de return)

if __name__ == "__main__" :
    theApp = App()
    setLevel(theApp, 10)
    window = Window(theApp._display_surf)
    button = Button(window, restart(theApp), theApp)
    theApp.setWindow(window)
    theApp.setButton(button)
    theApp.on_execute()