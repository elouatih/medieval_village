#!/usr/bin/env python3

from transform import rotate, translate, scale, identity
from math import atan, degrees

from core import Node
from objectLoaders import ObjectLoadMesh, add_object

class Castle(Node):
    def __init__(self, shader_materials):
        super().__init__()
        self.children = []
        self.tower = ObjectLoadMesh(shader_materials, './models/objects/FBX/Simpletower.fbx', (1, 1, 1))
        self.wall = ObjectLoadMesh(shader_materials, './models/objects/FBX/Wall.fbx', (1, 1, 1))
        self.large_tower = ObjectLoadMesh(shader_materials, './models/objects/FBX/LargeSimpleTower.fbx', (1, 1, 1))
        self.door = ObjectLoadMesh(shader_materials, './models/objects/FBX/Door.fbx', (1, 1, 1))
        self.tunnel = ObjectLoadMesh(shader_materials, './models/objects/FBX/Tunnel.fbx', (1, 1, 1))
        self.bridge = ObjectLoadMesh(shader_materials, './models/objects/FBX/Bridge.fbx', (1, 1, 1))
        self.tree = ObjectLoadMesh(shader_materials, './models/nature/FBX/CommonTree_Autumn_1.fbx', (1, 1, 1))

    def construct_castle(self, transform=identity()):
        objects = []
        # ADD TOWERS
        objects.append(add_object(self.tower, transform=transform@translate(4, 7, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(0, 7, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(-5, 5.5, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(-7, -2, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(-3, -9, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(2, -7.5, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(6, -6.5, 0)@scale(1.5)))
        objects.append(add_object(self.tower, transform=transform@translate(5, 0, 0)@scale(1.5)))

        # ADD WALLS
        objects.append(add_object(self.wall, transform=transform@translate(2, 7, 0)@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-2.5, 6.25, 0)@rotate((0, 0, 1), 180+degrees(atan(1.5/5.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-5.5, 3.5, 0)@rotate((0, 0, 1), 180+degrees(atan(7.5/2.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-6.5, 0, 0)@rotate((0, 0, 1), 180+degrees(atan(7.5/2.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-6, -3.75, 0)@rotate((0, 0, 1), 180+60+degrees(atan(7.0/4.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-4, -7, 0)@rotate((0, 0, 1), 180+60+degrees(atan(7.0/4.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(-.5, -8.25, 0)@rotate((0, 0, 1), 180+180+degrees(atan(1.5/5.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(4, -7, 0)@rotate((0, 0, 1), 180+180+degrees(atan(1.5/5.0)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(5.25, -1.75, 0)@rotate((0, 0, 1), 180+270+degrees(atan(1/7)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(5.75, -5, 0)@rotate((0, 0, 1), 180+270+degrees(atan(1/7)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(5, 1.75, 0)@rotate((0, 0, 1), 180+270+degrees(atan(1/7)))@scale(2.5)))
        objects.append(add_object(self.wall, transform=transform@translate(4.5, 5, 0)@rotate((0, 0, 1), 180+270+degrees(atan(1/7)))@scale(2.5)))

        #ADD LARGE TOWERS & TUNNEL & BRIDGE
        objects.append(add_object(self.tower, transform=transform@translate(-1.5, 3, 0)@scale(2.5)))
        objects.append(add_object(self.tower, transform=transform@translate(1.5, 4, 0)@scale(3)))
        objects.append(add_object(self.tower, transform=transform@translate(2, -3, 0)@scale(3.5)))
        objects.append(add_object(self.tunnel, transform=transform@translate(-6, -6.5, 0)@rotate((0, 0, 1), 180+180+60+degrees(atan(7.0/4.0)))@scale(2.5)))
        objects.append(add_object(self.bridge, transform=transform@translate(-6.66, -7.15, 0)@rotate((0, 0, 1), +180+60+degrees(atan(7.0/4.0)))@scale(2.5)))

        #ADD TREE
        objects.append(add_object(self.tree, transform=transform@translate(-3, -3, 0)@scale(3)))
        objects.append(add_object(self.wall, transform=transform@translate(2, .5, 0)@rotate((0, 0, 1), 270+degrees(atan(1/7)))@scale(3.5)))

        # ADD OBJECTS TO CASTLE' CHILDREN
        self.children.extend(objects)
