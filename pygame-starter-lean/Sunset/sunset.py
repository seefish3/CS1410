import pygame
import picture

class SunSet:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mPicture = picture.Picture( self.mWidth, self.mHeight )
        return

    def actOnPressA( self ):
        return

    def actOnHoldA( self ):
        return

    def actOnHoldUP( self ):
        return

    def actOnLeftClick( self, x, y ):
        return

    def evolve( self, dt ):
        self.mPicture.evolve( dt )
        return

    # draws the current state of the system
    def draw( self, surface ):
        self.mPicture.draw( surface )
        return
