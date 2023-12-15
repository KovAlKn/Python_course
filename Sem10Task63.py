import pandas as pd 
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('california_housing_test.csv')

#1. Изобразите отношение households к population с помощью точечного графика
sns.scatterplot(data=df, x='households', y='population')
plt.show()

#2. Визуализировать longitude по отношения к median_house_value, используя линейный график
sns.relplot(x='longitude',y='median_house_value',data=df,kind='line')
plt.show()

#3. Представить гистограмму по housing_median_age
sns.histplot(data=df,x='housing_median_age')
plt.show()

#4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
sns.histplot(data=df,x='median_house_value',hue='housing_median_age')
plt.show()