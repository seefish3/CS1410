import pygame

class Ball:

    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.x = min_x
        self.y = min_y
        self.size = size
        self.dx = 0
        self.dy = 0
        self.minX = min_x
        self.maxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = 0
        self.mLeftPaddleMaxY = 0
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = 0
        self.mRightPaddleMaxY = 0
        return

            #Updates the x and y data members, but only if the new values are within the minimum and maximum values specified by the data members.
            #If either of the new values is incorrect, do not change anything.
        def setPosition(self, x, y):
            if x >= minX and x <= maxX and y >= mMinY and y <= mMaxY:
                self.x = x
                self.y = y
                return True
            else:
                return False


            #Updates the dx and dy data members. Does not check the values.
        def setSpeed(self, dx, dy):
            self.dx = dx
            self.dy = dy
            return True

            #Updates the mLeftPaddleMinY and mLeftPaddleMaxY data members, but only if the new values are within the minimum and maximum values specified by the data members.
            # Only sets the two data members if the parameters are valid. This means the minimum must not be less than mMinY and the maximum must not be more than mMaxY. Also, the minimum must be less than the maximum.
        def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
            if min_y <= paddle_min_y and max_y >= paddle_max_y:
                self.mLeftPaddleMinY = paddle_min_y
                self.mLeftPaddleMaxY = paddle_max_y
                return True
            else:
                return False

            return

            #Updates the mRightPaddleMinY and mRightPaddleMaxY data members, but only if the new values are within the minimum and maximum values specified by the data members. See notes in setLeftPaddleY.
        def setRightPaddleY(self, paddle_min_y, paddle_max_y):
            if min_y <= paddle_min_y and max_y >= paddle_max_y:
                self.mRightPaddleMinY = paddle_min_y
                self.mRightPaddleMaxY = paddle_max_y
                return True
            else:
                return False
            return

            #Receives the proposed new_y value for the ball.
            #If traveling from the current y position to the new y position would not cause the ball to bounce from the top wall, then return new_y unchanged.
            #If the value would cause the ball to bounce, then reverse the sign of dy, calculate the corrected new_y value and return the corrected value. The picture below may help.
        def checkTop(self, new_y):
            if self.y > new_y:
                return new_y
            else:

                return

            #Receives the proposed new_y value for the ball. If the new y value would not cause the ball to bounce from the bottom wall, then return new_y unchanged.
            #If the value would cause the ball to bounce, then reverse the sign of dy, calculate the corrected new_y value and return the corrected value.
            #This is similar to checkTop, but you need to include the ball’s size in your calculations. This is because the bottom of the ball will bounce from the bottom wall.
            #This is similar to the way #checkRight accounts for the right side of the ball touching the right wall.
        def checkBottom(self, new_y):

            return

            #Receives the proposed new_x value for the ball. If the new x value would not cause the ball to touch the left wall, then return new_x unchanged.
            #If the value would cause the ball to touch, then stop the ball, calculate the corrected new_x value and return it. Note that this will cause the ball to stick to the wall where it touches.
        def checkLeft(self, new_x):

            return

            #Receives the proposed new_x value for the ball. If the new x value would not cause the ball to touch the right wall, then return new_x unchanged.
            #If the value would cause the ball to touch, then stop the ball, calculate the corrected new_x value and return it.
            #Note that this will cause the ball to stick to the wall where it touches.
        def checkRight(self, new_x):

            return

            ##Receives the proposed new_x and new_y values for the ball. If the new x and new y values would not cause the ball to touch the left paddle, then return new_x unchanged.
            #If the value would cause the ball to touch, then bounce the ball from the paddle. This requires the dx to change signs. Calculate the corrected new_x value and return it.
            #If the ball’s x coordinate is already to the left of the paddle’s coordinate, there is no collision. If the ball is moving right, there is no collision.
            #To touch the paddle, the ball’s mid_y value must be between the paddle’s minimum and maximum y values. mid_y is the average of the ball’s current y position, and the new y position.
        def checkLeftPaddle(self, new_x, new_y):

            return

            #Receives the proposed new_x and new_y values for the ball. If the new x and new y values would not cause the ball to touch the right paddle, then return new_x unchanged.
            #If the value would cause the ball to touch, then bounce the ball from the paddle. This requires the dx to change signs. Calculate the corrected new_x value and return it.
            #To touch the paddle, the ball’s mid_y value must be between the paddle’s minimum and maximum y values.
        def checkRightPaddle(self, new_x, new_y):

            return

            #Receives dt, the amount of seconds that have passed since the last frame.
            #Uses x, dx and dt to calculate new_x, the proposed new x position of the ball.
            #Does similarly to calculate new_y. Uses checkTop, checkBottom, checkLeft, checkRight, checkLeftPaddle and checkRightPaddle to update the values of new_x and new_y.
            #Note that these methods will also change the sign of dx and/or dy if necessary.
            #move doesn’t need to worry about it. Finally sets x and y from the possibly updated values of new_x and new_y.
        def move(self, dt):

            return

            #Recieves several parameters. Sets the ball’s position using the x parameter and a y-value randomly chosen between min_y and max_y.
            #You may want to look at the random.uniform() function. Sets the ball’s dx to a randomly chosen value between min_dx and max_dx. Sets the ball’s dy to a randomly chosen value between min_dy and max_dy
        def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):

            return

            #Recieves several parameters. Sets the ball’s position using the x parameter and a y-value randomly chosen between min_y and max_y.
            #You may want to look at the random.uniform() function. Sets the ball’s dx to a randomly chosen value between -min_dx and -max_dx.
            #Sets the ball’s dy to a randomly chosen value between min_dy and max_dy
        def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):

            return

            #Uses PyGame to draw the rectangle for the ball. There are no unit tests for this method. It will be verified during the acceptance tests for pass-off of the full game.
        def draw(self, surface):

            return
