'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.'''

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5'

first =var2.split()
first_set=set(first
              )
second = var3.split()
second_set= set(second)

cross= first_set.intersection(second_set)
sorted_cross=sorted(cross)
print(' '.join(sorted_cross))



