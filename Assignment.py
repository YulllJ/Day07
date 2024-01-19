# 과제9.16 242 다
#9.1
# def good():
#     return ['Harry','Ron','Hermione']
# print(good())

def good() -> list:
    '''
    chapter 9 things to do 91
    :return: list
    '''
    harry_porter=input().split()
    return harry_porter
print(good())
#9.2
# def get_odds():
#     odd=0
#     for i in range(10) :
#         if i % 2 !=0 :
#             odd += 1 #python에서는 odd++로 못쓴다. odd += 1로 써준다.
#             if odd==3:
#                 yield i
# for x in get_odds():
#     print(x)
def get_odds(n) -> int:
    '''
    1부터 n까지의 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    '''
    for i in range(1, n+1,2):
        yield i
cnt=0
odds=get_odds(9)
for odd in odds:
    cnt=cnt+1
    if cnt ==3:
        print(f'Third number is {odd}')
        break
#9.3
# def test(f):
#     def inner():
#         print("start")
#         print(f())
#         print("end")
#     return inner #inner함수 꼭 반환 해줘야한다.
# @test #decorator가 inner함수의 기능 확장한거 확인 가능
# def good():
#     return ['Harry','Ron','Hermione']
#
# print(good())
# decorator 기존함수 수정 없이 기능 확장 개방폐쇄 원리
# Open Closed Principle
def test(f):
    '''
    decorator함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    '''
    def test_in (*args, **kwargs):#비워놔도 되지만 와도 동작하게끔 가변인수 넣자, 딕셔너리 하고 싶을때 생각해서 키워드가변인수도
        print("start")
        result=f(*args, **kwargs)
        print('end')
        return result
    return test_in
#@test#이거 달아주면 아래처럼 객체 안만들고 그냥 greeting 호출하기만 해도 확장할 수 있어
def greeting():
    print("안녕하세요~")

t=test(greeting)#이렇게 직접 객체 만들어주는 방식으로도 동작할 수 있다.
t()
#9.4
# 여기는 진도 나가고 나서 하기
short_list=[1,2,3]
position=5
try:
    short_list[position]
except:
    print("Caught an oops")