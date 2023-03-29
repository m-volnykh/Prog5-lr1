def fib(n):
    """
    Список чисел ряда Фибоначчи 

    Возвращает значения не превосходящие данное n

    Например: 
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]

    """
    lst = [0, 1]
    while lst[-1] <= n:
        lst.append(lst[-1] + lst[-2])
    lst.pop()
    return lst


def num_input(in_list):
    while True:
        num = input()
        if num != "":
            in_list.append(int(num))
        else:
            break


def fib_iter(l):
    from itertools import filterfalse
    fib_l = fib(max(l))
    l_new = list(filterfalse(lambda x: x not in l, fib_l))
    return l_new


def fib_gen(l):
    while True:
        i = l[-2]
        yield i + l[-1]


def fib_gen_ver(n):
    el = [0, 1]
    g = fib_gen(el)
    while el[-1] <= n:
        el.append(next(g))
    el.pop()
    return el


class FibonacchiLst:

    def __init__(self, instance):
        self.instance = instance   
        self.idx = 0 
        
        
    def __iter__(self):
        return self 
    

    def fibcls(self, n): 
        lst = [0, 1]
        while lst[-1] <= n:
            lst.append(lst[-1] + lst[-2])
        lst.pop()
        return lst


    def __next__(self): 
        fib_instance = self.fibcls(max(self.instance)) 
        while True:
            try:
                res = fib_instance[self.idx] 
                
            except IndexError:
                raise StopIteration
            
            if res in self.instance: 
                self.idx += 1
                return res

            self.idx += 1


def main():
    n1 = int(input("Задание 1\nВведите максимальное значение элементов ряда Фибоначчи: "))
    fib_list = fib(n1)
    print(fib_list)
  
    user_lst_2 = []
    print("\nЗадание 2\nВведите список чисел:")
    num_input(user_lst_2)
    print(list(FibonacchiLst(user_lst_2)))
  
    user_lst_3 = []
    print("\nЗадание 3\nВведите список чисел:")
    num_input(user_lst_3)
    print(fib_iter(user_lst_3))
  
    n2 = int(input("\nЗадание 4\nВведите максимальное значение элементов ряда Фибоначчи: "))
    fib_gen_list = fib_gen_ver(n2)
    print(fib_gen_list)


if __name__ == '__main__':
    main()