import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pyassimp

# # 윈도우 크기
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600

# def load_model(file_path):
#     scene = pyassimp.load(file_path)
#     if not scene.meshes:
#         raise ValueError("The model does not contain any meshes.")

#     vertices = []
#     for mesh in scene.meshes:
#         vertices.extend(mesh.vertices)

#     indices = [i for face in scene.meshes[0].faces for i in face]

#     return vertices, indices

# def draw_model(vertices, indices):
#     glBegin(GL_TRIANGLES)
#     for i in indices:
#         glVertex3fv(vertices[i])
#     glEnd()

# def main():
#     pygame.init()
#     pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
#     gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)
#     glTranslatef(0.0, 0.0, -5)

#     # fbx 파일 경로 설정
#     model_file = "untitled.fbx"

#     try:
#         vertices, indices = load_model(model_file)
#     except Exception as e:
#         print(f"Error loading the model: {e}")
#         pygame.quit()
#         return

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return

#         glRotatef(1, 3, 1, 1)  # 회전

#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         draw_model(vertices, indices)
#         pygame.display.flip()
#         pygame.time.wait(10)

# if __name__ == "__main__":
#     main()

print("dd")
