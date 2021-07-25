import math
from general import *

def angles_to_vector(mag,alpha,beta,gamma):
    return Vector(mag.cos(alpha),mag.cos(beta),mag.cos(gamma))


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def mult(self,a):
        self.i *= a
        self.j *= a
        self.k *= a

    def div(self,a):
        self.i *= 1/a
        self.j *= 1/a
        self.k *= 1/a

    def dot_product(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k
    def dot_product_extended(self, other):
        return "( "+str(self.i * other.i)+", " + str(self.j * other.j) + ", " + str(self.k * other.k)+ " )"

    def cross_product(self,other):
        one = self.j*other.k - self.k*other.j
        two = self.k*other.i - self.i*other.k
        three = self.i*other.j - self.j*other.i
        return Vector(one,two,three)

    def get_angles(self):
        m = self.magnitude()
        alpha = math.degrees(math.acos(self.i/m))
        beta = math.degrees(math.acos(self.j/m))
        gamma = math.degrees(math.acos(self.k/m))
        return "( alpha = " + str(alpha) + ", beta = " + str(beta) + ", gamma = " + str(gamma) + " )"

    def magnitude(self):
        a = self.i * self.i + self.j * self.j + self.k * self.k
        return math.sqrt(a)

    def angle_between(self, other):
        return math.degrees(
            math.acos(self.dot_product(other) / (self.magnitude() * other.magnitude()))
        )

    def minus(self,other):
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

    def add(self,other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def unit_vector(self):
        m = self.magnitude()
        return Vector(self.i / m, self.j / m, self.k / m)

    def clone(self):
        return Vector(self.i , self.j, self.k)

    def __str__(self):
        return "( " + str(self.i) + ", " + str(self.j) + ", " + str(self.k) + " )"

    __repr__ = __str__


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def minus(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def to_vector(self):
        return Vector(self.x, self.y, self.z)

    def __str__(self):
        return "( " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + " )"

    __repr__ = __str__


if __name__ == "__main__":
    P = Vector(1000/math.sqrt(41),800/math.sqrt(41),0)
    Q = Vector(-500/math.sqrt(27.25),150/math.sqrt(27.25),0)

    # At C
    Rce = Vector(0,4,0)
    Rcf = Vector(-5,1.5,0)

    Mp = Rce.cross_product(P)
    Mq = Rcf.cross_product(Q)

    # print(Mp)
    # print(Mq)
    # print(Mp.add(Mq))

    # At B
    Rbe = Vector(5,4,0)
    Rbf = Vector(0,1.5,0)

    Mp = Rbe.cross_product(P)
    Mq = Rbf.cross_product(Q)

    # print(Mp)
    # print(Mq)
    # print(Mp.add(Mq))


    # At A
    Rae = Vector(5,0,0)
    Raf = Vector(0,-2.5,0)

    Mp = Rae.cross_product(P)
    Mq = Raf.cross_product(Q)


    # print(Mp)
    # print(Mq)
    # print(Mp.add(Mq))
    





    
    
