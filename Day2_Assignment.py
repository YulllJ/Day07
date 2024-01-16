#
# while True:
#     menu = input("1) Farenheit -> Celsius 2) Celsius -> Farenheit  3) Quit Program: ")
#     if menu == '1' :
#         farenheit=float(input('Input Farenheit : '))
#         print(f'Farenheit :{farenheit}F, Celsius : {((farenheit-32.0)*5/9):.4f}C')
#     elif menu == '2' :
#         Celsius=float(input('Input Celsius : '))
#         print(f'Farenheit :{((Celsius*9/5)+32.0):.4f}F, Celsius : {Celsius}C')
#     else:
#         print("terminate program")
#         break
numbers=input("Input first second number : ").split()
n1=int(numbers[0])
n2=int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1
#파이썬은 이렇게 바로 가능 (packing, unpacking의 관계임)
for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        #print(f'{number} is not prime number')
        pass #아무것도 하지 않는데 지나갈 때 사용하는 코드 continue는 위로 올라가는 것임
    else :
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')