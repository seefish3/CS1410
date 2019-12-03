import pygame

class Light:

    def __init__( self, x, y, radius ):
        self.mX = x
        self.mY = y
        self.mRadius = radius
        self.mColor = ( 243, 247, 14 )
        return

    def evolve( self, dt ):
        #self.mY -= 10*dt
        return

    def draw( self, surface ):
        center = ( int(self.mX), int(self.mY) )
        pygame.draw.circle( surface, self.mColor, center, int(self.mRadius), 0 )
        return
