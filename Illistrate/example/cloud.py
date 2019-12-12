import pygame

class Cloud:

    def __init__( self, x, y, width, height ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mColor = ( 251, 200, 122 )
        return

    def darken( self ):
        r, g, b = self.mColor
        r *= 0.9
        g *= 0.9
        b *= 0.9
        self.mColor = (int(r),int(g),int(b))
        return

    def lighten( self ):
        r, g, b = self.mColor
        r *= 1.1
        g *= 1.1
        b *= 1.1
        self.mColor = (min(int(r),255), min(int(g),255), min(int(b),255) )
        return

    def evolve( self, dt ):
        return

    def draw( self, surface ):

        rect = pygame.Rect( int ( self.mX ), int ( self.mY ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.ellipse( surface, self.mColor, rect, 0 )
        
        return
