import numpy as np
from unidecode import unidecode

string1 = unidecode("haf nooij")
string2 = unidecode("ha noi")

with open("./data/test/lookup_tables/tinh_thanh.txt", "r") as file:
	data = file.read()
data = data.split(',')
data[-1] = data[-1][:len(data[-1])-1]

def levenshtein(seq1, seq2):
	size_x = len(seq1) + 1
	size_y = len(seq2) + 1
	matrix = np.zeros((size_x, size_y))
	for x in range(size_x):
		matrix[x][0] = x
	for y in range(size_y):
		matrix[0][y] = y

	for x in range(1, size_x):
		for y in range(1, size_y):
			if seq1[x-1] == seq2[y-1]:
				matrix[x][y] = min(matrix[x-1][y] + 1, matrix[x-1][y-1], matrix[x][y-1] + 1)
			else:
				matrix[x][y] = min(matrix[x-1][y] + 1, matrix[x-1][y-1] + 1, matrix[x][y-1] + 1)

	return (int(matrix[size_x - 1, size_y - 1]))


for i in data:
	print(levenshtein(i.lower(), string1), i)
