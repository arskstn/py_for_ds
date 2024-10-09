import time
import sys

def menu():
    try:
        choice = int(input("Выберите режим работы:\n1 - Операции с числами\n2 - Операции с матрицами\n3 - выход из программы\nВведите номер режима: "))
        if (choice == 1):
            number_menu()
        elif (choice == 2):
            matrix_menu()
        elif (choice == 3):
            print("Выход")
            time.sleep(2)
            sys.exit()
        else:
            print("Неправильный выбор, попробуйте еще раз")
            menu()
    except ValueError:
        print("Это не число, которое от вас ожидали, попробуйте еще раз")
        time.sleep(2)
        menu()
        
def number_menu():
    try:
        choice = int(input("Выберите операцию с числами:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Выход в меню\nВведите номер операции: "))
        if (choice == 1):
            print("Результат:",float(input("Введите первое число: ")) + float(input("Введите второе число: ")))
        elif (choice == 2):
            print("Результат:",float(input("Введите первое число: ")) - float(input("Введите второе число: ")))
        elif (choice == 3):
            print("Результат:",float(input("Введите первое число: ")) * float(input("Введите второе число: ")))
        elif (choice == 4):
            print("Результат:",float(input("Введите первое число: ")) / float(input("Введите второе число: ")))
        elif (choice == 5):
            menu()
        else:
            print("Неправильный выбор, попробуйте еще раз")
            menu()
    except ValueError:
        print("Это не число, которое от вас ожидали, попробуйте еще раз")
        time.sleep(2)
        number_menu()
        
def matrix_menu():
    try:
        choice = int(input("Выберите операцию с матрицами:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Выход в меню\nВведите номер операции: "))
        if (choice == 1):
            i, j = map(int, input("Введите количество строк и столбцов первой матрицы через пробел: ").split())
            k, l = map(int, input("Введите количество строк и столбцов второй матрицы через пробел: ").split())
            if(i==k and j==l):
                m1 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(j)] for row in range(i)]
                m2 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(l)] for row in range(k)]
                m3 = [[0] * j for _ in range(i)]
                for a in range(0, i):
                    for b in range(0, j):
                        m3[a][b] = m1[a][b] + m2[a][b]
                print("Результат:")
                print(*m3, sep='\n')
                time.sleep(2)
                matrix_menu()
        elif (choice == 2):
            i, j = map(int, input("Введите количество строк и столбцов первой матрицы через пробел: ").split())
            k, l = map(int, input("Введите количество строк и столбцов второй матрицы через пробел: ").split())
            if(i==k and j==l):
                m1 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(j)] for row in range(i)]
                m2 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(l)] for row in range(k)]
                m3 = [[0] * j for _ in range(i)]
                for a in range(0, i):
                    for b in range(0, j):
                        m3[a][b] = m1[a][b] - m2[a][b]
                print(*m3, sep='\n')
                time.sleep(2)
                matrix_menu()            
            else:
                print("Размерности при вычитании должны быть одинаковы, попробуйте еще раз")
                time.sleep(2)
                matrix_menu()
        elif(choice == 3):
            i, j = map(int, input("Введите количество строк и столбцов первой матрицы через пробел: ").split())
            k, l = map(int, input("Введите количество строк и столбцов второй матрицы через пробел: ").split())
            if(j==k):
                m1 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(j)] for row in range(i)]
                m2 = [[float(input(f"Задайте элемент на строке {row + 1}, столбце {col + 1}: ")) for col in range(l)] for row in range(k)]
                m3 = [[0] * i for _ in range(i)]
                for i in range(len(m1)):
                    for j in range(len(m2[0])):
                        for k in range(len(m2)):
                            m3[i][j] += m1[i][k] * m2[k][j]
                print(*m3, sep='\n')
                time.sleep(2)
                matrix_menu()            
            else:
                print("Кол-во столбцов первой матрицы и кол-во строк второй матрицы должны быть одинаковы, попробуйте еще раз")
                time.sleep(2)
                matrix_menu()
        elif (choice == 4):
            menu()
        else:
            print("Неправильный выбор, попробуйте еще раз")
            menu()
    except ValueError:
        print("Это не число, которое от вас ожидали, попробуйте еще раз")
        time.sleep(2)
        matrix_menu()

if __name__ == "__main__":
    menu()
