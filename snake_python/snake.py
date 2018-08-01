# -*- coding: utf-8 -*-

from mySnake import *
from sys import exit

class Apple:
    # Instance variables:
    # x : int
    # y : int
    step = 40

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Player:
    # Instance variables:
    # x : list of ints
    # y : list of ints
    # direction : int
    # updateCount : int
    # length : int

    # Class variables:
    step = 40
    updateCountMax = 4

    def __init__(self, length, x, y):
       self.length = length
       self.x = [x]
       self.y = [y]
       self.direction = 0
       self.updateCount = 0
       self.alive = True
       # Fill up the list
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[1] = 1 * self.step
       self.x[2] = 2 * self.step

    def update(self):
        if not self.alive:
            return

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

    def collidesWithApple(self, apple):
        if not self.alive:
            return False

        if isCollision(apple.x, apple.y, self.x[0], self.y[0]):
            self.grow()
            apple.x = -1
            apple.y = -1 # Invalid position to put the apple outside of the board
            return True
        return False

    def collidesWithSelf(self):
        for i in range(2, self.length):
            if isCollision(self.x[0], self.y[0], self.x[i], self.y[i]):
                return True
        return False

    def collidesWithWall(self, width, height):
        return wallCollision(self.x[0], self.y[0], width, height)

    def grow(self):
        """
        Grows the snake by adding the head at the next logical position.
        Note that this means that update should be called after
        """
        self.length = self.length + 1
        self.x.append(-42)
        self.y.append(-42)

    def shift(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def setAlive(self, alive):
        self.alive = alive
        return alive

class App:
    # Instance variables:
    # gameOverPlayer : boolean
    # gameOverOtherPlayer : boolean
    # player : Player
    # other_player : Player
    # apple : Apple
    # window :
    # button :
    # _display_surf : PyGame Surface
    # _running : boolean
    # _image_surf : PyGame Surface
    # _apple_surf : PyGame Surface

    windowWidth = 800
    step = 40
    windowHeight = 600
    player = None
    other_player = None
    apple = None
    window = None
    button = None
    level = 1
    speed = 1

    def __init__(self):
        self.gameOverPlayer = False
        self.gameOverOtherPlayer = False
        self.player = Player(3, 0, 0)
        self.other_player = Player(3, 1, 1)
        self.apple = Apple(5,5)
        self.window = None
        self.button = None
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Snake game')
        self._running = True
        self._image_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("pygame.png").convert()

    def setWindow(self, window):
        self.window = window

    def setButton(self, button):
        self.button = button

    def restart(self):
        self.gameOverPlayer = False
        self.gameOverOtherPlayer = False
        self.player = Player(3, 0, 0)
        self.other_player = Player(3, 1, 1)
        self.apple = Apple(5, 5)
        self._running = True

    def on_loop(self):
        self.player.update()
        self.other_player.update()

        # does a snake eat the apple? + Use short-circuit evaluation + grow head here if needed
        if self.other_player.collidesWithApple(self.apple) or self.player.collidesWithApple(self.apple):
            # Need to affect a new place for the apple
            x = randint(0, 19) * self.step
            y = randint(0, 14) * self.step
            while not valid_pos(self, x, y):
                x = randint(0, 19) * self.step
                y = randint(0, 14) * self.step
            self.apple.x = x
            self.apple.y = y

        # does a snake collide with itself?
        self.gameOverPlayer = self.player.collidesWithSelf()
        self.gameOverOtherPlayer = self.other_player.collidesWithSelf()
        self.player.setAlive(not self.gameOverPlayer)
        self.other_player.setAlive(not self.gameOverOtherPlayer)

        # does a snake collide with a wall?
        self.gameOverPlayer = self.gameOverPlayer or self.player.collidesWithWall(self.windowWidth, self.windowHeight)
        self.gameOverOtherPlayer = self.gameOverOtherPlayer or self.other_player.collidesWithWall(self.windowWidth, self.windowHeight)
        self.player.setAlive(not self.gameOverPlayer)
        self.other_player.setAlive(not self.gameOverOtherPlayer)


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        print("on_event called")
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._image_surf)
        self.other_player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)

        if self.gameOverPlayer:
            self.window.setText("Joueur 1 a gagné !")
            self.window.draw()
            self.button.draw()
        elif self.gameOverOtherPlayer:
            self.window.setText("Joueur 2 a gagné !")
            self.window.draw()
            self.button.draw()

        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()
        exit

    def on_execute(self):

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            movePlayer(self.player, keys)
            moveOtherPlayer(self.other_player, keys)

            if (keys[K_ESCAPE]):
                self._running = False

            if (keys[K_RETURN]):
                restart(self)

            #print("Events:\n{}, {}".format(QUIT, MOUSEBUTTONDOWN))
            for event in pygame.event.get():
                #print(event)
                #print(event.type)
                if event.type == QUIT:
                    self._running = False
                elif event.type == MOUSEBUTTONDOWN and self.gameOver:
                    print("Hello from the event")
                    self.button.getEvent(event)

            if not self.gameOverPlayer:
                self.on_loop()

            self.on_render()
            self.speed = snakeSpeed(self.player.length)
            time.sleep(100.0 / (1000.0 * self.level * self.speed));

        self.on_cleanup()

class Window(object):
    text = "You Lose !"
    def __init__(self, screen):
        self.screen = screen
        self.rect = Rect((200,150),(400,300))
        self.color = pygame.Color('White')

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        myfont = pygame.font.SysFont("monospace", 60, True)
        label = myfont.render(self.text, 1, pygame.Color('Red'))
        self.screen.blit(label, (230,230))

    def setText(self, text):
        self.text = text

class Button(object):
    def __init__(self, parent, app):
        self.parent = parent
        self.rect = Rect((325,350), (150,50))
        self.color = pygame.Color('Black')
        self.screen = parent.screen
        self._visible = False
        self.app = app

    def getEvent(self, event):
        if self.rect.collidepoint(event.pos):
            self.app.restart()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render("restart", 1, pygame.Color('White'))
        self.screen.blit(label, (355, 365))

