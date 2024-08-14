def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
    

def factors(b):
    for i in range(1, b+1):
        if is_factor(i, b):
            print(i)


if __name__ == '__main__':

    b = input('Введите число: ')
    
    if b.isdigit() and int(b) > 0:
        factors(int(b))
    else:
        print('Ошибка ввода: нужно ввести целое положительное число')

