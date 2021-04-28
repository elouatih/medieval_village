#!/usr/bin/env python3

from core import Node
from transform import rotate, translate, identity, scale
from objectLoaders import ObjectLoadTextured, add_object, ObjectLoadMesh
from random import random, randint
from skinning_mesh import KeyFrameControlNode, KeyFrames, TransformKeyFrames

light_dir = (-1, -1, -1)

class Town(Node):
    def __init__(self, shader_1, shader_2):
        super().__init__()
        self.children = []
        self.tower = ObjectLoadTextured(shader_1, './models/RTS/tower.FBX', light_dir)
        self.wall = ObjectLoadTextured(shader_1, './models/RTS/casstle_wall.FBX', light_dir)
        self.big_house = ObjectLoadTextured(shader_1, './models/RTS/big_house.FBX', light_dir)
        self.church = ObjectLoadTextured(shader_1, 'models/RTS/church.FBX', light_dir)
        self.rock_wall = ObjectLoadTextured(shader_1, 'models/RTS/rock_wall_small.FBX', light_dir)
        self.trees = [ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_1.fbx', light_dir),
                      ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_2.fbx', light_dir),
                      ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_3.fbx', light_dir),
                      ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_4.fbx', light_dir),
                      ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_5.fbx', light_dir),
                      ObjectLoadMesh(shader_2, 'models/nature/FBX/CommonTree_Autumn_1.fbx', light_dir)]

    def construct_houses(self, shader_1, shader_2, transform=identity()):
        big_houses= []
        for j in range(0, 5, 2):
            if(j % 4 == 2):
                for i in range(0, 5, 2):
                    big_houses.append(add_object(self.big_house, transform=transform@translate(100*i, 100*j, 0)@rotate((0, 0, 1), random()*180)))
            elif(j % 4 == 0):
                for i in range(1, 4, 2):
                    big_houses.append(add_object(self.big_house, transform=transform@translate(100*i, 100*j, 0)@rotate((0, 0, 1), random()*90)))
            else :
                pass
        #self.children.extend([add_object(self.trees['autumn_tree'], shader_2, transform=transform@translate(100*3, 100*1, 0)@scale(50))])
        self.children.extend(big_houses)

    def construct_town(self, shader, shader_2, transform=identity()):
        towers = []
        castle_walls = []
        towers.append(add_object(self.tower, transform=transform@translate(32.5*20, 33*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(87.5*20, 33*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(115*20, 33*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(172.5*20, 33*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(172.5*20, 105*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(172.5*20, 129*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(172.5*20, 159*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(172.5*20, 187.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(75*20, 187.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(20*20, 162.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(20*20, 131.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(20*20, 120.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(20*20, 92.5*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(120*20, 185*20, 0)@scale(2)@rotate((1,0,0),90)))
        towers.append(add_object(self.tower, transform=transform@translate(140*20, 185*20, 0)@scale(2)@rotate((1,0,0),90)))

        self.children.extend(towers)

        for i in range(33*20, 87*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, 38*20, -100)@scale(2)@rotate((1,0,0),90)))
        for i in range(115*20, 172*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, 38*20, -100)@scale(2)@rotate((1,0,0),90)))

        for j in range(37*20, 105*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(172*20, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0, 1, 0),90)))
        for j in range(105*20, 130*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(172*20, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0, 1, 0),90)))

        for j in range(162*20, 187*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(172*20, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0, 1, 0),90)))

        for i in range(75*20, 120*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, 190*20, -100)@scale(2)@rotate((1,0,0),90)))

        for i in range(140*20, 172*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, 190*20, -100)@scale(2)@rotate((1,0,0),90)))

        j = 166.5*20
        for i in range(20*20, 73*20, 9):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0,1,0), 24.44)))
            j = j + 4

        for j in range(96*20, 121*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(18*20, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0, 1, 0),90)))

        for j in range(134*20, 164*20, 100):
            castle_walls.append(add_object(self.wall, transform=transform@translate(18*20, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0, 1, 0),90)))

        j = 92*20
        for i in range(20*20, 32*20, 21):
            castle_walls.append(add_object(self.wall, transform=transform@translate(i, j, -100)@scale(2)@rotate((1,0,0),90)@rotate((0,1,0), 90+11.86)))
            j = j - 99

        self.construct_houses(shader, shader_2, transform=translate(700, 1000, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(650, 150, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(700, -1000, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(-200, 1000, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(100, -700, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(-1000, 720, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(-1250, 0, 0)@scale(1.5))
        self.construct_houses(shader, shader_2, transform=translate(-1200, -1000, 0)@scale(1.5))

        for _ in range(50):
            x = randint(-1300, 1300)
            y = randint(-1200, 1400)
            self.children.extend([add_object(self.trees[randint(0,3)], transform=translate(x, y, 0)@scale(randint(40, 70)))])

        self.children.extend([add_object(self.trees[-1], translate(40, 40, 0)@scale(120))])

        self.children.extend([add_object(self.church, transform=translate(-150, -400, 0)@rotate((0, 0, 1), 180)@scale(2))])

        self.children.extend(castle_walls)

        for i in range(-220, 200, 100):
            self.children.extend([add_object(self.rock_wall, transform=translate(i, 600, 5)@scale(2))])
            self.children.extend([add_object(self.rock_wall, transform=translate(i, 0, 5)@scale(2))])
        for i in range(100, 600, 100):
            self.children.extend([add_object(self.rock_wall, transform=translate(-300, i, 5)@scale(2)@rotate((0, 0, 1), 90))])
        for i in range(300, 400, 100):
            self.children.extend([add_object(self.rock_wall, transform=translate(500, i, 5)@scale(2)@rotate((0, 0, 1), 90))])

        self.children.extend([add_object(self.rock_wall, transform=translate(450, 150, 5)@scale(2)@rotate((0, 0, 1), 90-45))])
        self.children.extend([add_object(self.rock_wall, transform=translate(350, 50, 5)@scale(2)@rotate((0, 0, 1), 90-45))])
        self.children.extend([add_object(self.rock_wall, transform=translate(450, 450, 5)@scale(2)@rotate((0, 0, 1), 90+45))])
        self.children.extend([add_object(self.rock_wall, transform=translate(350, 550, 5)@scale(2)@rotate((0, 0, 1), 90+45))])
