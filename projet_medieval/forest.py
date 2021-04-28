#!/usr/bin/env python3

from transform import translate, identity, scale
from objectLoaders import add_object, ObjectLoadMesh
from random import randint

class Forest():
    def __init__(self, shader):
        super().__init__()
        self.children = []
        self.trees = []
        self.trees.append(ObjectLoadMesh(shader, "./models/nature/FBX/PineTree_1.fbx", (1, 0, 0)))
        self.trees.append(ObjectLoadMesh(shader, "./models/nature/FBX/PineTree_2.fbx", (1, 0, 0)))
        self.trees.append(ObjectLoadMesh(shader, "./models/nature/FBX/PineTree_3.fbx", (1, 0, 0)))
        self.trees.append(ObjectLoadMesh(shader, "./models/nature/FBX/PineTree_4.fbx", (1, 0, 0)))
        self.trees.append(ObjectLoadMesh(shader, "./models/nature/FBX/PineTree_5.fbx", (1, 0, 0)))

    def construct_forest(self, transform=identity()):
        for _ in range(350):
            self.children.extend([add_object(self.trees[randint(0, 4)], transform=transform@translate(randint(0, 10000), randint(0, 4000), 0)@scale(randint(60, 100)))])
