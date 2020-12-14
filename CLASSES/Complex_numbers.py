#!/usr/bin/python3
#				"Complex numbers"
class ComplexNumber:
	def __init__(self, realpart, imagpart):
		self.real = realpart
		self.imag = imagpart

	def __add__(self, other):
		return ComplexNumber(self.real + other.real, self.imag + other.imag)

	def __sub__(self, other):
		return ComplexNumber(self.real - other.real, self.imag - other.imag)

	def print(self):
		if self.imag == 0:
			print(f"Real = {self.real}")
		else:
			print(f"Real = {self.real}, Imaginary = {self.imag}j\n")

