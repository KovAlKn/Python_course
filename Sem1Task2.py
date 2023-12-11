'''Найдите сумму цифр трехзначного числа.'''

num= int(input('Введите 3-х значное число '))
a=num//100
rest=num%100
b= rest//10
sum=a+b+rest%10
print(sum)