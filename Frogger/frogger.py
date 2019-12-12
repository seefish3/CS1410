from froggerlib import frog, stage, car, turtle, home, road
import pygame

class Frogger:

    def __init__(self, cell_size, num_row, num_col, width, height):
        self.cell_size = cell_size
        self.num_row = num_row
        self.num_col = num_col
        self.width = width
        self.height = height

        gap_size = .1 * self.cell_size
        x = self.num_col - 1 // 2
        y = (self.num_row - 1) * self.cell_size
        w = self.cell_size
        h = self.cell_size
        dx = x #desired X
        dy = y #desired y
        s = 10
        hg = self.cell_size
        vg = self.cell_size
        self.frog = frog.Frog(x, y, w, h, dx, dy, s, hg, vg)

        x = 0
        y = (self.num_row - 1) * self.cell_size
        w = self.width
        h = self.cell_size

        self.stage1 = stage.Stage(x, y, w, h)

        x = 0
        y = (self.num_row -2 ) * self.cell_size
        w = self.cell_size -1
        h = self.cell_size -1
        dx = self.width + self.cell_size
        dy = y
        s = 3
        self.car1 = car.Car(x,y,w,h,dx,dy,s)

        x = -self.cell_size
        y = (self.num_row -3 ) * self.cell_size
        w = self.cell_size
        h = self.cell_size
        dx = self.width + self.cell_size
        dy = y
        s = 3
        self.turtle1 = turtle.Turtle(x,y,w,h,dx,dy,s)

        self.home = home.Home(0, 0, self.width//2, self.cell_size)

        num_roads = (self.num_row - 3 ) // 2
        self.roads = []
        self.num_roads = ( self.num_row - 3) // 2
        for i in range(num_roads):
            x = 0
            y = (self.num_row - 2+i) * self.cell_size
            w = 1
            h = self.cell_size

        self.frog_dead = False

    def down( self ):
        self.frog.down()

    def up( self ):
        self.frog.up()

    def left( self ):
        self.frog.left()

    def right( self ):
        self.frog.right()

    def evolve(self, dt):
        if self.frog_dead:
            return
        self.frog.move()
        if self.frog.outOfBounds(self.width, self.height):
            self.frog_dead = True

        self.car1.move()
        if self.car1.atDesiredLocation():
            self.car1.setX(-self.cell_size)

        if self.car1.hits(self.frog):
            self.frog_dead = True

        self.turtle1.move()
        self.turtle1.supports(self.frog)

        if self.home.hits(self.frog):
            return


    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(surface,(255,255,255), rect)

        draw_obj(surface, self.stage1,(200,100,200))
        draw_obj(surface, self.car1, (255,0,0))
        draw_obj(surface, self.turtle1, (255,255,0))
        draw_obj(surface, self.frog,(0,200,100))
        draw_obj(surface, self.home, (255,0,0))
        draw_obj(surface, self.roads, (255,255,255))


def draw_obj(surface, obj, color):
    rect = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, rect)
