# -*- coding: utf-8 -*-

class File :

	def __init__(self) :
		self._f = list()

	def enfiler(self, obj) :
		self._f.append(obj)

	def defiler(self) :
		if not self.fileVide() :
			self._f.pop(0)

	def fileVide(self) :
		return len(self._f) == 0

	def getValeur(self) :
		if not self.fileVide() :
			return self._f[0]
		print("File vide")