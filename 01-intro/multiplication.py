def multi_table(a):
    '''Вывод таблицы умножения для числа'''
    for i in range(1, 11):
        print(f'{a} x {i} = {a*i}')




if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))