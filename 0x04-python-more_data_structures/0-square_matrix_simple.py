#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = []
	for i in range(3):
		new_matrix.append([row[i ** 2] for row in matrix])
