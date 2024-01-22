#composition은 안에 있는거 # aggregation은 바깥에 있는것 애매하면 association
# module import할때는 어떤 모듈인지 써줘야돼
'''
import mymath


while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {mymath.fahrenheit_to_celsius(fahrenheit):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        if mymath.isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if mymath.isprime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Menu!')
# module

from mymath import * # 이렇게 하면 이름 없애줘야돼


while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {fahrenheit_to_celsius(fahrenheit):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        if isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Menu!')
# 어떤 모듈에서 온건지 알필요가 있어 개발할때 완전히 없애서 쓰지는 않아
# 모듈들 안에 같은 이름 함수 있을수있어 적당하게 타협해서 두가지 섞어서 쓴다
'''

import mymath as mm # 이렇게 하면 이름 없애줘야돼


while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {mm.fahrenheit_to_celsius(fahrenheit):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        if mm.isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if mm.isprime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Menu!')
#절충 버전으로 이름을 안겹치게 어디에서온 함수인지 쓰되, 너무 기니까 줄여서 쓰는 절충안을 많이 사용함 pandas를 pd로 한다든가....
