def movePoint(self, shiftxy, origin):
        return (origin[0] + shiftxy[0], origin[1] + shiftxy[1])

def moveRect(self, shiftxy):
    self.collideRect.topleft = self.movePoint(shiftxy, self.collideRect.topleft)
    self.collideRect.topright = self.movePoint(shiftxy, self.collideRect.topright)       
    self.collideRect.bottomleft = self.movePoint(shiftxy, self.collideRect.bottomleft)   
    self.collideRect.bottomright = self.movePoint(shiftxy, self.collideRect.bottomright) 

def rotatePoint(self, angle, point, origin):
    sinT = math.sin(math.radians(angle))
    cosT = math.cos(math.radians(angle))
    return (origin[0] + (cosT * (point[0] - origin[0]) - sinT * (point[1] - origin[1])),
                origin[1] + (sinT * (point[0] - origin[0]) + cosT * (point[1] - origin[1])))

def rotateRect(self, degrees):
    center = (self.rect.centerx, self.rect.centery)
    print("origin topleft: ", self.collideRect.topleft)
    self.collideRect.topleft = self.rotatePoint(degrees, self.collideRect.topleft, center)
    print("new topleft: ", self.collideRect.topleft)
    self.collideRect.topright = self.rotatePoint(degrees, self.collideRect.topright, center)
    self.collideRect.bottomleft = self.rotatePoint(degrees, self.collideRect.bottomleft, center)
    self.collideRect.bottomright = self.rotatePoint(degrees, self.collideRect.bottomright, center)