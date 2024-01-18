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
print(isprime.__doc__) #help 처럼 이렇게 해도 똑같이 동작함 docstring이라고 부름 속성을 이용해서 이렇게 함수 설명 볼수있다.

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
        #map으로 대체 가능
        n1,n2=map(int,input("Input first second number: ").split())
        # numbers = input("Input first second number : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:
        #     n1, n2 = n2, n1
        #max,min함수로 바꾸기
        n1,n2=min(n1,n2), max(n1,n2)
        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ')
        print("\n")

    elif menu == '5':
        print("terminate program")
        break
    else :
        print("Invalid value")

# 받는게 매개변수? argument = 전달되는 실제값 그차이부터 제대로 확인해야할듯
# None은 True False와 다른 종류이다. None은 is 연산자를 사용한다.
# is 로 있는 건ㅛ지 없는건지 구분하는 용도로 사용 가능 is None 이런식으로 가능


#result는 초기화가 되는게 아니라 누적해서 저장함
def buggy(arg, result =[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')
#누적안하고 초기화가 하고싶으면 안에다가 빈 리스트 선언해주면 된다.
def buggy(arg):
    result = []
    result.append(arg)
    print(result)
buggy('a')
buggy('b')
# tuple로 한번에 담아 매개변수를 *로 tuple에 담아서 받는다?
# 가변인수처리가 없다.
# args는 맨뒤에 보내야 한다.
# 파이썬에선 포인터개념이 없다.
# 파이썬에는 오버로딩 개념이 아예 없다. 자바는 가능하다. *활용한 매개변수로 비슷한 효과를 낼 수 있다.
# *argument는 tuple에 담긴다. 즉 처리할떄도 튜플에 맞게 처리해야된다.
'''
# def a(n1, n2):
#     print(n1, n2)
def a(a , *n):
    print(a+n)
a(7)
a(a=7, 11)
'''
# **두개하면 키워드 argument로 dictionary로 바꿀 수 있다.
def print_kwargs(**kwargs): # *하나면 tuple에 두개면 dictionary에 담기게 된다.
    print(kwargs)
print_kwargs() #매개변수 받으면 dictionary로 출력 dictionary는 순서 없다.
# 함수 안에서 *의 의미는 start와 end가 named arugumet로 돼있어야돼 안하고 싶으면 인수로 받아야 한다는 의미
# defalut 매개변수의 의미를 말하는 듯 파이썬에헛 함수 (=)값을 집어 넣어주는 것..
# 디폴트 매개변수 하고 싶으면 *하고 =을 하면 됨
# 파이썬의 모든 것은 객체다
def run_something(func):
    func()
def answer():
    print(42)
run_something(answer)
#이런식으로 함수를 매개변수로 받아서 가능하다.
#함수와 뒤에 함수에 들어간 변수로 사용가능하다. 함수와 매개변수를 매개변수로 받을 수 있다.

def squares(*n):
    '''
    넘겨받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    #return n*n #tuple계산을 그냥 하지 못해 이거 수정해야 가변인수로 사용이 가능한 것
    return [ pow(i,2) for i in n]#list comprehension으로 사용이 가능함 tuple 개수 모르니까 range로 할게 아니라 그냥 시퀀스 있는 data니까 왼쪽 처럼 짜면됨

def run_function(f,*number)->list: #받아서 다시 리컨 하는거임 list로 리턴...? 제대로 이해다시 해야할듯
    return f(*number)


print(squares(7,5,2))
print(run_function(squares,9,10)) #f가 또 받아야 하는 거니까 9,10은 tuple로 받는게 아니라 수치로 받아야함
##############여기 매개변수 다시 보고 제대로 이해해야함
#함수 안에 함수도 가능함 Inner function
#closure 동적으로 다른 함수에 의해 생성이 되는 함수 #decorator에서 사용한다.
#안에서 바깥함수의 매개변수 받을 필요없이 직접적으로 가져와서 바로 쓴다. 자기 함수내에서 선언되지 않은 바깥의 변수를 가져와서 쓴다(신기..)
#inner2 함수이름을 호출하지 않고 반환한다.
#안쪽 함수의 메모리를 가지고 있는 것 knight2가 a랑 b는 주소를 가지고 있고 값을 홀드하는게 아니야...?
#무슨 의미인지 제대로 이해해봐야 할듯
def out_func(nout):
    def inner_func(nin):
        return nin*nin
    return inner_func(nout)

print(out_func(5))
#타입도 살펴보자 어떻게 되는지 함수만 찍혀
#외부함수를 호출함 ->nout이 받았음 ->안쪽 함수 받았음 -> 아쪽 함수 이름을 리턴 x가 받은 것은 inner function의 주소를 받음
#-> 바깥 변수에 자유롭게 접근하고 받았어 -> 9를 기억하고 있다...? 함수 메모리 번지가 찍혀 소괄호 ()이용해서 함수 실행시켜야된다.
#inner함수랑 똑같다.nout이9인걸 가지ㅗ 있어 언제 할지는 나중에 실행하면 되는거...? 어렵다 다ㅣㅅ 이해하기
#inner함수는 그냥 안에서 호출한것,, closure는 약간 달라 바깥의 변수를 참조할수있게 쓰고 호출식이 아니라 함수 이름만 던져주면 된다. 바깥함수에 값을 넣어주고  함수를 실행시키면 inner함수가 실행이도니다.(이떄 바깥함수가 받는 값 가지고 있음)
#C++에서는 함수 포인터로 받음

#list안의 값을 다 더하고 싶어
numbers=["7","-11","3"]
hap=0
for i in numbers:
    hap=hap+int(i)
print(hap)

print(sum(map(int,numbers)))# 이렇게 간단하게 map함수 활용 가능