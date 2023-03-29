import configparser
import math


PARAMS = {
        'precision': None,
        'output_type': None,
        'possible_actions': None,
        'destination': None
}


def load_params(file="params.ini"):

    global PARAMS
    config = configparser.ConfigParser()
    config.read(file)
    PARAMS['precision'] = config['Params']['precision']
    PARAMS['output_type'] = config['Params']['output_type']
    PARAMS['possible_actions'] = config['Params']['possible_actions']
    PARAMS['destination'] = config['Params']['destination']


def convert_precision(precision):
    """
    Функция возвращает количество знаков дробной части в
    заданной точности

    precision: заданная точность
    """
    string = str(precision)
    i_exp = string.find('e')
    if i_exp != -1:
        i = abs(int(string[i_exp+1:]))
        return i
    else:
        for i in range(len(str(precision))):
            if float(precision) * 10**i >= 1:
                return i


def sqrtDisp(*args):
    """
    Функция находит среднеквадратическое отклонение S

    *args: список произвольного количества числовых значений,
    необходимых для нахождения S
    """
    averageX = 0
    n = 0
    for x in args:
        averageX += x
        n += 1
    averageX /= n

    s = 0
    for x in args:
        temp = (x - averageX)
        s += temp*temp
    s /= n
    s = math.sqrt(s)
    
    return s


def calculate(op1, op2, act):
    """
    Функция определяет, какое действие нужно выполнить,
    выполняет заданное выражение и возвращает полученное
    значение

    op1: значение первого операнда
    op2: значение второго операнда
    act: выполняемое действие 
    """

    if act == '+':
        r = op1 + op2
   
    elif act == '-':
        r = op1 - op2
   
    elif act == '*':
        r = op1 * op2
   
    elif act == '/':
        if op2 != 0:
            r = op1 / op2
        else:
            r = 'Деление на ноль невозможно'
   
    elif act == '^':
        if op1 < 0 and 0 < op2 < 1:
            r = 'Недопустимое значение основания'
        else:
            r = op1**op2
   
    elif act == '//':
        if op2 != 0:
            r = abs(op1) // abs(op2)
        else:
            r = 'Деление на ноль невозможно'
   
    elif act == '%':
        if op2 != 0:
            r = op1 % op2 
        else:
            r = 'Деление на ноль невозможно'
   
    else:
        r = 'Такой операции нет'

    return r




