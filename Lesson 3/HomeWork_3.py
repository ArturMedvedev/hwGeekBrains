'''
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(var_1, var_2, var_3):
    '''
    Функция принимает 3 аргумента
    :param var_1: - float
    :param var_2: - float
    :param var_3: - float
    :return: - сумма наибольших двух
    '''
    my_list = [var_1, var_2, var_3]
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    return float(max_1) + float(max_2)

result = my_func(3.14, 25.3, 18.4)
print(result)