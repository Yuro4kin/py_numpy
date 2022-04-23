import numpy as np

# 3. Функции автозаполнения, создания матриц и числовых диапазонов
#    https://numpy.org/doc/stable/

# Например мы хотим создать матрицу из десяти 0, создадим такой список
m = np.array([0] * 10)
print(m)
# [0 0 0 0 0 0 0 0 0 0]

# # Например мы хотим создать матрицу из пятнадцати 1, создадим такой список
m1 = np.array([1] * 15)
print(m1)
# [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]

# Если мы хотим сгенерировать список, можем воспользоваться механизмом генерации списков - list comprehension
m2 = np.array([x for x in range(10)])
print(m2)
# [0 1 2 3 4 5 6 7 8 9]

# Функции автозаполнения элементов массива - данные функции работают быстрей чем генератор массива array()
# Название              Описание
#
# empty(shape, …)       Возвращает новый массив заданного размера и типа данных, но без определенных значений.
# eye(N, M=None, …)     Возвращает массив размером NxMс единичными диагональными элементами (остальные элементы равны нулю)
# identity(n, …)        Возвращает квадратный массив размерностью nxn с единичными элементами по главной диагонали (остальные равны нулю).
# ones(shape, …)        Возвращает массив заданного размера и типа, состоящего из всех единиц.
# zeros(shape, …)       Возвращает массив заданного размера и типа, состоящего из всех нулей.
# full(shape, value, …) Возвращает массив заданного размера и типа со значениями value.

# Например получим одномерный массив из произвольных десяти чисел
m3 = np.empty(10)
print(m3)
# [ 7.25563882e+199  2.03729894e+174  9.79882228e+252  1.19490107e+190
#   7.21903950e+159 -1.27091336e-310  2.78139142e+180  6.01347002e-154
#   6.01347002e-154  2.34726922e+251]

# Например получим одномерный массив из произвольных десяти чисел типа 'int16'
m4 = np.empty(10, dtype='int16')
print(m4)
# [26995 25978  3802 30034 29806 28009 22373 29281 26990 26478]

# Например получим двумерный массив размерностью (3,2) из произвольных десяти чисел типа 'int16'
m5 = np.empty((3, 2), dtype='int16')
print(m5)
# [[  7488 -18295]
#  [ 32760      0]
#  [ 12000 -18295]]

# Например получим одномерный массив - единичная матрица, где посередине 1, из произвольных десяти чисел типа 'int16'
m6 = np.eye(4)
print(m6)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Например получим одномерный массив - единичная матрица, где посередине 1, 'int16', остальные 0
m7 = np.eye(4, 2)
print(m7)
# [[1. 0.]
#  [0. 1.]
#  [0. 0.]
#  [0. 0.]]

# Например нам нужно получить строго единичную матрицу
m8 = np.identity(5)
print(m8)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# Например нам нужен массив, состоящий из одних 0, используем функцию zeros()
# первый аргумент - размерность массива, на выходе трехмерный массив, состоящий из всех 0
m9 = np.zeros((2, 3, 4))
print(m9)
# [[[0. 0. 0. 0.]
#   [0. 0. 0. 0.]
#   [0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0.]
#   [0. 0. 0. 0.]
#   [0. 0. 0. 0.]]]

# ones() - функция создает массив из всех 1, размерность укажем с помощью списка
# на выходе двумерный массив 4х3, состоящий из всех 1, тип будет 'int8'
m10 = np.ones([4, 3], dtype='int8')
print(m10)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]
#  [1 1 1]]

# full() - функция позволяет создавать произвольные массивы, например размерностью 3х2, это двумерный массив
#          состоящий из заданных значений, например -1
m11 = np.full((3, 2), -1)
print(m11)
# [[-1 -1]
#  [-1 -1]
#  [-1 -1]]


# Функции создания матриц - генерировать матрицы на основе списков или по определенным правилам
# Название                  Описание
# mat(object, …)            Приводит входные данные object к матрице, если это возможно. Параметр object может быть строкой, списком или кортежем.
# diag(list, …)             Формирует диагональную матрицу на основе списка или массива NumPy. В последних версиях возвращает копию массива (а не его представление).
# diagflat(list, …)         Формирует диагональную матрицу из списка list, который сначала сжимает до одной оси (преобразует в одномерный список или массив).
# tri(N, M=None, …)         Создает треугольный массив NxM с единицами на главной диагонали и ниже ее.
# tril(list, …)             Преобразует двумерный список или массив list в треугольную матрицу с нулевыми элементами выше главной диагонали.
# triu(list, …)             Преобразует двумерный список или массив list в треугольную матрицу с нулевыми элементами ниже главной диагонали.
# vander(list, N=None, …)   Создание матрицы Вандермонда из одномерного списка или массива list. Второй параметр N определяет число столбцов (по умолчанию формируется квадратная матрица).

# mat() - позволяет создавать матрицу из строки с элементами, на выходе получим матрицу-matrix
#         [[ ]] - две квадратные скобки это матрица [ - первая ось [ - вторая ось,
#         матрица размерностью 1х4 - имеем здесь одну строку, которую создали из строки, элементы можно указывать и через запятую
m12 = np.mat('1 2 3 4')
print(m12)
# [[1 2 3 4]]

# mat() - создадим двумерную матрицу из строки
m13 = np.mat('1 2; 3 4')
print(m13)
# [[1 2]
#  [3 4]]

# mat() - создадим матрицу на основе списка [5, 4, 3]
m14 = np.mat([5, 4, 3])
print(m14)
# [[5 4 3]]

# mat() - двумерная матрица, указываем двумерный список (1, 2, 3), обратить внимание чтоб была представлена прямоугольная таблица чисел
m15 = np.mat([(1, 2, 3), (4, 5, 6)])
print(m15)
# [[1 2 3]
#  [4 5 6]]

# diag() - создаем диагональные матрицы c элементами по главной диагонали
m16 = np.diag([1, 2, 3])
print(m16)
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

# diag() - можно передать двумерный список или двумерный массив,
#          для которых функция выделяет элементы, которые стоят по главной диагонали
m17 = np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(m17)
# [1 5 9]

# diagflat() - Например мы хотим создать диагональную матрицу из многомерных данных из двух- трех- мерного списка
#              все элементы воспринимаются как единый список, теперь они стоят по главной диагонали
m18 = np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(m18)
# [[1 0 0 0 0 0 0 0 0]
#  [0 2 0 0 0 0 0 0 0]
#  [0 0 3 0 0 0 0 0 0]
#  [0 0 0 4 0 0 0 0 0]
#  [0 0 0 0 5 0 0 0 0]
#  [0 0 0 0 0 6 0 0 0]
#  [0 0 0 0 0 0 7 0 0]
#  [0 0 0 0 0 0 0 8 0]
#  [0 0 0 0 0 0 0 0 9]]

# tri() - создает диагональную матрицу, по главной диагонали 1, те элементы, что над главной диагональю равны 0
m19 = np.tri(4)
print(m19)
# [[1. 0. 0. 0.]
#  [1. 1. 0. 0.]
#  [1. 1. 1. 0.]
#  [1. 1. 1. 1.]]

# tri() - матрица размерностью 4х2, элементы под главной диагональю равны 1, над главной диагональю равны 0
m20 = np.tri(4, 2)
print(m20)
# [[1. 0.]
#  [1. 1.]
#  [1. 1.]
#  [1. 1.]]

# tri() - матрица размерностью 2х4, элементы под главной диагональю равны 1, над главной диагональю равны 0
m21 = np.tri(2, 4)
print(m21)
# [[1. 0. 0. 0.]
#  [1. 1. 0. 0.]]

# Например нужно привести уже существующие массивы array() к треугольному виду tri()
# array() ---> tril(), элементы над главной диагональю равны 0, под главной диагональю элементы остались прежними
m22 = np.array( [(1, 2, 3), (4, 5, 6), (7, 8, 9)] )
m22_1 = np.tril(m22)
print(m22_1)
# [[1 2 3]                    [[1 0 0]
#  [4 5 6]        ---> tril() [4 5 0]
#  [7 8 9]]                   [7 8 9]]

# array() ---> triu(), элементы над главной диагональю остались прежними , под главной диагональю элементы равны 0
m22_2 = np.triu(m22)
print(m22_2)
#  [[1 2 3]                   [[1 2 3]
#  [4 5 6]        ---> triu() [0 5 6]
# [7 8 9]]                    [0 0 9]]

# Если мы функции tril() укажем не массив, а одномерный список, то на основе одномерного списка будет
#                        сформирована треугольная матрица
m23 = np.tril([1, 2, 3])
print(m23)
# [[1 0 0]
#  [1 2 0]
#  [1 2 3]]

# Если мы функции tril() укажем многомерный массив, которому передадим трехмерный список
# на выходе сформирована на основе трехмерного списка многомерная треугольная матрица
m24 = np.tril( [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]] )
print(m24)
# [[[1 0 0]
#   [4 5 0]
#   [7 8 9]]]

# функции tril и triu будут работать и с многомерными массивами - возьмем трехмерный массив
# В этом случае каждый двумерный срез(сечения) будут приведены к треугольному виду(матрице).
m25 = np.tril([[[1,2,3], [4,5,6], [7,8,9]], [[10,20,30], [40,50,60], [70,80,90]], [[100,200,300], [400,500,600], [700,800,900]]])
print(m25)
# [[[  1   0   0]
#   [  4   5   0]
#   [  7   8   9]]
#
#  [[ 10   0   0]
#   [ 40  50   0]
#   [ 70  80  90]]
#
#  [[100   0   0]
#   [400 500   0]
#   [700 800 900]]]

#  vander() - формирует матрицу Вандермонда из одномерных списков или массивов
m26 = np.vander([1, 2, 3])
print(m26)
# [[1 1 1]
#  [4 2 1]
#  [9 3 1]]

# Функции формирования числовых диапазонов
# Следующая группа функций - служит для формирования числовых диапазонов.
# Что делают эти функции? Когда мы с вами изучали язык Python, то говорили о функции
#           range(Start, Stop, Step)
# которая генерирует числовой диапазон с параметрами Start, Stop, Step.
# Причем, все эти параметры должны быть целочисленными.
# В NumPy есть подобные функции, но более гибкие и работающие с вещественными величинами.
#
# Название                  Описание
#
# arange()                  Возвращает одномерный массив с равномерно разнесенными числами указанного диапазона.
# linspace(start, stop, …)  Возвращает одномерный массив c равномерно разнесенными числами, используя только значения начала и конца интервала.
# logspace(start, stop, …)  Возвращает одномерный массив с числами, равномерно распределенных по логарифмической шкале.
# geomspace(start, stop, …) Формирование чисел по геометрической прогрессии.

# ф-ции возвращают отображение многомерных графиков
# meshgrid(x1, ..., xn, …)
#          x1, ..., xn – одномерные последовательности или массивы, используемые для формирования координатной сетки по каждой из осей.
# mgrid[]                   Возвращает массив плотных координатных сеток.
# ogrid[]                   Возвращает открытую сетку значений.

m27 = np.arange(5)
print(m27)
# [0 1 2 3 4]

m28 = np.arange(1, 5)
print(m28)
# [1 2 3 4]

#                     шаг - можно работать с вещественными данными и шаг тоже можно задавать вещественный
m29 = np.arange(1, 5, 0.5)
print(m29)
# [1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# на выходе одномерный массив вещественных чисел
m30 = np.arange(0, np.pi, 0.1)
print(m30)
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7
#  1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.  3.1]
# используя данный массив можно вычислить sin или cos для следующих углов
m31 = np.cos(np.arange(0, np.pi, 0.1))
print(m31)
# [ 1.          0.99500417  0.98006658  0.95533649  0.92106099  0.87758256
#   0.82533561  0.76484219  0.69670671  0.62160997  0.54030231  0.45359612
#   0.36235775  0.26749883  0.16996714  0.0707372  -0.02919952 -0.12884449
#  -0.22720209 -0.32328957 -0.41614684 -0.5048461  -0.58850112 -0.66627602
#  -0.73739372 -0.80114362 -0.85688875 -0.90407214 -0.94222234 -0.97095817
#  -0.9899925  -0.99913515]

# linspace(start, stop, …) - n - это колличество делений интервала от start до stop, если n=0, то получим пустой массив
#                           ecли n=1, то будет одно значение start, ecли n=2, то будет два значения start и stop
#                           ecли n=3, то будет два значения start, stop и значение пополам 2
#                           все деления(интервал) n будут происходить равномерно

m32 = np.linspace(0, np.pi, 0)
print(m32)
# []

m33 = np.linspace(0, np.pi, 1)
print(m33)
# [0.]

# указали два значения - начальное и конечное
m34 = np.linspace(0, np.pi, 2)
print(m34)
# [0.         3.14159265]

# указали три значения - получим, начальное, конечное и середину мнтервала
m35 = np.linspace(0, np.pi, 3)
print(m35)
# [0.         1.57079633 3.14159265]

m36 = np.linspace(0, np.pi, 4)
print(m36)
# [0.         1.04719755 2.0943951  3.14159265]

m37 = np.linspace(0, np.pi, 5)
print(m37)
# [0.         0.78539816 1.57079633 2.35619449 3.14159265]

# логорифмический масштаб, указали 1 - это 1*10
#                       3- колличество делений, сколько берем значений в этом интервале
m38 = np.logspace(0, 1, 3)
print(m38)
#               центральное значение - это корень квадратный из 10
# [ 1.          3.16227766 10.        ]

m39 = np.logspace(0, 1, 4)
print(m39)
# [ 1.          2.15443469  4.64158883 10.        ]

# получаем геометрическую прогрессию, каждый последующий чле умножаем на 2, и получаем следующий член
m40 = np.geomspace(1, 4, 3)
print(m40)
# [1. 2. 4.]

m41 = np.geomspace(1, 16, 5)
print(m41)
# [ 1.  2.  4.  8. 16.]


# Функции формирования массивов на основе данных
# Название                   Описание
#
# array(object, …)           Преобразует список или кортеж object в массив NumPy.
# asanyarray(list, …)        Преобразует список list в массив array, сохраняя тип подкласса.
# ascontiguousarray(list, …) Возвращает непрерывный массив в памяти, подобно как это организовано в языке C.
# asmatrix(list, …)          Преобразует входную последовательность list в матрицу NumPy (тип matrix).
# copy(list, …)              Возвращает копию массива list (если это объект NumPy) или просто создает массив на основе списка языка Python.
# frombuffer(buffer, …)      Преобразует данные из буфера в массив NumPy
# fromfile(file, …)          Возвращает массив из данных текстового или бинарного файла file.
# fromfunction(func, shape, …) Создает массивразмерностью shape с помощью функции func.
# fromiter(iter, …)          Создает массив на основе итерируемого объекта.
# fromstring(string, …)      Создает массив из данных строки.
# loadtxt(file, …)           Формирует массив из данных текстового файла.

# Сформируем двумерный массив состоящий из чисел
m42 = np.array( [(1, 2), (3, 4)] )
print(m42)
# [[1 2]
#  [3 4]]
# Создадим копию данного массива в памяти
m_c = np.copy(m42)
print(m_c)
# [[1 2]
#  [3 4]]
# Изменим первую строку элементов двумерного массива m_c на 100, при этом массив m42 остался прежним
m_c[0] = 100
print(m_c)
# [[100 100]
#  [  3   4]]

# Например есть функция getRange(), которая возвращает некие значения 100 * x + y, на основе аргументов x, y
# которые передаются в функци getRange(x, y)
# fromfunction() - далее используя эту функцию, на основе функции getRange() создаем массив размерами 2x2
# x , y - это аргументы, которые являются индексами при создании матрицы 2х2
# x - это строка, y - это столбец. Сначала x = 0, а y - менялся от 0 до 1
# Далее х увеличился на 1 и у нас появилось 100, и к 100 мы добавляли y, который менялся от 0 до 1
def getRange(x, y):
    return 100 * x + y
m43 = np.fromfunction(getRange, (2, 2))
print(m43)
# [[  0.   1.]
#  [100. 101.]]


def getRange_easy(x, y):
    return x + y
m44 = np.fromfunction(getRange_easy, (3, 3))
print(m44)
#   0  1  2
#   y  y  y
# [[0. 1. 2.]  x - index 0  при (y от 0 до 2)
#  [1. 2. 3.]  x - index 1  при (y от 0 до 2)
#  [2. 3. 4.]] x - index 2  при (y от 0 до 2)

# умножение x * y
#   0  1  2
#   y  y  y
# [[0. 0. 0.]   x - index 0  при (y от 0 до 2)
#  [0. 1. 2.]   x - index 1  при (y от 0 до 2)
#  [0. 2. 4.]]  x - index 2  при (y от 0 до 2)



# Использование функции fromfunction() совместно с lambda() функцией, в одну строку предыдущий пример
# lambda функция с двумя аргументами x, y
m45 = np.fromfunction(lambda x, y: x*100+y, (2, 2))
print(m45)
# [[  0.   1.]
#  [100. 101.]]

# fromiter() - функция помогает формировать массив на основе любого итерируемого объекта, например строки
#              на выходе массив из отдельных символов, состоящий из этой строки
m46 = np.fromiter("hello", dtype='U1')
print(m46)
# ['h' 'e' 'l' 'l' 'o']

# Здесь в качестве объекта передается функция-генератор и на выходе получаем одномерный массив чисел
# функция getRange_g() будет возвращать порядковые значения
def getRange_g(N):
    for i in range(N):
        yield i
m47 = np.fromiter(getRange_g(4), dtype='int8')
print(m47)
# [0 1 2 3]

# функция - fromstring() позволяет создавать массив из строковых данных, например
# формируем массив из строки '1 2 3', указываем тип данных элементов 'int16', разделитель ' '
# на выходе получим массив из чисел 1, 2, 3
m48 = np.fromstring('1 2 3', dtype='int16', sep= ' ')
print(m48)
# [1 2 3]

m49 = np.fromstring('1, 2, 3', dtype='int16', sep= ',')
print(m49)
# [1 2 3]