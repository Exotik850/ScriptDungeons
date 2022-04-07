from ursina import *
import math
import random

TWO_PI = 2 * math.pi


def sub(v1: Vec3, v2: Vec3):
    temp = v1
    temp.x -= v2.x
    temp.y -= v2.y
    temp.z -= v2.z
    return temp


def magnitude(v: Vec3):
    return (v.x ** 2 + v.y ** 2 + v.z ** 2) ** 0.5


def div(v: Vec3, n: float):
    temp = v
    temp.x /= n
    temp.y /= n
    temp.z /= n
    return temp


def normalize(v: Vec3):
    temp = v
    temp.x /= magnitude(temp)
    temp.y /= magnitude(temp)
    temp.z /= magnitude(temp)
    return temp


def randomVec2d() -> Vec2:
    temp = Vec2(0, 0)
    ang = random.random() * TWO_PI
    r = random.random()
    temp.x = math.cos(ang) * r
    temp.y = math.sin(ang) * r
    return temp


def randomVec3d() -> Vec3:
    temp = Vec3(0, 0, 0)
    ang = random.random() * TWO_PI
    r = random.random()
    temp.x = math.cos(ang) * r
    temp.y = math.sin(ang) * r
    temp.z = math.sin(ang) * r
    return temp


# find the distance between two entities
def distance_squared(entity1, entity2):
    pos1 = entity1.position
    pos2 = entity2.position
    d = (pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2
    return d


def distance(entity1, entity2):
    return distance_squared(entity1, entity2) ** 0.5


# find the closest entity to the given entity
def closest_entity(entity, entities):
    closest = None
    for ent in entities:
        if ent == entity:
            continue
        if closest is None:
            closest = ent
        elif distance(entity, ent) < distance(closest, ent):
            closest = ent
    return closest


# find the closest entity to the given entity within a certain range
def closest_entity_within_range(entity, entities, range):
    closest = None
    for ent in entities:
        if ent == entity:
            continue
        if distance(entity, ent) < range:
            if closest is None:
                closest = ent
            elif distance(entity, ent) < distance(closest, ent):
                closest = ent
    return closest
