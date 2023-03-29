from .calc_log import write_log
from .calc_print import print_results
from .module import load_params, PARAMS, sqrtDisp, convert_precision, calculate 
from datetime import datetime 


load_params()    
ndigits = convert_precision(PARAMS['precision'])
r_type = PARAMS['output_type']
p_acts = PARAMS['possible_actions']
dest = PARAMS['destination']
  
act = input("Введите действие: ")
if act not in p_acts:
    print("Таких действий в калькуляторе нет")
  
if act == 'S':
    op_lst = []
    op = input("Введите аргумент: ")
    while op != '':
        op_lst.append(float(op))
        op = input("Введите аргумент: ")
    r = sqrtDisp(*op_lst)
    r = round(r, ndigits);
    if r_type == int:
        r = int(r)
    print("Результат: ", r)

    print_results(*op_lst, action=act, result=r)
  
    current_time = str(datetime.now())[0:19]
    write_log(*op_lst, time=current_time, action=act, result=r, file=dest)

else:
    op1 = float(input("Введите операнд 1: "))
    op2 = float(input("Введите операнд 2: "))
    r = calculate(op1, op2, act)
    r = round(r, ndigits);
    if r_type == int:
        r = int(r)
    print("Результат: ", r)

    print_results(*(op1, op2), action=act, result=r)
  
    current_time = str(datetime.now())[0:19]
    write_log(*(op1, op2), time=current_time, action=act, result=r, file=dest)

