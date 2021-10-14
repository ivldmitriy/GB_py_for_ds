# -*- coding: utf-8 -*-
"""ivlev_py_alg_lesson3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HL9dk2ITdnDKm567PKB-pwznDib8rEQA

#Обучение с учителем

##Задание 1
"""

# Импортируем базовые бибилиотеки numpy, pandas
import numpy as np
import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
# Импорт matplotlib
from matplotlib import pyplot as plt
# %config InlineBackend.figure_format = 'svg'
# %matplotlib inline

# Импортируем модули из библиотеки scikit-learn
from sklearn.datasets import load_boston, load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, roc_auc_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Загружаем тренировочный датасет и формируем датафреймы pandas
boston = load_boston()
data = boston.data
feature_names = boston.feature_names
target = boston.target
X = pd.DataFrame(data, columns=feature_names)
y = pd.DataFrame(target, columns=["price"])
print('\nИнформация о матрице признаков:')
X.info()
print('\nИнформация о целевом признаке:')
y.info()

print(boston["DESCR"])

# Разделям датасеты на обучающие и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Строим модель регрессии 
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# Проверка точности предсказаний
# Формируем датасет для проверки
check_test_lr = pd.DataFrame({
    "y_test": y_test["price"],
    "y_pred": y_pred.flatten(),
})
check_test_lr["error"] = check_test_lr["y_pred"] - check_test_lr["y_test"]
print(check_test_lr.head())

# Расчитываем коэффициент детерминации
r2_lr = r2_score(check_test_lr["y_pred"], check_test_lr["y_test"])
print(f'Коэффициент детерминации R2: {r2_lr:.2f}')

# Визуально оценим, какой коэффициент имеет наибольший вклад
plt.barh(feature_names, lr.coef_.flatten())
plt.xlabel("Вес признака")
plt.ylabel("Признак")
plt.show()

#проведем стандартизацию признаков, чтобы трезво оценить веса
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_train_scaled = pd.DataFrame(X_train_scaled, columns=feature_names)
X_test_scaled = scaler.fit_transform(X_test)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=feature_names)

#Обучим модель заново
lr.fit(X_train_scaled, y_train)

# Визуально оценим, какой коэффициент теперь имеет наибольший вклад
plt.barh(feature_names, lr.coef_.flatten())
plt.xlabel("Вес признака")
plt.ylabel("Признак")
plt.show()

"""##Задание 2"""

# Импортируем модули из библиотеки scikit-learn
from sklearn.ensemble import RandomForestRegressor

# Строим модель решающих деревьев
model = RandomForestRegressor(n_estimators=1000, max_depth=12, random_state=42)

# Обучаем модель и используем ее
model.fit(X_train, y_train.values[:,0])
y_pred_rf = model.predict(X_test)

# Проверка точности предсказаний
# Формируем датасет для проверки
check_test_rf = pd.DataFrame({
    "y_test": y_test["price"],
    "y_pred": y_pred_rf.flatten(),
})
check_test_rf["error"] = check_test_rf["y_pred"] - check_test_rf["y_test"]
print(check_test_rf.head())

# Расчитываем коэффициент детерминации
r2_rf = r2_score(check_test_rf["y_pred"], check_test_rf["y_test"])
print(f'Коэффициент детерминации R2: {r2_rf:.2f}')



"""Метод случайного леса отработал лучше - коэффициент детерминации 0,85 против 0,67 у метода линейной регрессии.

##*Задание 3

Вызовите документацию для класса RandomForestRegressor,
найдите информацию об атрибуте feature_importances_.

С помощью этого атрибута найдите сумму всех показателей важности,
установите, какие два признака показывают наибольшую важность.
"""

feature_importances = pd.DataFrame(model.feature_importances_, columns = ['importance'], index=feature_names)
feature_importances = feature_importances.sort_values(by='importance', ascending=False)
sum_importance = feature_importances['importance'].sum()
print(f'Сумма всех показателей важности: {sum_importance:.2f}\n')
n=2
print(f'{n} признака с наибольшей важностью:')
print(feature_importances.head(n))

"""##*Задание 4"""

#Импортируйте из соответствующих модулей RandomForestClassifier, GridSearchCV и train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

#Загрузите датасет creditcard.csv и создайте датафрейм df
from google.colab import drive
drive.mount('/content/drive')
DATASET_PATH = '/content/drive/My Drive/_ML/GB/5_py_alg/creditcard.csv'
df = pd.read_csv(DATASET_PATH, sep=',')

#С помощью метода value_counts с аргументом normalize=True убедитесь в том, что выборка несбалансирована 
print(f'Частота встречаемости значений каждого класса:\n{df["Class"].value_counts(normalize=True)}\n')
#Используя метод info, проверьте, все ли столбцы содержат числовые данные и нет ли в них пропусков
print(f'Информация по датасету:')
df.info()

#Примените следующую настройку, чтобы можно было просматривать все столбцы датафрейма: pd.options.display.max_columns = 100
pd.options.display.max_columns = 100
#Просмотрите первые 10 строк датафрейма df
df.head(10)

#Создайте датафрейм X из датафрейма df, исключив столбец Class
X = df.drop(['Class'], axis = 1)
#Создайте объект Series под названием y из столбца Class
y = pd.Series(data=df['Class'])
#Разбейте X и y на тренировочный и тестовый наборы данных при помощи функции train_test_split, используя аргументы: test_size=0.3, random_state=100, stratify=y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)
#У вас должны получиться объекты X_train, X_test, y_train и y_test. Просмотрите информацию о их форме
print(f'Информация по форме датасета X_train:\n{X_train.shape}')
print(f'\nИнформация по форме датасета X_test:\n{X_test.shape}')
print(f'\nИнформация по форме датасета y_train:\n{y_train.shape}')
print(f'\nИнформация по форме датасета y_test:\n{y_test.shape}')

#Для поиска по сетке параметров задайте такие параметры: parameters = [{'n_estimators': [10, 15], 'max_features': np.arange(3, 5), max_depth': np.arange(4, 7)}]
parameters = [{'n_estimators': [10, 15], 'max_features': np.arange(3, 5), 'max_depth': np.arange(4, 7)}]
#Создайте модель GridSearchCV со следующими аргументами: estimator=RandomForestClassifier(random_state=100), param_grid=parameters, scoring='roc_auc', cv=3
grid_model = GridSearchCV(estimator=RandomForestClassifier(random_state=100), param_grid=parameters, scoring='roc_auc', cv=3)

#Обучите модель на тренировочном наборе данных
grid_model.fit(X_train, y_train)

#Просмотрите параметры лучшей модели с помощью атрибута best_params_
fitted_parameters = grid_model.best_params_
print(f'Наилучшие параметры для модели:\n{fitted_parameters}')

#Предскажите вероятности классов с помощью полученнной модели и метода predict_proba
class_probs = grid_model.predict_proba(X_test)
#Из полученного результата (массив Numpy) выберите столбец с индексом 1 (вероятность класса 1) и запишите в массив y_pred_proba
y_pred_proba = class_probs[:,1]

#Из модуля sklearn.metrics импортируйте метрику roc_auc_score.
from sklearn.metrics import roc_auc_score

#Вычислите AUC на тестовых данных и сравните с результатом,полученным на тренировочных данных, используя в качестве аргументов массивы y_test и y_pred_proba.
auc_score = roc_auc_score(y_test, y_pred_proba)
print(f'Искомая метрика: {auc_score:.2f}')

"""##*Дополнительные задания

*Дополнительные задания:
"""

#1). Загрузите датасет Wine из встроенных датасетов sklearn.datasets с помощью функции load_wine в переменную data
wine = load_wine()
wine_data = wine['data']

#2)Просмотрите тип данных этой структуры wine и создайте список data_keys, содержащий ее ключи.
wine_data_keys = wine.keys()
print(f'Ключи датасета: {wine_data_keys}')
print(f'Тип данных структуры wine: {type(wine)}')
print(f'Тип данных структуры data: {type(data)}')

#3). Просмотрите данные, описание и названия признаков в датасете. 
#Описание нужно вывести в виде привычного, аккуратно оформленного текста, без обозначений переноса строки, но с самими переносами и т.д.
print(wine['DESCR'])

#4). Сколько классов содержит целевая переменная датасета? Выведите названия классов.
class_names = set(wine["target"])
print(f'Целевая переменная содержит {len(class_names)} класса:')
for i in class_names:
  print(f'Class_{i}')

#5). На основе данных датасета (они содержатся в двумерном массиве Numpy) и названий признаков создайте датафрейм под названием X.
wine_X = pd.DataFrame(wine_data, columns=wine['feature_names'])
wine_X.head()

#6). Выясните размер датафрейма X и установите, имеются ли в нем пропущенные значения.
print(f'Информация по датасету:')
wine_X.info()
print(f'\nРазмер датасета:{wine_X.shape}')

#7). Добавьте в датафрейм поле с классами вин в виде чисел, имеющих тип данных numpy.int64. Название поля - 'target'.
wine_X['target'] = wine['target']
wine_X['target'] = wine_X['target'].astype(np.int64)
wine_X.info()

#8). Постройте матрицу корреляций для всех полей X. Дайте полученному датафрейму название X_corr.
wine_X_corr = wine_X.corr()

#9). Создайте список high_corr из признаков, корреляция которых с полем target по абсолютному значению превышает 0.5 (причем, само поле target не должно входить в этот список).
target_corr = wine_X_corr.loc[:, 'target'].drop('target')
high_corr = [i for i in target_corr.index if abs(target_corr[i])>0.5]

#10). Удалите из датафрейма X поле с целевой переменной. 
#Для всех признаков, названия которых содержатся в списке high_corr, вычислите квадрат их значений 
#и добавьте в датафрейм X соответствующие поля с суффиксом '_2', добавленного к первоначальному названию признака. 
#Итоговый датафрейм должен содержать все поля, которые, были в нем изначально, а также поля с признаками из списка high_corr, возведенными в квадрат. 
#Выведите описание полей датафрейма X с помощью метода describe.
#wine_X = wine_X.drop(['target'], axis=1)
for name in wine_X.columns:
  if name in high_corr:
    wine_X[f'{name}^2'] = wine_X[f'{name}']**2
#wine_X.head()
wine_X.describe()
