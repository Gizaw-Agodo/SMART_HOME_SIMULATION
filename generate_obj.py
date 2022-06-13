from OpenGL.GL import *
 
def generate(object):
    object.gl_list = glGenLists(1)
    glNewList(object.gl_list, GL_COMPILE)
    glEnable(GL_TEXTURE_2D)
    glFrontFace(GL_CCW)
    for face in object.faces:
        vertices, normals, texture_coords, material = face

        mtl = object.mtl[material]
        if 'texture_Kd' in mtl:
            glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
        else:
            glColor(*mtl['Kd'])

        glBegin(GL_POLYGON)
        for i in range(len(vertices)):
            if normals[i] > 0:
                glNormal3fv(object.normals[normals[i] - 1])
            if texture_coords[i] > 0:
                glTexCoord2fv(object.texcoords[texture_coords[i] - 1])
            glVertex3fv(object.vertices[vertices[i] - 1])
        glEnd()
    glDisable(GL_TEXTURE_2D)
    glEndList()
