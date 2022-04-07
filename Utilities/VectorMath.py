from ursina import *
import math
import random

TWO_PI = 2 * math.pi


def sub(v1: Vec3, v2: Vec3):
    """
    Return the difference between the two vectors
    :param v1: the first vector
    :param v2: the second vector
    :return: the difference between the two vectors
    """
    temp = v1
    temp.x -= v2.x
    temp.y -= v2.y
    temp.z -= v2.z
    return temp


def magnitude(v: Vec3):
    """
    Return the magnitude of the given vector
    :param v: the vector to find the magnitude of
    :return: the magnitude of the given vector
    """
    return (v.x ** 2 + v.y ** 2 + v.z ** 2) ** 0.5


def div(v: Vec3, n: float):
    """
    Return the division of the given vector by the given number
    :param v: Vector3 to divide
    :param n: number to divide by
    :return: divided vector3
    """
    temp = v
    temp.x /= n
    temp.y /= n
    temp.z /= n
    return temp


def normalize(v: Vec3):
    """
    Return the normalized version of the given vector
    :param v: the vector to normalize
    :return: the normalized version of the given vector
    """
    temp = v
    temp.x /= magnitude(temp)
    temp.y /= magnitude(temp)
    temp.z /= magnitude(temp)
    return temp


def randomVec2d() -> Vec2:
    """
    Return a random 2D vector
    :return:
    """
    temp = Vec2(0, 0)
    ang = random.random() * TWO_PI
    r = random.random()
    temp.x = math.cos(ang) * r
    temp.y = math.sin(ang) * r
    return temp


def randomVec3d() -> Vec3:
    """
    Return a random 3D vector
    :return: a random 3D vector
    """
    temp = Vec3(0, 0, 0)
    ang = random.random() * TWO_PI
    r = random.random()
    temp.x = math.cos(ang) * r
    temp.y = math.sin(ang) * r
    temp.z = math.sin(ang) * r
    return temp


# find the distance between two entities
def distance_squared(entity1, entity2):
    """
    Return the distance between two entities squared
    :param entity1: the first entity
    :param entity2: the second entity
    :return: the distance between the two entities squared
    """
    pos1 = entity1.position
    pos2 = entity2.position
    d = (pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2
    return d


def distance(entity1, entity2):
    """
    Return the distance between two entities
    :param entity1: the first entity
    :param entity2: the second entity
    :return: the distance between the two entities
    """
    return distance_squared(entity1, entity2) ** 0.5


# find the closest entity to the given entity
def closest_entity(entity, entities):
    """
    Return the closest entity to the given entity
    :param entity: the entity to find the closest entity to
    :param entities: the list of entities to search through
    :return: the closest entity to the given entity
    """
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
    """
    Return the closest entity to the given entity within a certain range
    :param entity: the entity to find the closest entity to
    :param entities: the list of entities to search through
    :param range: the range to search within
    :return: the closest entity to the given entity within the given range
    """
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
