import random

class Matrix(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range (col)] for _ in range(row)]
    
    def output(self):
        for row in self.data:
            print(row)

    def fill(self) -> object:
        self.data = [[float(input(f'Введите элемент на строке {_}, столбец {__}: ')) for __ in range (self.col)] for _ in range(self.row)]
    
    def summarize(self, other) -> object:
        another = Matrix(self.row, self.col)
        for rows in range(self.row):
            for cols in range(self.col):
                another.data[rows][cols] = self.data[rows][cols] + other.data[rows][cols]
        return another

    def subtract(self, other) -> object:
        another = Matrix(self.row, self.col)
        for rows in range(self.row):
            for cols in range(self.col):
                another.data[rows][cols] = self.data[rows][cols] - other.data[rows][cols]
        return another

    def multiply(self, other) -> object:
        another = Matrix(self.row, other.col)
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    another.data[i][j] += self.data[i][k] * other.data[k][j]
        return another

    def random_gen(self, range1, range2) -> object:
        if(isinstance(range1, float) or isinstance(range2, float)):
            temp_m = [[round(random.uniform(range1, range2), 2) for _ in range (self.col)] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] = temp_m[i][j]
        else:
            temp_m = [[random.randint(range1, range2) for _ in range (self.col)] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] = temp_m[i][j]

    def transpose(self) -> object:
        other = Matrix(self.col, self.row)
        for i in range(other.row):
            for j in range(other.col):
                other.data[i][j] = self.data[j][i]
        return other

def main():
    print("Инициализируем матрицы а и б")
    a = Matrix(3,4)
    b = Matrix(5,6)
    print("Выводим матрицы a и b")
    Matrix.output(a)
    Matrix.output(b)
    print("Заполняем случайными числами 1-9 матрицу a, 1.53-8.52 матрицу b")
    Matrix.random_gen(a, 1, 9)
    Matrix.random_gen(b, 1.53, 8.52)
    print("Матрицы a и b")
    Matrix.output(a)
    Matrix.output(b)
    print("Инициализация с = а")
    c = a
    print("Транспонируем с")
    c = Matrix.transpose(c)
    print("Матрица с")
    Matrix.output(c)
    print("Присвоим d = c")
    d = c
    print("Прибавим к матрице c матрицу d")
    d = Matrix.summarize(c, d)
    Matrix.output(d)
    print("Вычитаем из матрицы d матрицу c")
    d = Matrix.subtract(d, c)
    Matrix.output(d)
    print("Инициализируем e 3x4, f 4x3")
    e = Matrix(3,4)
    f = Matrix(4,3)
    Matrix.output(e)
    Matrix.output(f)
    print("Заполняем e, f случайными числами 1-9")
    Matrix.random_gen(e, 1, 9)
    Matrix.random_gen(f, 1, 9)
    Matrix.output(e)
    Matrix.output(f)
    print("Перемножаем e, f")
    g = Matrix.multiply(e,f)
    Matrix.output(g)


if __name__ == "__main__":
    main()
