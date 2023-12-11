print('Витя сел в вагон от головы поезад:')
i = int(input())
print("номер вагона на табличке:")
j = int(input())
if i==j:
    print('Неизвестно')
else:
    print(f'В электричке {i+j-1} вагонов')
