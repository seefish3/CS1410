import pygame
import math
import random

class SmallBird:

    def __init__( self, x, y, width, height ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mColor = ( 0, 0, 0 )
        self.mThickness = 2
        return

    def thicken( self ):
        self.mThickness += 1
        if self.mThickness > 5:
            self.mThickness = 5
        return

    def thin( self ):
        self.mThickness -= 1
        if self.mThickness < 1:
            self.mThickness = 1
        return

    def evolve( self, dt ):
        r = random.randrange( 100 )
        if r < 3:
            self.thicken( )
        elif r < 6:
            self.thin( )
        return

    def draw( self, surface ):
        rect1 = pygame.Rect( int(self.mX), int(self.mY), int(self.mWidth/2), int(self.mHeight) )
        rect2 = pygame.Rect( int(self.mX+self.mWidth/2), int(self.mY), int(self.mWidth/2), int(self.mHeight) )
        pygame.draw.arc( surface, self.mColor, rect1, 0.0, math.pi, self.mThickness )
        pygame.draw.arc( surface, self.mColor, rect2, 0.0, math.pi, self.mThickness )
        return
