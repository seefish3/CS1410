import sun
import walls
import door

class Picture:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mWalls = walls.Walls( self.mWidth, self.mHeight )
        self.mSun = sun.Sun( 0.75 * self.mWidth, 0.66 * self.mHeight, (1./8.)*self.mHeight )
        self.mDoor = door.Door(self.mWidth / 6, self.mHeight / 3)
        return

    def evolve( self, dt ):
        self.mWalls.evolve( dt )
        self.mSun.evolve( dt )
        self.mDoor.evolve( dt )
        return

    def draw( self, surface ):
        self.mWalls.draw( surface )
        self.mSun.draw( surface )
        self.mDoor.draw( surface )

        return
