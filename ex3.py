class clsVect2D:
    _count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        clsVect2D._count += 1

    def getCount(self):
        return self._count
    # def _init_(self, vect2D):
    #     self.x = vect2D.x
    #     self.y = vect2D.y
    #     _count += 1

    def toString(self):
        return "x = " + str(self.x) + "y = " + str(self.y)

    def equals(self, vect2D):
        if self.x == vect2D.x and self.y == vect2D.y:
            return True
        else:
            return False

    def norme (self):
        return (self.x * 2 + self.y * 2) * 1 / 2





class clsVect3D(clsVect2D):
    _count = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        clsVect3D._count += 1

    # def _init_(self, vect3D):
    #     super()._init_(vect3D )
    #     self.z = vect3D.z

    def toString(self):
        return "x = " + str(self.x) + " y = " + str(self.y) + " z = " + str(self.z)

    def equals(self, nvect3D):
        if self.x == nvect3D.x and self.y == nvect3D.y and self.z == nvect3D.z:
            return True
        else:
            return False


    def norme(self):
        return (self.x * 2 + self.y * 2 + self.z ** 2) * 1 / 2
