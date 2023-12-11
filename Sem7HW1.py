'''Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве
аргумента функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.'''
def operation(a):
    return a

def print_operation_table(operation, rows=9, columns=9):
    if rows<2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        first_line=[]
        for k in range(1,columns+1):
            first_line.append(str(k))
        print(' '.join(first_line))

        for i in range(2,rows+1):
            row=[]
            for j in range(1,columns+1):
                if j==1:
                    row_str=str(i)
                else:
                    row.append(str(operation(i,j)))
            line=' '.join(row)
            print(row_str+line)



# print_operation_table(lambda x, y: x * y, 3, 3)
# print_operation_table(lambda x, y: x + y, 4, 4)
# print_operation_table(lambda x, y: x - y, 5, 5)
# print_operation_table(lambda x, y: x / y, 4, 4)
# print_operation_table(lambda x, y: x * y)