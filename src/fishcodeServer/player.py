#!/usr/bin/env/ python3
from fishcodeServer.entity import Entity

class Player(Entity):

	def __init__(self, name, size):
		super().__init__(size)
		self.name = name
		self.shots = []
		self.texture.generateDefaultImg()

	def setEnergy(self, energy):
		self.energy = energy

	def getEnergy(self):
		return self.energy

	def shoot(self):
		shootLoseEnergy()
		newShot = Shot(self)
		newShot.setPosition(self.getPosition())
		newShot.setRotaion(self.getRotation())
		self.shots.append()
		self.myMap.updateShot()

	def removeShot(self, shot):
		self.shots.remove(shot)

	def getShots(self):
		return self.shots

	def shootLoseEnergy(self):
		self.setEnergy(self.getEnergy - 1)

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def getName(self):
		return self.name
