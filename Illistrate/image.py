import pygame
import walls
import door
#import tv
import light
#import window
#import plant
#import table


class Image:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = walls.Walls( self.width, self.height )
        self.door = door.Door(0.10 * self.width, 20 * self.height, self.width / 7, self.height/ 5, 112, 95, 54)
        #self.tv = tv.TV()
        self.light = light.Light( 0.75 * self.width, 0.66 * self.height, (1./8.)*self.height )

        return

    def draw( self, surface ):
        self.walls.draw(surface)
        self.door.draw(surface)
        self.light.draw(surface)

        return

    def evolve( self, dt ):
        self.walls.evolve(dt)
        self.door.evolve(dt)
        self.light.evolve(dt)

        return


    def actOnPressA( self ):
        return

    def actOnHoldA( self ):
        return

    def actOnHoldUP( self ):
        return

    def actOnLeftClick( self, x, y ):
        return
