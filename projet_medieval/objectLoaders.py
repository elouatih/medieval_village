#!/usr/bin/env python3
from transform import identity
from core import Node
from loaders import load_phong_textured, load_phong_mesh, load_skinned

# Create a node object and add to it an object
def add_object(object, transform=identity()):
    obj = Node(transform=transform)
    obj.add(object)
    return obj

class ObjectLoadTextured(Node):
    def __init__(self, shader, file, light_dir):
        super().__init__()
        self.add(*load_phong_textured(file, shader, light_dir))

class ObjectLoadMesh(Node):
    def __init__(self, shader, file, light_dir):
        super().__init__()
        self.add(*load_phong_mesh(file, shader, light_dir))

class ObjectLoadSkinned(Node):
    def __init__(self, shader, file, light_dir):
        super().__init__()
        self.add(*load_skinned(file, shader, light_dir))
