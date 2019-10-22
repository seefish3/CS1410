import pygame


class Background:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (81, 93, 172)
        return

    def draw(self, surface):

        ract = pygame.Rect(int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ))
        pygame.draw.rect(surface, self.mColor, rect, 0)

        return

        
