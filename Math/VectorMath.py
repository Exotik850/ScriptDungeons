from ursina import *

def sub(v1: Vec3, v2: Vec3):
    temp = v1
    temp.x -= v2.x
    temp.y -= v2.y
    temp.z -= v2.z
    return temp