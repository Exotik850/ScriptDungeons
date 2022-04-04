from ursina import *
import math
import random
TWO_PI = 2*math.pi

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

def randomVec2d() -> Vec2:
    temp = Vec2(0,0)
    ang = random.random() * TWO_PI
    r = random.random()
    temp.x = math.cos(ang) * r
    temp.y = math.sin(ang) * r
    return temp
