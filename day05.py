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
# defalut 매개변수의 의미를 말하는 듯 파이썬에서 함수 (=)값을 집어 넣어주는 것..
# 디폴트 매개변수 하고 싶으면 *하고 =을 하면 됨
# 파이썬의 모든 것은 객체다
def run_something(func):
    func()
def answer():
    print(42)
run_something(answer)
# 이런식으로 함수를 매개변수로 받아서 가능하다.
# 함수와 뒤에 함수에 들어간 변수로 사용가능하다. 함수와 매개변수를 매개변수로 받을 수 있다.

def squares(*n):
    '''
    넘겨받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    #return n*n #tuple계산을 그냥 하지 못해 이거 수정해야 가변인수로 사용이 가능한 것
    return [pow(i,2) for i in n]#list comprehension으로 사용이 가능함 tuple 개수 모르니까 range로 할게 아니라 그냥 시퀀스 있는 data니까 왼쪽 처럼 짜면됨

def run_function(f,*number)->list:
    return f(*number)
#안에 f가 list로 반환하니까 얘도 list로 반환하는 것

print(squares(7,5,2))
print(run_function(squares,9,10))
#number니까 튜플로 받음
#f가 또 받아야 하는 거니까 9,10은 tuple로 받는게 아니라 수치로 받아야함

# 함수 안에 함수도 가능함 Inner function
# closure 동적으로 다른 함수에 의해 생성이 되는 함수 #decorator에서 사용한다.
# 안에서 바깥함수의 매개변수 받을 필요없이 직접적으로 가져와서 바로 쓴다. 자기 함수내에서 선언되지 않은 바깥의 변수를 가져와서 쓴다(신기..)
# inner2 함수이름을 호출하지 않고 반환한다. inner2함수의 복사본을 동적으로 생성해서 반환하는것
# 안쪽 함수의 메모리를 가지고 있는 것 knight2가 a랑 b는 주소를 가지고 있고 값을 홀드하는게 아니야 반환값 자체가 함수..
# a랑 b를 실행하면 그때 결과가 나옴
def out_func(nout):
    def inner_func(nin):
        return nin*nin
    return inner_func(nout)
print(out_func(5))
# 타입도 살펴보자 어떻게 되는지 함수만 찍혀
# 외부함수를 호출함 ->nout이 받았음 ->안쪽 함수 받았음 -> 아쪽 함수 이름을 리턴 x가 받은 것은 inner function의 주소를 받음
# -> 바깥 변수에 자유롭게 접근하고 받았어 -> 9를 기억하고 있다 함수 메모리 번지가 찍혀 소괄호 ()이용해서 함수 실행시켜야된다.
# inner함수랑 비슷.nout이9인걸 가지고 있어 언제 할지는 나중에 실행하면 그떄 값을 반환하게 되는 것
# inner함수는 그냥 안에서 호출한것, closure는 약간 달라 바깥의 변수를 참조할수있게 쓰고 호출식이 아니라 함수 이름만 던져주면 된다. 바깥함수에 값을 넣어주고 함수를 실행시키면 inner함수가 실행이된다.(이떄 바깥함수가 받는 값 가지고 있음)
# C++에서는 함수 포인터로 받음

# list안의 값을 다 더하고 싶어
numbers=["7","-11","3"]
hap=0
for i in numbers:
    hap=hap+int(i)
print(hap)

print(sum(map(int,numbers)))# 이렇게 간단하게 map함수 활용 가능

def squares(n):
    return n * n
even_numbers=[i for i in range(51) if i % 2 ==0]
print(even_numbers)
print(tuple(map(squares, even_numbers)))
print(tuple(map(lambda x:x**2, even_numbers))) #lambda로 같이 구현할 수 있어 이름 없는 함수 익명함수 람다함수
# 간단한 함수는 선언하지 말고 람다함수로 그때그때 쓰고 버리자
# generator 시퀀스를 생성하는 객체; 메모리에 생성 정렬 안하고 아주 큰 시퀀스를 순회한다.(range도 generator임)
# generator는 순회할때 마지막으로 불린거 기억하고 그 다음 값을 반환함(그러니까 1부터 10까지 차례대로 만들어지는게 가능한거임)
# 이전 호출 메모리에 저장이 안돼 항상 똑같은 상태로 첫번째 줄부터 동작하는 것
# 우리의 range함수를 직접 만들어보자
# 아래 함수 괄호 안 키워드 매개변수, 디폴트 매개변수임
def my_range(first=0, last =10 ,step=1):#숫자는 만들어서 보내주는데 기억은 하지 않는다. 0을 하고 그다음 스텝으로 가면 0을 보내줬지만 그 값을 기억하지는 않는다.
    number=first
    while number<last:
        yield number# generator에서는 값을 return이 아니라 yield로 값을 반환한다.
        number += step
print(my_range(1,5))
#generator는 객체를 순회한다. 이떄 한번만 순회하고 해당 값을 증석애서 생성해서 보내기때문에 다시 시작하거나 되돌리지 않는다.
r=my_range()
print(r, type(r))
for x in r:
    print(x)# 출력다됨
for x in r:
    print(x)# 여기서 출력안됨 다시 쓰고 싶으면 다시 만들어줘야한다.
    # 한번 꺼내쓰면 다시 써야돼 다시 돌아와야돼
    # 두번쨰 출력할떄 안나와 다시 generator객체 만들어야돼
# 확장에는 열려있고, 수정에는 닫혀있다  개방폐쇄 원칙
# 코드를 바꾸지 않고 수정하고 싶을떄 사용하는게 decorator
# closure안에서 뭐 쓰고 있지,,,데커레이터 이해하기 위해서는 이거 잘 이해해야 가능하다.
# 수정에는 닫혀있따,, 잘만들어진 것을 굳이 고치지않는다.
# closure는 값을 기억해두니까...
# @해서 decoration함수 적어 이때 이 함수는 closure로 만들어져야한다.
# 원래 함수는 똑같이 동작하는데 거기에 옷을 입힌것 pow가 붙어서 나왔어 그러면 걷어내먄된다. @#ㄱ3 annotation지우고...
# 새로운 함수 만들바엔 description하는게 훨씬잘보이고 간단하다.
# 기존 안건들고 바꿀수 있는 방법임!
#데코레이터(@decorator)를 사용하면 데코레이터 함수의 내부(inner) 함수가 원래 함수에 대한 기능을 확장하거나 수정하는데 사용됨
# 데코레이터는 기존 함수를 취해서 새로운 함수를 반환하는 함수이므로, 데코레이터가 적용된 함수를 호출하면 데코레이터 함수의 내부 함수가 실행된다.
# 즉, @description이라고 적은 함수인 power안에 description함수의 inner함수가 들어가있는 것 처럼 확장이 되는 것이다.
def description(f):  # closure
    def inner(*args):
        print(f.__name__)#함수 이름 print
        print(f.__doc__)#함수 설명 print
        r = f(*args)
        return r

    return inner


def squares(n):
    """
    제곱 함수
    """
    return n * n

@description
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result


f1 = description(squares)
print(f1(9))#원래 함수 출력
print(power(2, 10))#power는 description inner함수 기능 없었는데 @해줘서 기능이 확장된 것!
