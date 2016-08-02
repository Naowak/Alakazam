import sys
sys.path.append("./../map")

import pygame
import Location
import math as m
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from enum import Enum
import time
import array

# class Angle(Enum) :
# 	left = 0
# 	top_left = 1
# 	top_right = 2
# 	right = 3
# 	bottom_right = 4
# 	bottom_left = 5

grey_dark = (0.6, 0.6, 0.6)
grey_shiny = (0.8, 0.8, 0.8)

SIZE = 1



# def new_vertices(i, j, angle) :
# 	y_BOTTOM = 0
# 	y_TOP = 0.5

# 	if angle == Angle.left :
# 		return (SIZE * (i + -1), SIZE * y_BOTTOM, SIZE * (j + 0))
# 	elif angle == Angle.top_left :
# 		return (SIZE * (i + -1/2), SIZE * y_BOTTOM, SIZE * (j + m.sqrt(3)/2))
# 	elif angle == Angle.top_right :
# 		return (SIZE * (i + 1/2), SIZE * y_BOTTOM, SIZE * (j + m.sqrt(3)/2))
# 	elif angle == Angle.right :
# 		return (SIZE * (i + 1), SIZE * y_BOTTOM, SIZE * (j + 0))
# 	elif angle == Angle.bottom_right :
# 		return (SIZE * (i + 1/2), SIZE * y_BOTTOM, SIZE * (j + -m.sqrt(3)/2))
# 	elif angle == Angle.bottom_left :
# 		return (SIZE * (i + -1/2), SIZE * y_BOTTOM, SIZE * (j + -m.sqrt(3)/2))

# def line_top(i, j, i_size) :
# 	return j*(2*i_size + 2) + 2*i

# def line_bot(i, j, i_size) :
# 	return (j+1)*(2*i_size + 2) + 2*i

# def vertex_number(i, j, i_size, angle) :
# 	if angle == Angle.left :
# 		return line_top(i, j, i_size) + (-1 if j!=0 and j%2==0 else 0)
# 	elif angle == Angle.top_left :
# 		return line_top(i, j, i_size) + (0 if j!=0 and j%2==0 else 1)
# 	elif angle == Angle.top_right :
# 		return line_top(i, j, i_size) + (1 if j!=0 and j%2==0 else 2)
# 	elif angle == Angle.right :
# 		return line_bot(i, j, i_size) + (1 if j%2==0 else 2)
# 	elif angle == Angle.bottom_right :
# 		return line_bot(i, j, i_size) + (0 if j%2==0 else 1)
# 	elif angle == Angle.bottom_left :
# 		return line_bot(i, j, i_size) + (-1 if j%2==0 else 0)

# def HexGrid3D(i_size, j_size) :
# 	vertices = list()
# 	nb_vertices = (2*i_size + 2) * (j_size+1) - 2
# 	for i in range(nb_vertices) :
# 		vertices += [0]
# 	edges = list()
# 	cells = list()

# 	for j in range(j_size) :
# 		if j == 0 :
# 			for i in range(i_size) :
# 				(pos_x, pos_z) = location_to_coord(Location.Location(i,j))
# 				if i == 0 :
# 					vertices[vertex_number(i, j, i_size, Angle.left)] = new_vertices(pos_x, pos_z, Angle.left)
# 					vertices[vertex_number(i, j, i_size, Angle.top_left)] = new_vertices(pos_x, pos_z, Angle.top_left)
# 					vertices[vertex_number(i, j, i_size, Angle.top_right)] = new_vertices(pos_x, pos_z, Angle.top_right)
# 					vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 					vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)
# 					vertices[vertex_number(i, j, i_size, Angle.bottom_left)] = new_vertices(pos_x, pos_z, Angle.bottom_left)

# 					cells.append((vertex_number(i, j, i_size, Angle.left), 
# 						vertex_number(i, j, i_size, Angle.top_left), 
# 						vertex_number(i, j, i_size, Angle.top_right), 
# 						vertex_number(i, j, i_size, Angle.right), 
# 						vertex_number(i, j, i_size, Angle.bottom_right), 
# 						vertex_number(i, j, i_size, Angle.bottom_left)))

# 					edges.append((vertex_number(i, j, i_size, Angle.left),vertex_number(i, j, i_size, Angle.top_left)))
# 					edges.append((vertex_number(i, j, i_size, Angle.top_left),vertex_number(i, j, i_size, Angle.top_right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.top_right),vertex_number(i, j, i_size, Angle.right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.right),vertex_number(i, j, i_size, Angle.bottom_right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.bottom_right),vertex_number(i, j, i_size, Angle.bottom_left)))
# 					edges.append((vertex_number(i, j, i_size, Angle.bottom_left),vertex_number(i, j, i_size, Angle.left)))

# 				else :
# 					vertices[vertex_number(i, j, i_size, Angle.top_left)] = new_vertices(pos_x, pos_z, Angle.top_left)
# 					vertices[vertex_number(i, j, i_size, Angle.top_right)] = new_vertices(pos_x, pos_z, Angle.top_right)
# 					vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 					vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)

# 					cells.append((vertex_number(i, j, i_size, Angle.left), 
# 						vertex_number(i, j, i_size, Angle.top_left), 
# 						vertex_number(i, j, i_size, Angle.top_right), 
# 						vertex_number(i, j, i_size, Angle.right), 
# 						vertex_number(i, j, i_size, Angle.bottom_right), 
# 						vertex_number(i, j, i_size, Angle.bottom_left)))

# 					edges.append((vertex_number(i, j, i_size, Angle.left), vertex_number(i, j, i_size, Angle.top_left)))
# 					edges.append((vertex_number(i, j, i_size, Angle.top_left), vertex_number(i, j, i_size, Angle.top_right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.top_right), vertex_number(i, j, i_size, Angle.right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.right), vertex_number(i, j, i_size, Angle.bottom_right)))
# 					edges.append((vertex_number(i, j, i_size, Angle.bottom_right), vertex_number(i, j, i_size, Angle.bottom_left)))

# 		else :
# 			for i in range(i_size) :
# 				(pos_x, pos_z) = location_to_coord(Location.Location(i,j))
# 				if i == 0 :
# 					if j % 2 == 0 :
# 						vertices[vertex_number(i, j, i_size, Angle.left)] = new_vertices(pos_x, pos_z, Angle.left)
# 						vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_left)] = new_vertices(pos_x, pos_z, Angle.bottom_left)

# 						cells.append((vertex_number(i, j, i_size, Angle.left), 
# 							vertex_number(i, j, i_size, Angle.top_left), 
# 							vertex_number(i, j, i_size, Angle.top_right), 
# 							vertex_number(i, j, i_size, Angle.right), 
# 							vertex_number(i, j, i_size, Angle.bottom_right), 
# 							vertex_number(i, j, i_size, Angle.bottom_left)))

# 						edges.append((vertex_number(i, j, i_size, Angle.left),vertex_number(i, j, i_size, Angle.top_left)))
# 						edges.append((vertex_number(i, j, i_size, Angle.top_right),vertex_number(i, j, i_size, Angle.right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.right),vertex_number(i, j, i_size, Angle.bottom_right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_right),vertex_number(i, j, i_size, Angle.bottom_left)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_left),vertex_number(i, j, i_size, Angle.left)))

# 					else :
# 						vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_left)] = new_vertices(pos_x, pos_z, Angle.bottom_left)

# 						cells.append((vertex_number(i, j, i_size, Angle.left), 
# 							vertex_number(i, j, i_size, Angle.top_left), 
# 							vertex_number(i, j, i_size, Angle.top_right), 
# 							vertex_number(i, j, i_size, Angle.right), 
# 							vertex_number(i, j, i_size, Angle.bottom_right), 
# 							vertex_number(i, j, i_size, Angle.bottom_left)))

# 						edges.append((vertex_number(i, j, i_size, Angle.top_right),vertex_number(i, j, i_size, Angle.right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.right),vertex_number(i, j, i_size, Angle.bottom_right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_right),vertex_number(i, j, i_size, Angle.bottom_left)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_left),vertex_number(i, j, i_size, Angle.left)))
# 				else :
# 					if i == i_size - 1 and j % 2 != 0 :
# 						vertices[vertex_number(i, j, i_size, Angle.top_right)] = new_vertices(pos_x, pos_z, Angle.top_right)
# 						vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)

# 						cells.append((vertex_number(i, j, i_size, Angle.left), 
# 							vertex_number(i, j, i_size, Angle.top_left), 
# 							vertex_number(i, j, i_size, Angle.top_right), 
# 							vertex_number(i, j, i_size, Angle.right), 
# 							vertex_number(i, j, i_size, Angle.bottom_right), 
# 							vertex_number(i, j, i_size, Angle.bottom_left)))

# 						edges.append((vertex_number(i, j, i_size, Angle.top_left),vertex_number(i, j, i_size, Angle.top_right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.top_right),vertex_number(i, j, i_size, Angle.right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.right),vertex_number(i, j, i_size, Angle.bottom_right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_right),vertex_number(i, j, i_size, Angle.bottom_left)))

# 					else :
# 						vertices[vertex_number(i, j, i_size, Angle.right)] = new_vertices(pos_x, pos_z, Angle.right)
# 						vertices[vertex_number(i, j, i_size, Angle.bottom_right)] = new_vertices(pos_x, pos_z, Angle.bottom_right)

# 						cells.append((vertex_number(i, j, i_size, Angle.left), 
# 							vertex_number(i, j, i_size, Angle.top_left), 
# 							vertex_number(i, j, i_size, Angle.top_right), 
# 							vertex_number(i, j, i_size, Angle.right), 
# 							vertex_number(i, j, i_size, Angle.bottom_right), 
# 							vertex_number(i, j, i_size, Angle.bottom_left)))

# 						edges.append((vertex_number(i, j, i_size, Angle.top_right),vertex_number(i, j, i_size, Angle.right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.right),vertex_number(i, j, i_size, Angle.bottom_right)))
# 						edges.append((vertex_number(i, j, i_size, Angle.bottom_right),vertex_number(i, j, i_size, Angle.bottom_left)))


# 	for cell in cells :
# 		glBegin(GL_POLYGON)
# 		glColor3fv(grey_dark)
# 		for vertex in cell :
# 			glVertex3fv(vertices[vertex])
# 		glEnd()

# 	for edge in edges :
# 		glBegin(GL_LINES)
# 		glColor3fv(grey_shiny)
# 		for vertex in edge :
# 			glVertex3fv(vertices[vertex])
# 		glEnd()



# edges = (
# 		(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),
# 		(6,7),(7,8),(8,9),(9,10),(10,11),(11,6),
# 		(0,6),(1,7),(2,8),(3,9),(4,10),(5,11)
# 		)

# sides = (
# 	(0, 1, 7, 6),
# 	(1, 2, 8, 7),
# 	(2, 3, 9, 8),
# 	(3, 4, 10, 9),
# 	(4, 5, 11, 10),
# 	(5, 0, 6, 11),
# 	(0, 1, 2, 3, 4, 5),
# 	(6, 7, 8, 9, 10, 11)
# 	)


# def Hex3D(x, y_BOTTOM, y_TOP, z) :

# 	vertices = (
# 	(SIZE * (x + 1), SIZE * y_BOTTOM, SIZE * (z + 0)),
# 	(SIZE * (x + 1/2), SIZE * y_BOTTOM, SIZE * (z + m.sqrt(3)/2)),
# 	(SIZE * (x + -1/2), SIZE * y_BOTTOM, SIZE * (z + m.sqrt(3)/2)),
# 	(SIZE * (x + -1), SIZE * y_BOTTOM, SIZE * (z + 0)),
# 	(SIZE * (x + -1/2), SIZE * y_BOTTOM, SIZE * (z + -m.sqrt(3)/2)),
# 	(SIZE * (x + 1/2), SIZE * y_BOTTOM, SIZE * (z + -m.sqrt(3)/2)),

# 	(SIZE * (x + 1), SIZE * y_TOP, SIZE * (z + 0)),
# 	(SIZE * (x + 1/2), SIZE * y_TOP, SIZE * (z + m.sqrt(3)/2)),
# 	(SIZE * (x + -1/2), SIZE * y_TOP, SIZE * (z + m.sqrt(3)/2)),
# 	(SIZE * (x + -1), SIZE * y_TOP, SIZE * (z + 0)),
# 	(SIZE * (x + -1/2), SIZE * y_TOP, SIZE * (z + -m.sqrt(3)/2)),
# 	(SIZE * (x + 1/2), SIZE * y_TOP, SIZE * (z + -m.sqrt(3)/2))
# 	)

# 	# glColor3fv(grey_dark)
# 	# for surface in sides :
# 	# 	glBegin(GL_POLYGON)
# 	# 	for vertex in surface :
# 	# 		glVertex3fv(vertices[vertex])
# 	# 	glEnd()

# 	for edge in edges :
# 		for vertex in edge :
# 			glVertex3fv(vertices[vertex])


def point_central(i_size, j_size) :
	(x, z) = location_to_coord(Location.Location(i_size, j_size))
	x += 1
	z += m.sqrt(3)/2
	return (x/2, z/2)

def vertices_generator(i_size, j_size, high_min, high_max) :
	vertices = list()
	racine_3_sur_2 = m.sqrt(3)/2
	(x_center, z_center) = point_central(i_size, j_size)
	for j in range(j_size) :
		for i in range(i_size) :
			(x, z) = location_to_coord(Location.Location(i, j))

			vertices.append(SIZE * (-x_center + x + 1))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + 0))
			vertices.append(SIZE * (-x_center + x + 1/2))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + -1/2))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + -1))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + 0))
			vertices.append(SIZE * (-x_center + x + -1/2))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + -racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + 1/2))
			vertices.append(SIZE * high_min)
			vertices.append(SIZE * (-z_center + z + -racine_3_sur_2))

			vertices.append(SIZE * (-x_center + x + 1))
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + 0))
			vertices.append(SIZE * (-x_center + x + 1/2))
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + -1/2))
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + -1))
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + 0))
			vertices.append(SIZE * (-x_center + x + -1/2))
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + -racine_3_sur_2))
			vertices.append(SIZE * (-x_center + x + 1/2)) 
			vertices.append(SIZE * high_max)
			vertices.append(SIZE * (-z_center + z + -racine_3_sur_2))
	return vertices

def indices_hex_bot_generator(indice, nb) :
	indice.append(nb+0)
	indice.append(nb+1)
	indice.append(nb+2)
	indice.append(nb+3)
	indice.append(nb+4)
	indice.append(nb+5)

def indices_hex_top_generator(indice, nb) :
	indice.append(nb+6)
	indice.append(nb+7)
	indice.append(nb+8)
	indice.append(nb+9)
	indice.append(nb+10)
	indice.append(nb+11)

def indices_hex_generator(i_size, j_size) :
	indice = list()
	nb = 0
	for j in range(j_size) :
		for i in range(i_size) :
			indices_hex_bot_generator(indice, nb)
			indices_hex_top_generator(indice, nb)
			nb += 12
	return indice

def indices_edges_generator(i_size, j_size) :
	indice = list()
	nb = 0
	for j in range(j_size) :
		for i in range(i_size) :
			indice.append(nb+0)
			indice.append(nb+1)
			indice.append(nb+1)
			indice.append(nb+2)
			indice.append(nb+2)
			indice.append(nb+3)
			indice.append(nb+3)
			indice.append(nb+4)
			indice.append(nb+4)
			indice.append(nb+5)
			indice.append(nb+5)
			indice.append(nb+0)

			indice.append(nb+6)
			indice.append(nb+7)
			indice.append(nb+7)
			indice.append(nb+8)
			indice.append(nb+8)
			indice.append(nb+9)
			indice.append(nb+9)
			indice.append(nb+10)
			indice.append(nb+10)
			indice.append(nb+11)
			indice.append(nb+11)
			indice.append(nb+6)

			indice.append(nb+0)
			indice.append(nb+6)
			indice.append(nb+1)
			indice.append(nb+7)
			indice.append(nb+2)
			indice.append(nb+8)
			indice.append(nb+3)
			indice.append(nb+9)
			indice.append(nb+4)
			indice.append(nb+10)
			indice.append(nb+5)
			indice.append(nb+11)
			nb+=12
	return indice

def color_Hex(i, j, i_size, vertices) :
	nb = 12*(j*i_size + i)
	sides = (
	(nb + 0, nb + 1, nb + 7, nb + 6),
	(nb + 1, nb + 2, nb + 8, nb + 7),
	(nb + 2, nb + 3, nb + 9, nb + 8),
	(nb + 3, nb + 4, nb + 10, nb + 9),
	(nb + 4, nb + 5, nb + 11, nb + 10),
	(nb + 5, nb + 0, nb + 6, nb + 11),
	(nb + 0, nb + 1, nb + 2, nb + 3, nb + 4, nb + 5),
	(nb + 6, nb + 7, nb + 8, nb + 9, nb + 10, nb + 11)
	)

	glBegin(GL_POLYGON)
	for surface in sides :
		for vertex in surface :
			glVertex3fv((vertices[3*vertex], vertices[3*vertex + 1], vertices[3*vertex+2]))
	glEnd()

def location_to_coord(loc) :
	if not isinstance(loc, Location.Location) :
		raise Exception("loc isn't a Location")
	# x = loc.getAbscisse()*2*m.cos(m.radians(30))*m.cos(m.radians(30))
	# z = loc.getAbscisse()*2*m.cos(m.radians(60))*m.cos(m.radians(30)) + 2*m.cos(m.radians(30))*loc.getOrdonnee()
	z = loc.getAbscisse()*2*m.cos(m.radians(30))
	if loc.getOrdonnee()%2 == 1 :
		z += m.cos(m.radians(30))
	x = loc.getOrdonnee()*1.5
	return (x,z)
	
def run() :
	pygame.init()
	information_screen = pygame.display.Info()
	display = (information_screen.current_w, information_screen.current_h)
	pygame.display.set_mode(display, FULLSCREEN|DOUBLEBUF|OPENGL)

	glEnable(GL_DEPTH_TEST)
	gluPerspective(70, (display[0]/display[1]), 0.1, 100)
	glRotatef(90, 0, 1, 0)
	glTranslatef(40, 5, 0)
	glRotatef(60, 0, 0, 1)
	#glRotatef(70, 1, 0, 0)
	glColor3fv(grey_shiny)

	size_i = 25
	size_j = 25
	nb_vertices = size_j*size_i*12
	vertices = vertices_generator(size_i, size_j, 0, 0.5)
	indice_edges = indices_edges_generator(size_i, size_j)

	display_edges_list = glGenLists(1)
	glNewList(display_edges_list, GL_COMPILE)
	glEnableClientState(GL_VERTEX_ARRAY)
	glVertexPointer(3, GL_FLOAT, 0, vertices)
	glDrawElements(GL_LINES, nb_vertices*3, GL_UNSIGNED_INT, indice_edges)
	glDisableClientState(GL_VERTEX_ARRAY)
	glEndList()

	display_hex_list = glGenLists(1)
	glNewList(display_hex_list, GL_COMPILE)
	for j in range(size_j) :
		for i in range(size_i) :
			color_Hex(i, j, size_i, vertices)
	glEndList()

	while True:
		start = time.time()

		for event in pygame.event.get() :
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) :
				pygame.quit()
				exit()

			if event.type == MOUSEMOTION and event.buttons[2] == 1 :
				mouvement_ratio_horizontal = event.rel[0] / display[0]
				if event.pos[1] >= display[1]/2 :
					glRotatef(180*mouvement_ratio_horizontal, 0, 1, 0)
				else :
					glRotatef(-180*mouvement_ratio_horizontal, 0, 1, 0)

			# if event.type == pygame.MOUSEBUTTONDOWN :
			# 	if event.button == 4 :
			# 		glTranslatef(0, 1, 0)
			# 	if event.button == 5 :
			# 		glTranslatef(0, -1, 0)

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glColor3fv((180/256, 140/256, 100/256))
		glCallList(display_hex_list)
		glColor3fv((0.34, 0.31, 0.22))
		glCallList(display_edges_list)
		glTranslatef(0, 2, 0)
		glCallList(display_edges_list)
		glTranslatef(0, -2, 0)

		pygame.display.flip()
		pygame.time.wait(10)

		end = time.time()
		fps = int(round(1/(end - start)))
		pygame.display.set_caption("hex_map" + ": " + str(fps))

	glDeleteLists(list, 1)

run()