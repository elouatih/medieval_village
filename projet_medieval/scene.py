#!/usr/bin/env python3

from core import Viewer, Shader
from castle import Castle
from town import Town
from transform import translate, scale, rotate, vec, quaternion
import glfw
from forest import Forest
from objectLoaders import ObjectLoadSkinned, ObjectLoadTextured, add_object
from skinning_mesh import KeyFrameControlNode, KeyFrames, TransformKeyFrames

light_dir = (-1, -1, -1)

def scene(viewer, shader_materials, shader_texture, shader_skinned):
    size = 10000
    """ -------------- create a scene and add objects ------------------- """
    # create ground object and add it to the viewer
    main_ground = ObjectLoadTextured(shader_texture, 'models/models_OBJ/Ground.obj', light_dir)
    viewer.add(add_object(main_ground))

    # create mountain instances and add them to the viewer
    mountain = ObjectLoadTextured(shader_texture, 'models/models_OBJ/Mountain.obj', light_dir)
    x_mountains = [-0.80, -0.80, 0.80, 0.80]
    y_mountains = [-0.80, 0.80, -0.80, 0.80]
    scales = [250, 230, 220, 200]
    rotation = rotate((1, 0, 0), 90)
    for x, y, z in zip(x_mountains, y_mountains, scales):
        viewer.add(add_object(mountain, translate(x*size, y*size, -100)@rotation@scale(z)))

    # create skybox and add it to the viewer
    skybox = ObjectLoadTextured(shader_texture, 'models/models_OBJ/SkyBox.obj', light_dir)
    viewer.add(add_object(skybox))

    # create a town and add it to the viewer
    town = Town(shader_texture, shader_materials)
    town.construct_town(shader_texture, shader_materials, translate(-0.2*size, -0.2*size, 175))
    viewer.add(*town.children)

    # create town ground and church ground
    town_ground = ObjectLoadTextured(shader_texture, 'models/models_OBJ/GroundTown.obj', light_dir)
    church_ground = ObjectLoadTextured(shader_texture, 'models/models_OBJ/church_ground.obj', light_dir)
    viewer.add(add_object(town_ground, translate(-0.2*size, -0.2*size, 2)))
    viewer.add(add_object(church_ground, translate(-0.03*size, 0.06*size, 5)@rotate((0, 0, 1), -90)))

    # create forests
    forest = Forest(shader_materials)
    forest.construct_forest(translate(-2500, -6000, 0))
    viewer.add(*forest.children)

    # create a worker
    rotation = rotate((1, 0, 0), 90)@rotate((0, 1, 0), 90)@scale(0.5)
    worker = ObjectLoadSkinned(shader_skinned, 'models/characters/worker/worker_cutting_down.FBX', (-1, 0, 0))
    viewer.add(add_object(worker, transform=rotation))

    # create town's guards
    guard = ObjectLoadSkinned(shader_skinned, 'models/characters/armored_swordman/armored_swordman_standing.FBX', (-1, 0, 0))
    transformation = translate(-0.2*size, -0.2*size, 0)

    translations = [translate(32.5*20, 33*20-50, 0), translate(87.5*20, 33*20-50, 0),
                    translate(115*20, 33*20-50, 0), translate(172.5*20, 33*20-50, 0),
                    translate(172.5*20+100, 105*20, 0), translate(172.5*20+100, 129*20, 0),
                    translate(172.5*20+100, 159*20, 0), translate(172.5*20+100, 187.5*20, 0),
                    translate(75*20, 187.5*20+50, 0), translate(20*20, 162.5*20+50, 0),
                    translate(20*20, 131.5*20+50, 0), translate(20*20, 120.5*20+50, 0),
                    translate(20*20-100, 92.5*20, 0), translate(120*20-100, 185*20, 0),
                    translate(140*20-100, 185*20, 0)]
    for t in translations:
        viewer.add(add_object(guard, transform=transformation@t@rotation))

    # create a non flat ground
    non_flat = ObjectLoadTextured(shader_texture, 'models/models_OBJ/terre_eleve.obj', light_dir)
    viewer.add(add_object(non_flat, transform=translate(0.10*size, 0.35*size, 0)))

    # create a castle
    castle = Castle(shader_materials)
    castle.construct_castle(transform=translate(0.10*size, 0.35*size, 400)@scale(40))
    viewer.add(*castle.children)

    # add an animated door
    translate_keys = {0: vec(0, 0, 300) , 4: vec(0, 0, 100)}
    scale_keys = {0: 1, 4: 1}
    rotate_keys = {0: quaternion(), 4: quaternion()}
    door = ObjectLoadTextured(shader_texture, 'models/models_OBJ/door.obj', light_dir)
    keynode = KeyFrameControlNode(translate_keys, rotate_keys, scale_keys)
    keynode.add(add_object(door, translate(30, -1300, 0)@rotate((0, 1, 0), 90)@rotate((1, 0, 0), -90)))
    viewer.add(keynode)

def main():
    viewer = Viewer()
    shader_1 = Shader("shaders/texture.vert", "shaders/texture.frag")
    shader_2 = Shader("shaders/phong.vert", "shaders/phong.frag")
    shader_3 = Shader("shaders/skinning.vert", "shaders/texture.frag")
    scene(viewer, shader_2, shader_1, shader_3)
    viewer.run()

if __name__ == '__main__':
    glfw.init()                # initialize window system glfw
    main()                     # main function keeps variables locally scoped
    glfw.terminate()           # destroy all glfw windows and GL contexts
