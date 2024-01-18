# set은 딕셔너리에서 키만 있는 것과 같다. 따라서 키는 유니크해야돼
# set은 값 꺼낼때(dict) 말고 존재여부 판정할때 사용하면 좋다, set= key container value까지 있는거 다루렴녀 dict로
# set은 기호로만 만들수 없어 empty set만드려면 set()으로만 가능
# set은 중복 제거, key만 존재함 set은 순서가 존재하지 않는다 섞여서 나와도 상관없어
# item은 키벨류 튜플 형태로 반환
# for name, contencts in drinks.items(): 에서 unpacking해서 값을 각각 받음
# 교집합에 & 쓴다. a.intersection(b)나 a & b로 쓴다.
# 합집합 | union
# 부분집합 subset은 <=  a.issubset(b); return type:boolean
# tuple은 없지만 set도 comprehension존재함(조건이 너무 많아서 길어져서 가독성 떨어지면 그냥 나눠서 쓰는게 낫다)
# 안변하는 set을 frozenset add로 추가불가(그냥 set은 가능했음):immutable
# is&*&$라고 이름 떠진 것은 boolean type이라는게 명확히 잘보인다.
# 객체지향설계 원칙 SOLID
# 그중 S..책임 = 기능 <단일 책임 원칙> 하나의 클래스, 하나의 함수는 맡은 바 하나만 잘하면 된다. 각각의 기능에 충실하게
def isprime(n) -> bool: #-> bool 안써도 되는데 어떤 타입으로 반환되는지 명시적으로 적어주는 것
    '''#3개 치면 주석구문 작성 가능
    매개변수로 넘겨 받은 수가 소수인지 여부 boolean으로 리턴
    :param n: 판정할 수 # """하면 함수 파라미터 어떤거인지 typing 가능하게 나옴"""
    :return: 소수면 True, 소수가 아니면 False
    '''
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
    return True

help(isprime)#우리가 작성한 함수에 대한 설명이 나옴 #help는 작성법같은거 알려줘 빌트인 함수들도 다 설명해줌


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
        print("\n")

    elif menu == '5':
        print("terminate program")
        break
    else :
        print("Invalid value")


