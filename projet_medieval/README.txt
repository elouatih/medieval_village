------- PROJET GRAPHIQUE 3D : CITE MEDIEVALE --------

# Requirements
- Python 3.5 (voir 3D Graphics -> FAQ)
- GLFW et Assimp et clang (voir 3D Graphics -> FAQ)
- AssimpCy (voir 3D Graphics -> FAQ)
- PyOpenGL

- PyOpenAL : pip install PyOpenAL (pour ajouter du son à la scène)
  ################### IMPORTANT : #############################
  si l'installation de la bibliothèque PyOpenAL n'est pas réussie,
  le projet ne peut pas être lancé. Dans ce cas, il est possible d'ouvrir la scène sans
  activer le son. Il suffit de commenter les lignes du fichier core.py :
            >>> ligne 10 : import openal as AL
                    ...
            >>> ligne 204 : source = AL.oalOpen("lotr.wav")
            >>> ligne 205 : source.play()
                    ...
            >>> ligne 223 : AL.oalQuit()
                    ...
            >>> ligne 234 : if key == glfw.KEY_A:
            >>> ligne 235 :    AL.oalQuit()
            >>> ligne 236 : if key == glfw.KEY_S:
            >>> ligne 237 :    source = AL.oalOpen("lotr.wav")
            >>> ligne 238 :    source.play()


# Running the project

Ligne de commande : >>> cd projet_medieval
                    >>> python3 scene.py

# Keyboard settings

Action               | QWERTY     | AZERTY
---------------------------------------------
Quitter la scène     | Q - ESCAPE | A - ESCAPE
Animer un personnage | SPACE      | SPACE
Arrêter le son       | A          | Q
Relancer le son      | S          | S
(Le son est lancé par défaut au lancement de la scène)



