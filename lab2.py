import random

class Matrix(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range (col)] for _ in range(row)]
        
    def __str__(self):
        total_str = ''
        current_obj = self.data
        for row in current_obj:
            for col in current_obj:
                total_str += current_obj[row][col]
            total_str += '\n'
        return total_str 
    
    def output(self):
        print (*self, sep='\n')
        
    def fill(self) -> object:
        self.data = [[float(input(f'Введите элемент на строке {_}, столбец {__}: ')) for __ in range (self.col)] for _ in range(self.row)]
    
    def summarize(self, other, another) -> object:
        for rows in range(self.row):
            for cols in range(self.col):
                another[rows][cols] = self[rows][cols] + other[rows][cols]
        return another
		        
    def subtract(self, other, another) -> object:
    	for rows in range(self.row):
            for cols in range(self.col):
                another[rows][cols] = self[rows][cols] - other[rows][cols]
        return another

    def multiply()

    def random_gen(self, range1, range2) -> object:
	if(isinstance(range1, float) or isinstance(range2, float)):
		return [[round(random.uniform(range1, range2), 2) for _ in range (col)] for _ in range(row)]
	else:
		return[[random.randint(range1, range2) for _ in range (col)] for _ in range(row)]
    
    def transpose(self, other) -> object:
	    other.row = self.col
	    other.col = self.row
	    for i in range(other.row):
		    for j in range(other.col):
			    other.data[row][col] = self.data[col][row]
        return other
