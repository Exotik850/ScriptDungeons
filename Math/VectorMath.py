from ursina import *

def sub(v1: Vec3, v2: Vec3):
    temp = v1
    temp.x -= v2.x
    temp.y -= v2.y
    temp.z -= v2.z
    return temp

def div(v: Vec3, n: float):
    temp = v
    temp.x /= n
    temp.y /= n
    temp.z /= n
    return temp

def normalize(v: Vec3):
    temp = v
    temp.x /= temp.magnitude
    temp.y /= temp.magnitude
    temp.z /= temp.magnitude
    return temp