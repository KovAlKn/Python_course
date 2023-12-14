'''Узнать какая максимальная households в зоне минимального значения population'''
from pandas import read_csv

data = read_csv('california_housing_test.csv')
max_households_in_min_population = data[(data['population']==data['population'].min())]['households'].max()
print(max_households_in_min_population)