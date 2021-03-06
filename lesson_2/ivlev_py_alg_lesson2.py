# -*- coding: utf-8 -*-
"""ivlev_py_alg_lesson2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tKlVaridXkFLUDyag7uIVB5yxZz2OLc

#Визуализация данных в Matplotlib

##Задание 1

Загрузите модуль pyplot библиотеки matplotlib с псевдонимом plt, а также библиотеку numpy с псевдонимом np.
Примените магическую функцию %matplotlib inline для отображения графиков в Jupyter Notebook и настройки конфигурации ноутбука со значением 'svg' для более четкого отображения графиков.
Создайте список под названием x с числами 1, 2, 3, 4, 5, 6, 7 и список y с числами 3.5, 3.8, 4.2, 4.5, 5, 5.5, 7.
С помощью функции plot постройте график, соединяющий линиями точки с горизонтальными координатами из списка x и вертикальными - из списка y.
Затем в следующей ячейке постройте диаграмму рассеяния (другие названия - диаграмма разброса, scatter plot).
"""

# Commented out IPython magic to ensure Python compatibility.
from matplotlib import pyplot as plt
import numpy as np
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]

plt.plot(x, y)
plt.show()

plt.scatter(x, y)
plt.show()

"""##Задание 2

С помощью функции linspace из библиотеки Numpy создайте массив t из 51 числа от 0 до 10 включительно.
Создайте массив Numpy под названием f, содержащий косинусы элементов массива t.
Постройте линейную диаграмму, используя массив t для координат по горизонтали,а массив f - для координат по вертикали. Линия графика должна быть зеленого цвета.
Выведите название диаграммы - 'График f(t)'. Также добавьте названия для горизонтальной оси - 'Значения t' и для вертикальной - 'Значения f'.
Ограничьте график по оси x значениями 0.5 и 9.5, а по оси y - значениями -2.5 и 2.5.
"""

t = np.linspace(0, 10, 51)
f = np.cos(t)

label_font = {
    "fontsize": 14,
}

title_font = {
    "fontsize": 16,
    "fontweight": "bold",
}

plt.plot(t, f, color="green")
plt.title('График f(t)', fontdict=title_font)
plt.xlabel('Значения t', fontdict=label_font)
plt.ylabel( 'Значения f', fontdict=label_font)
plt.axis([0.5, 9.5, -2.5, 2.5])
plt.show()

"""##*Задание 3

С помощью функции linspace библиотеки Numpy создайте массив x из 51 числа от -3 до 3 включительно.
Создайте массивы y1, y2, y3, y4 по следующим формулам:
y1 = x**2
y2 = 2 * x + 0.5
y3 = -3 * x - 1.5
y4 = sin(x)
Используя функцию subplots модуля matplotlib.pyplot, создайте объект matplotlib.figure.Figure с названием fig и массив объектов Axes под названием ax,причем так, чтобы у вас было 4 отдельных графика в сетке, состоящей из двух строк и двух столбцов. В каждом графике массив x используется для координат по горизонтали.В левом верхнем графике для координат по вертикали используйте y1,в правом верхнем - y2, в левом нижнем - y3, в правом нижнем - y4.Дайте название графикам: 'График y1', 'График y2' и т.д.
Для графика в левом верхнем углу установите границы по оси x от -5 до 5.
Установите размеры фигуры 8 дюймов по горизонтали и 6 дюймов по вертикали.
Вертикальные и горизонтальные зазоры между графиками должны составлять 0.3.
"""

x = np.linspace(-3, 3, 51)
y1 = x**2
y2 = 2*x + 0.5
y3 = -3*x - 1.5
y4 = np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()
ys = (y1, y2, y3, y4)
fig.set_size_inches(8, 6)
fig.subplots_adjust(wspace=0.3, hspace=0.3)

for ax, y, title in zip(ax.flatten(), ys, range(1, 5)):
  ax.plot(x, y)
  ax.set_title(f'График y{title}', fontdict=title_font)

ax1.set_xlim([-5, 5])

fig.show()

"""##*Задание 4

В этом задании мы будем работать с датасетом, в котором приведены данные по мошенничеству с кредитными данными.
Ознакомьтесь с описанием и скачайте датасет creditcard.csv с сайта Kaggle.com по ссылке: [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
Данный датасет является примером несбалансированных данных, так как мошеннические операции с картами встречаются реже обычных.
Импортируйте библиотеку Pandas, а также используйте для графиков стиль “fivethirtyeight”.
Посчитайте с помощью метода value_counts количество наблюдений для каждого значения целевой переменной Class и примените к полученным данным метод plot, чтобы построить столбчатую диаграмму. Затем постройте такую же диаграмму, используя логарифмический масштаб.
На следующем графике постройте две гистограммы по значениям признака V1 - одну для мошеннических транзакций (Class равен 1) и другую - для обычных (Class равен 0). Подберите значение аргумента density так, чтобы по вертикали графика было расположено не число наблюдений, а плотность распределения. Число бинов должно равняться 20 для обеих гистограмм, а коэффициент alpha сделайте равным 0.5, чтобы гистограммы были полупрозрачными и не загораживали друг друга. Создайте легенду с двумя значениями: “Class 0” и “Class 1”. Гистограмма обычных транзакций должна быть серого цвета, а мошеннических - красного. Горизонтальной оси дайте название “V1”.
"""

import pandas as pd

plt.style.use('fivethirtyeight')

from google.colab import drive
drive.mount('/content/drive')
DATASET_PATH = '/content/drive/My Drive/_ML/GB/5_py_alg/creditcard.csv'

df = pd.read_csv(DATASET_PATH, sep=',')
class_count = df['Class'].value_counts()

fig, ax = plt.subplots(nrows=1, ncols=2)
fig.subplots_adjust(wspace=0.3)
ax1, ax2 = ax.flatten()
class_count.plot(ax=ax1, kind="bar")
class_count.plot(ax=ax2, kind="bar", logy=True)
ax1.set_xlabel('normal scale', fontdict=label_font)
ax2.set_xlabel('log scale', fontdict=label_font)
fig.show()

fraud = df.loc[(df["Class"] == 1), "V1"]
regular = df.loc[(df["Class"] == 0), "V1"]
bins = 20

plt.hist(fraud, bins, alpha = 0.5, color='red', label='Class 1', density=True)
plt.hist(regular, bins, alpha = 0.5, color='grey', label='Class 0', density=True)
plt.legend(loc='upper left')
plt.xlabel('V1', fontdict=label_font)
fig.show()

"""##**Задание на повторение материала

###1. Создать одномерный массив Numpy под названием a из 12 последовательных целых чисел чисел от 12 до 24 невключительно
"""

a = np.arange(12, 24)
print(f'Искомый массив:\n{a}')
print(f'Его длина: {len(a)}')

"""###2. Создать 5 двумерных массивов разной формы из массива a. Не использовать в аргументах метода reshape число -1."""

a1 = a.reshape((2, 6))
a2 = a.reshape((3, 4))
a3 = a.reshape((4, 3))
a4 = a.reshape((6, 2))
a5 = a.reshape((12, 1))

arrays = (a1, a2, a3, a4, a5)

for i, array in enumerate(arrays):
  print(f'Массив номер {i+1}:\n{array}\n')

"""###3. Создать 5 двумерных массивов разной формы из массива a. Использовать в аргументах метода reshape число -1 (в трех примерах - для обозначения числа столбцов, в двух - для строк)."""

a1 = a.reshape((2, -1))
a2 = a.reshape((3, -1))
a3 = a.reshape((4, -1))
a4 = a.reshape((-1, 2))
a5 = a.reshape((-1, 1))

arrays = (a1, a2, a3, a4, a5)

for i, array in enumerate(arrays):
  print(f'Массив номер {i+1}:\n{array}\n')

"""###4. Можно ли массив Numpy, состоящий из одного столбца и 12 строк, назвать одномерным?

Полагаю, что **нельзя** - у массива есть один столбец и двенадцать строк, для доступа к элементу необходимо **два** индекса.

###5. Создать массив из 3 строк и 4 столбцов, состоящий из случайных чисел с плавающей запятой из нормального распределения со средним, равным 0 и среднеквадратичным отклонением, равным 1.0. Получить из этого массива одномерный массив с таким же атрибутом size, как и исходный массив.
"""

b = np.random.randn(3, 4)
b_flat = b.flatten()
print(f'Требуемый массив 3 на 4:\n{b}')
print(f'\nТребуемый одномерный массив:\n{b_flat}')
if b.size == b_flat.size:
  print('\nБинго! Size совпадает.')

"""###6. Создать массив a, состоящий из целых чисел, убывающих от 20 до 0 невключительно с интервалом 2."""

a = [el for el in range(20, 0, -2)]
print(f'Требуемый массив:\n{a}')

"""###7. Создать массив b, состоящий из 1 строки и 10 столбцов: целых чисел, убывающих от 20 до 1 невключительно с интервалом 2. В чем разница между массивами a и b?"""

b = np.array([el for el in range(20, 1, -2)])
print(f'Требуемый массив:\n{b}')

"""На мой взгляд, разница между ними в мерности. Первый массив - одномерный, второй - двумерный.

###8. Вертикально соединить массивы a и b. a - двумерный массив из нулей, число строк которого больше 1 и на 1 меньше, чем число строк двумерного массива b, состоящего из единиц. Итоговый массив v должен иметь атрибут size, равный 10.
"""

b_col = 2
b_row = int(5/b_col + 0.5)
a_col = int(b_col)
a_row = int(b_row - 1)

a = np.zeros((a_row, a_col))
b = np.ones((b_row, b_col))
c = np.vstack((a, b))

print(f'Требуемый массив:\n{c}')
print(f'\nЕго атрибут size: {c.size}')

"""###9. Создать одномерный массив а, состоящий из последовательности целых чисел от 0 до 12. Поменять форму этого массива, чтобы получилась матрица A (двумерный массив Numpy), состоящая из 4 строк и 3 столбцов. Получить матрицу At путем транспонирования матрицы A. Получить матрицу B, умножив матрицу A на матрицу At с помощью матричного умножения. Какой размер имеет матрица B? Получится ли вычислить обратную матрицу для матрицы B и почему?"""

a = np.arange(0, 12)
print(f'Требуемый массив a:\n{a}')
A = a.reshape((4, 3))
print(f'\nТребуемая матрица A:\n{A}')
A_T = A.T
print(f'\nТребуемая матрица A_T:\n{A_T}')
B = A.dot(A_T)
print(f'\nТребуемая матрица B:\n{B}')
print(f'\nМатрица B имеет размер {B.shape[0]} на {B.shape[1]}')
print('Обратную матрицу для матрицы B вычислить не представляется возможным.')
print('Она вырожденная.')
print(f'Определитель матрицы B: {np.linalg.det(B)}')

"""###10. Инициализируйте генератор случайных числе с помощью объекта seed, равного 42."""

np.random.seed(42)
print(np.random.rand(3))
np.random.seed(42)
print(np.random.rand(3))

"""###11. Создайте одномерный массив c, составленный из последовательности 16-ти случайных равномерно распределенных целых чисел от 0 до 16 невключительно. """

c = np.random.randint(0, 16, 16)
print(f'Требуемый массив c:\n{c}')

"""###12. Поменяйте его форму так, чтобы получилась квадратная матрица C. Получите матрицу D, поэлементно прибавив матрицу B из предыдущего вопроса к матрице C, умноженной на 10. Вычислите определитель, ранг и обратную матрицу D_inv для D."""

C = c.copy()
n = int(c.size**0.5)
C.resize((n, n))
print(f'Требуемая матрица С:\n{C}')
D = B + C*10
print(f'\nТребуемая матрица D:\n{D}')
print(f'Определитель матрицы D: {np.linalg.det(D):.0f}')
print(f'Ранг матрицы D: {np.linalg.matrix_rank(D)}')
D_inv = np.linalg.inv(D)
print(f'\nТребуемая матрица D_inv:\n{D_inv}')

"""###13. Приравняйте к нулю отрицательные числа в матрице D_inv, а положительные - к единице. Убедитесь, что в матрице D_inv остались только нули и единицы. С помощью функции numpy.where, используя матрицу D_inv в качестве маски, а матрицы B и C - в качестве источников данных, получите матрицу E размером 4x4.  Элементы матрицы E, для которых соответствующий элемент матрицы D_inv равен 1, должны быть равны соответствующему элементу матрицы B, а элементы матрицы E, для которых соответствующий элемент матрицы D_inv равен 0, должны быть равны соответствующему элементу матрицы C."""

mask = np.array(D_inv > 0, dtype=np.int64)
print(f'Требуемая матрица-маска:\n{mask}')
E = np.where(mask, B, C)
print(f'\nИсходная матрица B:\n{B}')
print(f'\nИсходная матрица С:\n{C}')
print(f'\nТребуемая матрица E:\n{E}')
