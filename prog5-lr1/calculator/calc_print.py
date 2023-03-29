def print_results(*args, action = None, result = None, last_column=""):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде. 
    Последний аргумент в упакованном кортеже - результат вычислений, 
    Предпоследний - действие, которое выполнилось, остальные — аргументы, с которыми это действие выполнилось.
    """
    import string
    last_column = last_column + " " + action
    operands = {}
    _i = 0
    for op in args:
        operands[string.ascii_uppercase[_i]] = op
        _i += 1

    lst1 = []
    lst2 = []
    if len(last_column) > len(str(result)):
        draw_lst(lst1, last_column)
        draw_lst(lst2, str(result).center(len(last_column)))
    elif len(last_column) < len(str(result)):
        draw_lst(lst1, last_column.center(len(str(result))))
        draw_lst(lst2, str(result))
    else:
        draw_lst(lst1, last_column)
        draw_lst(lst2, str(result))
    for x in range(_i):
        a = operands.popitem()
        leng_a1 = len(str(a[1]))
        if leng_a1 > len(a[0]):
            a_ex = a[0].center(leng_a1)
            draw_lst(lst1, a_ex)
        else:
            draw_lst(lst1, a[0])
        draw_lst(lst2, str(a[1]))
    lst1.reverse()
    lst2.reverse()
    s1 = ''.join(lst1)
    s2 = ''.join(lst2)
    
    draw_border(len(s1))
    print('||', end="")
    print(s1)
    draw_border(len(s2))
    print('||', end="")
    print(s2)
    draw_border(len(s2))


def draw_border(n, t='='):
    print(' ' + t * (n - 1) + ' ')


def draw_lst(lst, string):
    lst.append(' ' + string + ' ||')   