############################################################################
#
# DIM - A Direct Interaction Manager for SAGE
# Copyright (C) 2013 Electronic Visualization Laboratory,
# University of Illinois at Chicago
#
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the distribution.
#  * Neither the name of the University of Illinois at Chicago nor
#    the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Direct questions, comments etc about SAGE UI to www.evl.uic.edu/cavern/forum
#
############################################################################

import math

class CoordinateCalculator(object):
    
    MAX_Y_ERROR = 0.5
    # in meters
    
    MAX_X_ERROR = 0.05
    # fractional
    
    RADIUS = 6.477 / 2;
    RADIANS_FOR_DOOR = 36 * math.pi / 180;
    MIN_Y = 0.305;
    MAX_Y = 2.625;
    MAX_Z = RADIUS * (2 + math.cos(RADIANS_FOR_DOOR / 2));
    X = 0
    Y = 1
    Z = 2
    BAD_SCREEN_POS = (-1,-1)
    
    
    def __init__(self):
        self.position = (0, 0, 1)
        self.orientation = (0, 0, 1)
        self.screen_pos = (0.5, 0.5)
    
    def set_position(self, x, y, z):
        self.position = (x, y, z)
    
    def set_orientation(self, x, y, z):
        self.orientation = (x, y, z)
    
    def calculate(self):
        '''Orientation is vertical'''
        if self.orientation[self.X] == 0 and self.orientation[self.Z] == 0:
            self.set_screen_pos(self.BAD_SCREEN_POS)
            return self.get_screen_pos()
        h = 0   # x-coordinate of the center of the circle
        k = 0   # z-coordinate of the center of the circle
        ox = self.orientation[self.X]  # parametric slope of x, from orientation vector
        oy = self.orientation[self.Y]  # parametric slope of y, from orientation vector
        oz = self.orientation[self.Z]  # parametric slope of z, from orientation vector
        x0 = self.position[self.X]   # position in x
        y0 = self.position[self.Y]   # position in y
        z0 = self.position[self.Z]   # position in z
        r = self.RADIUS    # Radius of the cylinder
        
        # A * t^2 + B * t + C
        A = ox*ox + oz*oz
        B = 2*ox*x0 + 2*oz*z0 - 2*h*ox - 2*k*oz
        C = x0*x0 + z0*z0 + h*h + k*k - r*r - 2*h*x0 - 2*k*z0
        
        if A != 0  and (B*B - 4*A*C) >= 0:
            t1 = (-B + math.sqrt(B*B - 4*A*C)) / (2*A)
            t2 = (-B - math.sqrt(B*B - 4*A*C)) / (2*A)
            t = 0
            if t1 >= 0:
                t = t1
            elif t2 >= 0:
                t = t2
            else:
                self.set_screen_pos(self.BAD_SCREEN_POS)
                return self.get_screen_pos()
            x_pos = ox*t + x0
            y_pos = oy*t + y0
            z_pos = oz*t + z0
            self.calculate_screen_position(x_pos, y_pos, z_pos)
            return self.get_screen_pos()
        else:
            self.set_screen_pos(self.BAD_SCREEN_POS)
            return self.get_screen_pos()
        
    
    def calculate_screen_position(self, x, y, z):
        '''I'm not certain that these checks are necessary; they aren't
        normal, and we'll get a valid point anyway.'''
        '''
        if z < 0:
            z = 0
        if z > 2*self.RADIUS:
            z = 2*self.RADIUS
        if y > self.MAX_Y:
            y = self.MAX_Y
        if y < self.MIN_Y:
            y = self.MIN_Y
        if x > self.RADIUS:
            x = self.RADIUS
        if x < -self.RADIUS:
            x = -self.RADIUS
        '''
        
        if y > self.MAX_Y:
            if y < self.MAX_Y + self.MAX_Y_ERROR:
                y = self.MAX_Y
            else:
                self.set_screen_pos(self.BAD_SCREEN_POS)
                return
        if y < self.MIN_Y:
            if y > self.MIN_Y - self.MAX_Y_ERROR:
                y = self.MIN_Y
            else:
                self.set_screen_pos(self.BAD_SCREEN_POS)
                return
            
        angle = math.atan2(x, z)
        
        if angle < 0:
            angle += 2*math.pi
        angle = 2*math.pi - angle
        angle -= self.RADIANS_FOR_DOOR / 2
        x = angle / (2*math.pi - self.RADIANS_FOR_DOOR)
        x += 0.02777777777 
        if x > 1:
            if x < 1 + self.MAX_X_ERROR:
                x = 1
            else:
                self.set_screen_pos(self.BAD_SCREEN_POS)
                return
        if x < 0:
            if x > -self.MAX_X_ERROR:
                x = 0
            else:
                self.set_screen_pos(self.BAD_SCREEN_POS)
                return
        y -= self.MIN_Y
        y /= (self.MAX_Y - self.MIN_Y)
        pos = (x, 1-y)
        self.set_screen_pos(pos)
    
    def set_screen_pos(self, pos):
        self.screen_pos = pos
    
    def get_screen_pos(self):
        return self.screen_pos
    
    def get_x(self):
        return self.screen_pos[0]
    
    def get_y(self):
        return self.screen_pos[1]
    
    def test(self):
        calc = CoordinateCalculator()
        calc.set_position(1, 1, 1)
        calc.set_orientation(1, 1, 1)
        return calc.calculate()
    
    def main(self):
        self.set_orientation(-1, -1, 1)
        self.set_position(0, 3, self.RADIUS)
        print self.calculate()
        
    
if __name__ == '__main__':
    obj = CoordinateCalculator()
    obj.main()
