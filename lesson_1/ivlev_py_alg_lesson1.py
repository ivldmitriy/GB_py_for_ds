# -*- coding: utf-8 -*-
"""ivlev_py_alg_lesson1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12nsKS2c0OUNNIW3JDUAbUFVL_UXaB-m5

#Theme 1
Вычисления с помощью Numpy

##Task 1
Импортируйте библиотеку Numpy и дайте ей псевдоним np.
Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.
"""

import numpy as np
a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]]).T
print('Матрица наблюдения-признаки')
print(a)
a_mean = a.mean(axis=0)
print(f'Среднее по первому и второму признаку соответственно {a_mean[0]} и {a_mean[1]}')

"""##Task 2
Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.
"""

a_centered = a - a_mean
print('Центрированная матрица наблюдения-признаки')
print(a_centered)

"""##Task 3
Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.
"""

a_centered_sp = np.dot(a_centered[:,0], a_centered[:,1])
cov_home = a_centered_sp / (a_centered.shape[0]-1)
print(f'Несмещенная оценка ковариации "домашним" методом: {cov_home}')

"""##Task 4*
В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.
"""

cov = np.cov(a_centered.T)
print(f'Несмещенная оценка ковариации встроенной функцией np: {cov[0,1]}')

"""##Task 5**
Необходимо реализовать метод сортировки целых (int) элементов. Метод должен быть реализован без использования “готовых” методов ( sorted, np.sort() ).
"""

#сортировка пузырьком - парный обмен
def sorter(b):
  a = b.copy()
  iterate = True
  while iterate:
    iterate = False
    for i in range(len(a) - 1):
      if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        iterate = True
  return a

print(f'Несортированный массив: {a[:, 1]}')
print(f'Cортированный массив: {sorter(a[:, 1])}')

"""#Theme 2
Работа с данными в Pandas

##Task 1
Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
[1, 1, 1, 2, 2, 3, 3],
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290].
"""

import pandas as pd
d1 = {
    'author_id': [1, 2, 3], 
    'author_name':['Тургенев', 'Чехов', 'Островский']
    }
authors = pd.DataFrame(d1)

d2 = {
    'author_id': [1, 1, 1, 2, 2, 3, 3], 
    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 
                   'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
    'price':  [450, 300, 350, 500, 450, 370, 290]
    }
book = pd.DataFrame(d2)

print(authors)
print('\n')
print(book)

"""##Task 2
Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

"""

authors_price = pd.merge(authors, book, on='author_id', how='left')
print(authors_price)

"""##Task 3
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
"""

authors_price = authors_price.sort_values(by='price', ascending=False)
authors_price = authors_price.reset_index(drop=True)
top5 = authors_price.head()
print(top5)

"""##Task 4
Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price,
в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

"""

author_name = authors_price.groupby("author_name")
authors_stat = pd.DataFrame(author_name.agg({'price' : ['min', 'max', 'mean']})).reset_index()
authors_stat = authors_stat.rename(columns={'price': '_price'})
authors_stat.columns = authors_stat.columns.swaplevel()
authors_stat.columns = [''.join(col) for col in authors_stat.columns]
print(authors_stat)

"""## Task 5*
Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.

"""

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print('Дополнили authors_price:')
print(authors_price)

book_info = pd.pivot_table(authors_price, values='price' , index='author_name',columns='cover', aggfunc=sum, fill_value=0)
print('\nПолучили book_info:')
print(book_info)

book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print('\nПолучили book_info2:')
print(book_info2)

if book_info.equals(book_info2) and book_info.index.names == book_info2.index.names:
  print('\nОни идентичны!')

"""## Task 5**
Вычисление метрик для мониторинга.

1.   суммарная выручка
2.   кол-во покупок
3.   средний чек
4.   среднее кол-во товаров в покупке

Дополнительно добавим возможность фильтровать данные по различным параметрам. Это может быть полезно чтобы посмотреть как меняются продажи в двух группах, или в какой-то отдельной категории товаров.
На вход функции будет подаваться датафрейм с данными о продажах, словарь с фильтрами и период, за который нужно посчитать метрики.
Функция должна вернуть датафрейм, в индексах которого будут все даты из указанного периода отсортированные по возрастанию, а столбцы - метрики ['revenue', 'number_purchases', 'average_check', 'average_number_items']. Формат данных столбцов - float, формат данных индекса - datetime64[ns].
Если в какие-то дни не было продаж, то нужно заполнить пропуск нулём.
"""

import pandas as pd

def calculate_sales_metrics(df, cost_name, date_name, sale_id_name, number_items_name, period, filters=None):
  print('Исходные данные:')
  print(df)
  print('\n')
  begin = pd.to_datetime(period['begin'])
  end = pd.to_datetime(period['end'])

  # сортировка по дате и выделение временного периода
  df[date_name] = pd.to_datetime(df[date_name])
  df = df.sort_values(by=date_name)
  mask = (df[date_name] >= begin) & (df[date_name] < end)
  data = df.loc[mask]
  print('Получаем данные за период:')
  print(data)
  print('\n')

  # фильтрация
  if filters:
    for key, bandpass in filters.items():
      #data = data.loc[~data[key].isin(bandpass)]
      data = data.query(f"{key} in {bandpass}")

  print('Фильтруем:')
  print(data)
  print('\n')

  # расчет метрик
  #суммарная выручка, кол-во покупок, средний чек, среднее кол-во товаров в покупке
  groupby = data.groupby(date_name)
  stat = pd.DataFrame(groupby.agg({cost_name : ['sum', 'mean'], number_items_name: ['count', 'mean']}))
  stat.columns = ['revenue', 'average_check', 'number_purchases', 'average_number_items']
  stat.index.name = None
  stat = stat[['revenue', 'number_purchases', 'average_check', 'average_number_items']]
  print('Анализируем метрики:')
  print(stat)

  return stat

sales = pd.DataFrame(
           [[820, '2021-04-03', 1, 5, 213],
            [740, '2019-03-04', 2, 6, 1],
            [250, '2020-01-07', 3, 2, 123],
            [360, '2020-01-07', 4, 3, 123],
            [220, '2020-01-07', 5, 1, 123],
            [350, '2020-01-07', 6, 3, 213],
            [347, '2018-06-23', 7, 2, 214],
            ],
           columns=['cost', 'date', 'sale_id', 'number_items', 'shop_id']
       )

period = {'begin': '2019-01-01', 'end': '2021-01-08'}
filter = {'shop_id': [1, 123, 943]}

res = calculate_sales_metrics(sales, 'cost', 'date', 'sale_id', 'number_items', period, filters=filter)
res.to_pickle('metrics.pkl')

