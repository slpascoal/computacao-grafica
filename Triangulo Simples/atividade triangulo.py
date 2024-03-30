import glfw
from OpenGL.GL import *
import numpy as np

def key_pressed(window, key, scancode, action, mods):
    
    if key == glfw.KEY_W and action == glfw.PRESS:
        global vertices
        angle = np.radians(10)
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0.0],
                                     [np.sin(angle), np.cos(angle), 0.0],
                                     [0.0, 0.0, 1.0]])
        vertices = np.dot(vertices.reshape(-1, 3), rotation_matrix).flatten()
        glVertexPointer(3, GL_FLOAT, 0, vertices)

if not glfw.init():
    raise Exception("GLFW não pode ser inicializado")

window = glfw.create_window(1280, 720, "Um triângulo grande e 'não cinza'", None, None)

if not window:
    glfw.terminate()
    raise Exception("GLFW não pode ser criado")

glfw.set_window_pos(window, 400, 100)
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.5, 0.5, 0.0
            ]

colors = [1.0, 0.0, 0.0,
          1.0, 0.0, 0.0,
          0.0, 0.0, 1.0
          ]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glfw.set_key_callback(window, key_pressed)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)
glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)
glClearColor(0, 0.1, 0.1, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)

glfw.terminate()
