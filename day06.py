# decorator밑에 설명한 부분 다시 이해하기
# wombat학 fruitbat위치 달라 클로벌인 웜팻은 바뀌지 않았다 로컬만 바뀜?
# 전역변수 참조해서 사용하고 싶을때는 global이라는 예약어 사용함
# 왜 전역변수는 남발하면 안될까 왜 써야할까? 프로그램 종료시킬떄까지 메모리에 계속 차지하고 있어(local은 pop돼서 사라짐)
# 공유해야할 자원들이 있으니까 자주 공유하는 것들은 전역변수로 만들어놓고 짠다.
# locals는 딕셔너리 형태로 로컬에서의 네임스페이스 반환함
# 우리나라에서는 _ 를 언더바라고 읽는데 영어로는 under score임
# main은 underscore두개에 할당돼 있다.
# 최대 recursion 깊이 초과했다. 불필요한 자기 호출이 계속되면 파이썬이 막음
def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 factorial 함수
    :param n: 정수
    :return:  정수
    '''
    result = 1
    for i in range(2, n+1): # n+1까지라고 작성돼있어야 n까지 계산됨
        result= result*i
    return result
print(factorial_repetition(int(input("number : "))))
# 재귀함수는 복제하는게 아니라 자가복제하여 사용함
# 재귀함수 버전
def factorial_recursion(n):
    if n ==1:
        return n
    else:
        return n * factorial_recursion(n-1) # 자기와 같은 함수 부르기
    '''
    재귀함수 이용한 팩토리얼 함수
    :param n: 정수,  int
    :return: fuunction, int
    '''
number=int(input("number: "))
print(factorial_recursion(number))
print(factorial_repetition(number))
print(globals())
# cpu안에서 accumulator에서 가져오면 금방됨 but 재귀함수는 호출때문에 시간이 너무 오래 걸림 이를 해결하기 위한 방법을 알고리즘 수업시간에 배움
# 동기화의 장점 :  단점 : 느려져  비동기의 장점 : 빨라 단점 : 가장 늦게끝나는 사람을 기준으로 완료돼?
# index는 못찾으면 예외를 던짐
# try안에 예외 발생할 가능성이 있는 코드들을 넣어주고 except로 처리해주는 방식



import random
class OopsException(Exception):
    pass

numbers= list()
# for i in range(1,5):
#     numbers.append(random.randint(1,100)) # 정수형 난수 발생기
numbers=[random.randint(1,100)for i in range(10)] # 이렇게 잘성할수도 있어 알아둬야
try: #예외발생여지 있으면 넣어주자
    pick=int(input(f"Input index (0~{len(numbers)-1}):")) #가변적으로 길이 되게 len으로 해주는게 제일 좋아
    print(numbers[pick])
    print(5/0) #이 오류도 exception으로 흘려가버려 어떤 에러인지 다시 확인해서 except해준다.
    raise OopsException("Oops~~")#raise는 강제로 만들어 던지는 것

except IndexError as err:#err은 시스템이 던져준 에러 메시지 받아서 저장하는것 err출력하면가능 변수 이름 err로 안해도 돼 아무 변수로 시스템이 던져준 에러메시지 as로 받을수 있는 것
    #이렇게 구체적으로 적으면 에러 종류에 맞게 except로 흘러가게됨
    #pick하려는 index에서 발생하는 것
    print(f"Out of range: Wrong index number\n {err}") #이런식으로 깔끔하게 나오도록 예외처리 해주는 것 뭐가 문제인지 알려주는 식으로.. but 인덱스 에러가 아닌것도 잡아버려 string입력해도 발생한 에러는 except가 뜨는거임
except ValueError as err:#어떤 에러인지 정확하게 써주면 된다.
    print(f"Input Only Number~\n {err}")#integer함수가 변환하는 과정에서 발생하는 value error
except ZeroDivisionError as err:
    print(f'The denominator cannot be 0. \n {err}')
# except OopsException as err:
#     print(f"Oops Oops{err}")
except Exception:# 위에 종류 아닌것들은 여기로..
    print("Error occurs") # 얘는 제일 아래에 와야한다. 위에 있으면 인덱스에러도 여기에 해당돼서 동작 제대로 안하게됨
    # 강제로만든 Oops error도 얘가 받음 위에 주석처리한 부분 처럼 Oops에 대한 예외처리도 만들어서 가능하다.
else:
    print(f"programming terminate")
