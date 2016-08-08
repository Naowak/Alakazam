import sys
sys.path.append("./../map")

import pygame
import math as m
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from enum import Enum
import time
import array

import Location
import Map
import Sight

SIZE = 1

class Display_list_color_click_array() :
	def __init__(self, i_size, j_size, bottom_y, top_y, map_data) :
		if not isinstance(i_size, int) :
			raise Exception("TYPE ERROR : i isn't an int")
		if not isinstance(j_size, int) :
			raise Exception("TYPE ERROR : j isn't an int")

		self.array = list()
		self.map_data = map_data
		self.i_size = i_size
		self.j_size = j_size
		self.bottom_y = bottom_y
		self.top_y = top_y

		for i in range(i_size) :
			self.array.append(list())
			for j in range(j_size) :
				self.array[i].append(None)

	def get_i_size(self) :
		return self.i_size

	def get_j_size(self) :
		return self.j_size

	def get_map_data(self) :
		return self.map_data

	def set_display_list(self, i, j, display_list) :
		if not isinstance(i, int) :
			raise Exception("TYPE ERROR : i isn't an int")
		if not isinstance(j, int) :
			raise Exception("TYPE ERROR : j isn't an int")
		self.array[i][j] = display_list

	def get_display_list(self, loc) :
		i = loc.getAbscisse()
		j = loc.getOrdonnee()
		return self.array[i][j]

	def create_display_list(self, i, j) :
		loc = Location.Location(i, j)
		if self.get_map_data().getCellType(loc) == "Empty" :
			self.set_display_list(i, j, glGenLists(1))
			glNewList(self.get_display_list(loc), GL_COMPILE)
			color = loc_to_color(loc)
			draw_hex(color, color, self.bottom_y, self.top_y)
			glEndList()
		elif self.get_map_data().getCellType(loc) == "Taken" :
			self.set_display_list(i, j, glGenLists(1))
			glNewList(self.get_display_list(loc), GL_COMPILE)
			color = loc_to_color(loc)
			draw_hex(color, color, self.bottom_y, self.top_y)
			glEndList()
		elif self.get_map_data().getCellType(loc) == "Full" :
			self.set_display_list(i, j, glGenLists(1))
			glNewList(self.get_display_list(loc), GL_COMPILE)
			color = loc_to_color(loc)
			draw_hex(color, color, self.bottom_y, self.top_y)
			draw_hex(color, color, self.top_y, self.top_y*2)
			glEndList()
		elif self.get_map_data().getCellType(loc) == "Hole" :
			pass

	def create_all_display_list(self) :
		for i in range(self.get_i_size()) :
			for j in range(self.get_j_size()) :
				self.create_display_list(i, j)

	def delete_display_list(self, i, j) :
		glDeleteLists(get_display_list(i, j), 1)

	def delete_all_display_list(self) :
		for i in range(get_i_size()) :
			for j in range(get_j_size()) :
				delete_display_list(i, j)




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

def point_central(i_size, j_size) :
	(x, z) = location_to_coord(Location.Location(i_size, j_size))
	x += 1
	z += m.sqrt(3)/2
	return (x/2, z/2)

def add_vertices_according_to_y(vertices, y) :
	racine_3_sur_2 = m.sqrt(3)/2
	vertices.append(SIZE * 1)
	vertices.append(SIZE * y)
	vertices.append(SIZE * 0)
	vertices.append(SIZE * 1/2)
	vertices.append(SIZE * y)
	vertices.append(SIZE * racine_3_sur_2)
	vertices.append(SIZE * -1/2)
	vertices.append(SIZE * y)
	vertices.append(SIZE * racine_3_sur_2)
	vertices.append(SIZE * -1)
	vertices.append(SIZE * y)
	vertices.append(SIZE * 0)
	vertices.append(SIZE * -1/2)
	vertices.append(SIZE * y)
	vertices.append(SIZE * -racine_3_sur_2)
	vertices.append(SIZE * 1/2)
	vertices.append(SIZE * y)
	vertices.append(SIZE * -racine_3_sur_2)

def one_hex_indices_edges_generator() :
	indice = list()
	indice.append(0)
	indice.append(1)
	indice.append(1)
	indice.append(2)
	indice.append(2)
	indice.append(3)
	indice.append(3)
	indice.append(4)
	indice.append(4)
	indice.append(5)
	indice.append(5)
	indice.append(0)

	indice.append(6)
	indice.append(7)
	indice.append(7)
	indice.append(8)
	indice.append(8)
	indice.append(9)
	indice.append(9)
	indice.append(10)
	indice.append(10)
	indice.append(11)
	indice.append(11)
	indice.append(6)

	indice.append(0)
	indice.append(6)
	indice.append(1)
	indice.append(7)
	indice.append(2)
	indice.append(8)
	indice.append(3)
	indice.append(9)
	indice.append(4)
	indice.append(10)
	indice.append(5)
	indice.append(11)

	return indice
			

def draw_hex(color_lines, color_sides, bottom_y, top_y) :
	vertices = list()
	nb_vertices = 12
	add_vertices_according_to_y(vertices, bottom_y)
	add_vertices_according_to_y(vertices, top_y)

	sides = (
	(0, 1, 7, 6),
	(1, 2, 8, 7),
	(2, 3, 9, 8),
	(3, 4, 10, 9),
	(4, 5, 11, 10),
	(5, 0, 6, 11),
	(0, 1, 2, 3, 4, 5),
	(6, 7, 8, 9, 10, 11)
	)

	#draw_lines
	glColor3fv(color_lines)
	glEnableClientState(GL_VERTEX_ARRAY)
	glVertexPointer(3, GL_FLOAT, 0, vertices)
	glDrawElements(GL_LINES, nb_vertices*3, GL_UNSIGNED_INT, one_hex_indices_edges_generator())
	glDisableClientState(GL_VERTEX_ARRAY)

	#draw_sides
	glColor3fv(color_sides)
	glBegin(GL_POLYGON)
	for surface in sides :
		for vertex in surface :
			glVertex3fv((vertices[3*vertex], vertices[3*vertex + 1], vertices[3*vertex+2]))
	glEnd()

def loc_to_color(loc) :
	return ((loc.getAbscisse()+1)/256, (loc.getOrdonnee()+1)/256, 0)

def color_array_to_loc(color_array) :
	return Location.Location((int) (color_array[0][0][0]*256) - 1, (int) (color_array[0][0][1]*256) - 1)

	
def run() :
	pygame.init()
	information_screen = pygame.display.Info()
	display = (information_screen.current_w, information_screen.current_h)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	glEnable(GL_DEPTH_TEST)
	gluPerspective(70, (display[0]/display[1]), 0.1, 200)
	glRotatef(90, 0, 1, 0)
	glTranslatef(40, 5, 0)
	glRotatef(60, 0, 0, 1)

	#data_init
	size_i = 26
	size_j = 26
	bottom_y = 0
	top_y = 0.5
	color_lines = (60/256, 60/256, 60/256)
	color_sides_empty = (170/256, 160/256, 150/256)
	color_sides_visible = (60/256, 60/256, 120/256)
	color_sides_click = (60/256, 60/256, 180/256)
	color_sides_full = (120/256, 110/256, 100/256)

	#map_data_init
	map_data = Map.Map(size_i, size_j)
	map_data.generationRelief()
	sight = Sight.Sight(size_i, size_j)

	#empty_hex
	display_list_empty_hex = glGenLists(1)
	glNewList(display_list_empty_hex, GL_COMPILE)
	draw_hex(color_lines, color_sides_empty, bottom_y, top_y)
	glEndList()

	#full_hex
	display_list_full_hex = glGenLists(1)
	glNewList(display_list_full_hex, GL_COMPILE)
	draw_hex(color_lines, color_sides_empty, bottom_y, top_y)
	draw_hex(color_lines, color_sides_full, top_y, top_y*2)
	glEndList()

	#hex_visible
	display_list_visible_hex = glGenLists(1)
	glNewList(display_list_visible_hex, GL_COMPILE)
	draw_hex(color_lines, color_sides_visible, bottom_y, top_y)
	glEndList()

	#hex_click
	display_list_click_hex = glGenLists(1)
	glNewList(display_list_visible_hex, GL_COMPILE)
	draw_hex(color_lines, color_sides_click, bottom_y, top_y)
	glEndList()

	#all_hex
	display_list_map = glGenLists(1)
	glNewList(display_list_map, GL_COMPILE)
	(central_x, central_z) = point_central(size_i, size_j)
	glTranslatef(-central_x, 0, -central_z)
	for j in range(size_j) :
		for i in range(size_i) :
			loc = Location.Location(i, j)
			cell_type = map_data.getCellType(loc)
			(x, z) = location_to_coord(loc)
			glTranslatef(x, 0, z)
			if cell_type == "Empty" :
				glCallList(display_list_empty_hex)
			elif cell_type == "Taken" :
				glCallList(display_list_empty_hex)
			elif cell_type == "Full" :
				glCallList(display_list_full_hex)
			elif cell_type == "Hole" :
			 	pass
			glTranslatef(-x, 0, -z)
	glTranslatef(central_x, 0, central_z)
	glEndList()

	#tab_display_list_one_hex_color
	tab_display_list_one_hex_color = Display_list_color_click_array(size_i, size_j, bottom_y, top_y, map_data)
	tab_display_list_one_hex_color.create_all_display_list()

	#all_hex_color_click
	display_list_all_hex_color_click = glGenLists(1)
	glNewList(display_list_all_hex_color_click, GL_COMPILE)
	(central_x, central_z) = point_central(size_i, size_j)
	glTranslatef(-central_x, 0, -central_z)
	for j in range(size_j) :
		for i in range(size_i) :
			loc = Location.Location(i, j)
			cell_type = map_data.getCellType(loc)
			if cell_type != "Hole" :
				(x, z) = location_to_coord(loc)
				glTranslatef(x, 0, z)
				glCallList(tab_display_list_one_hex_color.get_display_list(loc))
				glTranslatef(-x, 0, -z)
	glTranslatef(central_x, 0, central_z)
	glEndList()

	loc_click = Location.Location(-1, -1)

	while True:
		start = time.time()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glCallList(display_list_all_hex_color_click)

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

			if event.type == MOUSEBUTTONUP and event.button == 1 :
				color_array = glReadPixels(event.pos[0], information_screen.current_h - event.pos[1], 1, 1, GL_RGB, GL_FLOAT)
				loc_click = color_array_to_loc(color_array)
				try :
					sight.fieldOfView(loc_click, map_data)
				except Exception :
					pass

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		if loc_click.equals(Location.Location(-1, -1)) :
			glCallList(display_list_map)
		else :
			(central_x, central_z) = point_central(size_i, size_j)
			glTranslatef(-central_x, 0, -central_z)
			for j in range(size_j) :
				for i in range(size_i) :
					loc = Location.Location(i, j)
					cell_type = map_data.getCellType(loc)
					(x, z) = location_to_coord(loc)
					glTranslatef(x, 0, z)
					if loc == loc_click :
						if cell_type == "Empty" or cell_type == "Taken" :
							glCallList(display_list_click_hex)
					else :
						if cell_type == "Empty" :
							if sight.getSightCell(loc) == True :
								glCallList(display_list_visible_hex)
							else :
								glCallList(display_list_empty_hex)
						elif cell_type == "Taken" :
							if sight.getSightCell(loc) == True :
								glCallList(display_list_visible_hex)
							else :
								glCallList(display_list_empty_hex)
						elif cell_type == "Full" :
							glCallList(display_list_full_hex)
						elif cell_type == "Hole" :
						 	pass
					glTranslatef(-x, 0, -z)
			glTranslatef(central_x, 0, central_z)

		pygame.display.flip()
		pygame.time.wait(10)

		end = time.time()
		fps = int(round(1/(end - start)))
		pygame.display.set_caption("hex_map" + ": " + str(fps))

	glDeleteLists(display_list_empty_hex, 1)
	glDeleteLists(display_list_full_hex, 1)
	glDeleteLists(display_list_map, 1)

run()