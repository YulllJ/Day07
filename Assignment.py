#예외처리, 중복된 코드, 계산량도 발생, 입력받는 부분도 가독성 높이고 간결하게 줄이기 가능, 소수 아닐때는 반복문 금방 끝내버리지만 소수일떄는 쓸데없이 반복문 돌아
while True:
    menu = input("1) Farenheit -> Celsius 2) Celsius -> Farenheit  3) is_Prime 4) is_Prime in range 5) Quit Program: ")
    if menu == '1' :
        farenheit=float(input('Input Farenheit : '))
        print(f'Farenheit :{farenheit}F, Celsius : {((farenheit-32.0)*5/9):.4f}C')
    elif menu == '2' :
        Celsius=float(input('Input Celsius : '))
        print(f'Farenheit :{((Celsius*9/5)+32.0):.4f}F, Celsius : {Celsius}C')
    elif menu == '3':
        # prime number
        number = int(input("Input number : "))
        is_prime = True
        if number < 2:
            print(f'{number} is NOT prime number!')
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')


    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        # 파이썬은 이렇게 바로 가능 (packing, unpacking의 관계임)
        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                # print(f'{number} is not prime number')
                pass  # 아무것도 하지 않는데 지나갈 때 사용하는 코드 continue는 위로 올라가는 것임
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')
        print("\n")

    elif menu == '5':
        print("terminate program")
        break
    else :
        print("Invalid value")

#
# #반복문 써서 소수 판정 프로그램이 3번 4번은 구간 소수문제 어떻게 하라고? 제대로 못들엇음
# #연습문제 143페이지
# #6.5에서 1,2,3번 문제 해결
# #6.1
# l=[3,2,1,0]
# for i in l:
#     print(i)
# #6.2
# guess_me = 7
# number = 1
# while True:
#     if guess_me > number:
#         print('too low')
#     elif guess_me < number:
#         print("oops")
#         break
#     else:
#         print("found it!")
#     number += 1
# #6.3
# guess_me = 5
# for i in range(10):
#     if guess_me > number:
#         print('too low')
#     elif guess_me < number:
#         print("oops")
#     else:
#         print("found it!")
#     number += 1
#
#

########################################################
#개선한 버전
# numbers=input("Input first second number : ").split()
# n1=int(numbers[0])
# n2=int(numbers[1])
# if n1 > n2:
#     n1, n2 = n2, n1
# #파이썬은 이렇게 바로 가능 (packing, unpacking의 관계임)
# for number in range(n1, n2+1):
#     is_prime = True
#
#     if number < 2:
#         #print(f'{number} is not prime number')
#         pass #아무것도 하지 않는데 지나갈 때 사용하는 코드 continue는 위로 올라가는 것임
#     else :
#         i = 2
#         while i*i <= number:#계산량 줄이기 위한것
#         #소수일때 if문이 다 돈다는 문제점 발생
#             if number % i == 0:
#                 is_prime = False
#                 break
#             i = i + 1
#             #print(i, end=' ')#성능체크
#
#         if is_prime:
#             pass
#             print(number, end=' ')
#책에 있는 예제 205쪽 8.10까지
