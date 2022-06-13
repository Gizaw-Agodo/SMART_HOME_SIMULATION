import os
from OpenGL.GL import *
from load_material import *

class Object:

    def __init__(self, filename):
        dirname = os.path.dirname(filename)
        self.texcoords = []
        self.vertices = []
        self.normals = []
        self.faces = []
        self.gl_list = 0
        material = None

        for line in open('' + filename, "r"):
            if line.startswith('#'):
                continue
            values = line.split()
            if not values:
                continue
           
            if values[0] == 'v':
                value = list(map(float, values[1:4]))
                self.vertices.append(value)
          
            elif values[0] == 'vn':
                value = list(map(float, values[1:4]))
                self.normals.append(value)
            
            elif values[0] == 'vt':
                value = list(map(float, values[1:3]))
                self.texcoords.append(value)
            
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            
            elif values[0] == 'mtllib':
                path = os.path.join(dirname, values[1])
                self.mtl = loadMaterial(path)
            
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

    def render(self):
        glCallList(self.gl_list)

