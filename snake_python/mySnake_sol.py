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

def wallCollision(x, y, width, height):
    """
    Retourne True si le serpent touche le mur, False sinon
    """
    return (x < 0) or (x >= width) or (y < 0) or (y >= height)
    #return False # modifier

def valid_pos(app, x, y):
    """
    Retourne False si la position (x,y) se trouve sur le serpent, True sinon
    """
    for i in range(0, app.player.length):
        if app.player.x[i] == x and app.player.y[i] == y:
            return False
    for i in range(0, app.other_player.length):
        if app.other_player.x[i] == x and app.player.y[i] == y:
            return False
    return True
    #return False # a modifier
    
def isCollision(x1, y1, x2, y2):
    """
    Retourne True si (x1, y1) et (x2, y2) sont sur la même position, False sinon
    """
    return (x1 == y1) and (x2 == y2)
    #return False # a modifier

def movePlayer(player, keys):
    """
    exemple: si keys[K_RIGHT] player.moveRight()
    """
    if keys[K_LEFT]:
        player.moveLeft();
    if keys[K_RIGHT]:
        player.moveRight();
    if keys[K_UP]:
        player.moveUp();
    if keys[K_DOWN]:
        player.moveDown();
    return None # a modifier (pas de return)

def moveOtherPlayer(player, keys):
    """
    exemple: si keys[K_RIGHT] player.moveRight()
    """
    if keys[K_LEFT]:
        player.moveLeft();
    if keys[K_RIGHT]:
        player.moveRight();
    if keys[K_UP]:
        player.moveUp();
    if keys[K_DOWN]:
        player.moveDown();
    return None # a modifier (pas de return)

def snakeSpeed(length):
    """
    Augmente la vitesse en fonction de la longeur du serpent
    """
    if length < 10:
        return 1
    elif length < 20:
        return 2
    elif length < 50:
        return 3
    else:
        return 4
    #return 1 # a modifier
    
def setLevel(app, level):
    """
    Définit le niveau de dificulté au départ
    """
    app.level = level
    #return None # a modifier (pas de return)

if __name__ == "__main__" :
    theApp = App()
    setLevel(theApp, 10)
    window = Window(theApp._display_surf)
    button = Button(window, theApp)
    theApp.setWindow(window)
    theApp.setButton(button)
    theApp.on_execute()
