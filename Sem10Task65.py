'''Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
'''

import pandas as pd 
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
print(penguins.head())

# sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g')
# sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g',hue='sex', size= 'island', style='island')

#● Использовать PairGrid с типом графика на ваш выбор 
# x_vars = ['body_mass_g','bill_length_mm','bill_depth_mm','flipper_length_mm']
# y_vars = ['sex']
# pg=sns.PairGrid(penguins, x_vars=x_vars,y_vars=y_vars, hue='species')
# pg.map(sns.scatterplot)

#● Изобразить Heatmap
# data= penguins.pivot_table(index='species', columns='island', values='body_mass_g')
# sns.heatmap(data)
# plt.xlabel('Остров', size=14)
# plt.ylabel('Вид пингвина', size=14)

#● Использовать 2-3 гистограммы
penguins['bill_depth_mm'].hist(bins=5)

plt.show()