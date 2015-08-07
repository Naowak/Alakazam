# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:14:42 2015

@author: Gauthier
"""

from Character import *

class Team():
	"""group of Characters"""
	
	def __init__(self, Char1, Char2, Char3 ) :
		
		if not isinstance (Char1, Character):
			raise Exception ("Char1 must be a Character")
		if not isinstance (Char2, Character):
			raise Exception ("Char2 must be a Character")
		if not isinstance (Char3, Character):
			raise Exception ("Char3 must be a Character")
		
		self._char1 = Char1
		self._char2 = Char2
		self._char3 = Char3
	
	def getChar1(self):
		return self._char1
		
	def getChar2(self):
		return self._char2
	
	def getChar3(self):
		return self._char3
	
	def setChar1(self, Char):
		if not isinstance(Char, Character) :
			raise Exception ("Char must be a Character")
		self._char1 = Char
	
	def setChar2(self, Char):
		if not isinstance(Char, Character) :
			raise Exception ("Char must be a Character")
		self._char2 = Char
	
	def setChar3(self, Char):
		if not isinstance(Char, Character) :
			raise Exception ("Char must be a Character")
		self._char3 = Char	
	
	def getListChar(self):
		return [self.getChar1(), self.getChar2(), self.getChar3()]

	def __str__(self) :
		s = ''
		for elem in self.getListChar() :
			s += str(elem)
		return s