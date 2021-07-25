from general import *
from VecAPoi import *

class ThirdDimension:

    def set_vctor(self,i,j,k):
        self.vector = Vector(i,j,k)
    
    def set_point(self,x,y,z):
        self.point = Point(x,y,z)


class Line(ThirdDimension):

    def __init__(self,p,v):
        self.point = p
        self.vector = v
        return

    def vector(self):
        print(self.vector)

    def points(self):
        print(self.points)

    def parametric_equation(self):
        try:
            x = "\tx(t) = "+str(self.point.x) + " + " + str(self.vector.i)+"t"
            y = "\ty(t) = "+str(self.point.y) + " + " + str(self.vector.j)+"t"
            z = "\tz(t) = "+str(self.point.z) + " + " + str(self.vector.k)+"t"
            print("parametric_equation : ")
            print(x)
            print(y)
            print(z)
        except:
            print("error in parametric eq")

    def vector_equation(self):
        try:
            x = "( "+str(self.point.x) + " + " + str(self.vector.i)+"t ) î"
            y = "( "+str(self.point.y) + " + " + str(self.vector.j)+"t ) k"
            z = "( "+str(self.point.z) + " + " + str(self.vector.k)+"t ) l"
            eq = "\t"+x + " + " + y + " + "+z
            print("vector_equation")
            print(eq)
        except:
            print("error in vector eq")

    def symmetric_equation(self):
        try:
            x = "x - "+str(self.point.x)+" / "+str(self.vector.i)
            y = "y - "+str(self.point.y)+" / "+str(self.vector.j)
            z = "z - "+str(self.point.z)+" / "+str(self.vector.k)
            eq = "\t"+x +"  =  "+y+"  =  "+z
            print("symmetric_equation")
            print(eq)
        except:
            print("error in symmetric eq")




class Plane(ThirdDimension):

    def __init__(self,p):
        self.p = p
        return

    def initiate(self,p,v):
        self.point = p
        self.vector = v
        return

    def point_and_line(self,p,l):
        v2 = p.minus(l.point).to_vector()
        n = v2.cross_product(l.vector)
        self.point = p
        self.vector = n
        return

    def point_point_and_vector(self,p1,p2,v1):
        v2 = p1.minus(p2).to_vector()
        n = v1.cross_product(v2)
        return

    def normal(self):
        print(self.vector)

    def equation(self):
        if self.point & self.vector:
            d = self.vector.i*self.point.x + self.vector.j*self.point.y + self.vector.k*self.point.z
            eq = str(self.vector.i)+"x +" + str(self.vector.j)+"y +"+ str(self.vector.k)+"z = "+str(-1*d)
            print(eq)
        else:
            print("error in equation")

    def extended_equation(self):
        try:
            x = str(self.vector.i)+"(x - "+str(self.point.x)+ " )"
            y = str(self.vector.j)+"(y - "+str(self.point.y)+ " )"
            z = str(self.vector.k)+"(z - "+str(self.point.z)+ " )"
            eq = x+" + "+ y + " + "+z+" + "+" = 0"
            print(eq)
        except:
            print("error in extended equation")


if __name__ == "__main__":
    p1 = Point(5,0,0)
    p2 = Point(5,-1,1)
    v = p1.minus(p2).to_vector()
    l = Line(p1,v)
    l.parametric_equation()
    n1 = Vector(1,1,1)
    n2 = Vector(1,8,8)
    print(n1.angle_between(n2))
    
    
