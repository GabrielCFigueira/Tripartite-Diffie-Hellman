#!/usr/bin/python3

import math
from pynitefields import *

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def isInfinity(self):
        return False

    def printPoint(self):
        if(self.isInfinity()):
            print("Point at Infinity")
        else:
            print("X: " + convertListToString(self.x.exp_coefs) + "  Y: " + convertListToString(self.y.exp_coefs))


class PointAtInfinity(Point):
    def __init__(self):
        super().__init__()

    def isInfinity(self):
        return True


class EllipticCurve:
    def __init__(self,a,b):
        self.a = a
        self.b = b


#Elliptic curve operations

def negatePoint(p):
    return Point(p.x, p.y - 2 * p.y)

def addPoint(p, q, curve):
    if p.isInfinity():
        return q
    elif q.isInfinity():
        return p
    elif p.x == q.x and p.y == q.y - 2 * q.y:
        return PointAtInfinity()
    elif p.x == q.x and q.y == p.y:
        slope = (3 * pow(p.x, 2) + curve.a) / (2 * p.y)
    else:
        slope = (q.y - p.y) / (q.x - p.x)
    x = slope ** 2 - p.x - q.x
    y = slope * (p.x - x) - p.y
    return Point(x,y)

def getBinary(integer):
    return [int(n) for n in bin(integer)[2:]]

def doubleAndAdd(p, n, curve):
    binary = getBinary(n)
    r = PointAtInfinity()
    q = p
    i = len(binary) - 1
    while i >= 0:
        if binary[i] == 1:
            r = addPoint(r, q, curve)
        q = addPoint(q, q, curve)
        i -= 1
    return r


# Miller Algorithm

def computeFunction(p, q, value, curve):
    if (p.x == q.x and p.y == q.y - 2 * q.y) or p.isInfinity() or q.isInfinity():
        if p.isInfinity():
            return value.x - q.x
        else:
            return value.x - p.x
    elif p.x == q.x and p.y == q.y:
        slope = (3 * pow(p.x, 2) + curve.a) / (2 * p.y)
    else:
        slope = (p.y - q.y) / (p.x - q.x)
    return (value.y - p.y + slope * (p.x - value.x)) / (value.x + p.x + q.x - pow(slope, 2))


def Miller(p, order, value, curve):
    res = 1
    v = p
    binary = getBinary(order)
    i = len(binary) - 2
    while i >= 0:
        dv = addPoint(v, v, curve)
        res = res ** 2 * computeFunction(v, v, value, curve) #/ computeFunction(dv, negatePoint(dv), value, curve)
        v = dv
        if binary[i] == 1:
            vp = addPoint(v, p, curve)
            res = res * computeFunction(v, p, value, curve) #/ computeFunction(vp, negatePoint(vp), value, curve)
            v = vp
        i = i - 1
    return res

def WeilPairing(p, q, s, order, curve):
    a = Miller(p,order,addPoint(q,s,curve),curve)
    b = Miller(p,order,s,curve)
    c = Miller(q,order,addPoint(p, negatePoint(s), curve),curve)
    d = Miller(q,order,negatePoint(s),curve)


    #e = Miller(p,order,q,curve)
    #f = Miller(q,order,p,curve)
    #print(e)
    #print(f)
    #print(e / f)
    print(a)
    print(b)
    print(c)
    print(d)
    return a * d / (b * c)


## Main and other functions

def convertListToString(input_seq):
    i = 0
    final_str = "["
    while(True):
        final_str += " " + str(input_seq[i]) + " "
        i += 1
        if(i == len(input_seq)):
            final_str += "]"
            break
        final_str += ";"
    return final_str

if __name__ == "__main__":
    gf = GaloisField(17)
    p = Point(gf[9],gf[15])
    #q = Point(gf[49],gf[20])
    #s = Point(gf[0],gf[0])
    ec = EllipticCurve(gf[0],gf[7])

    doubleAndAdd(p,15,ec).printPoint()
