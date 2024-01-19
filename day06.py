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
#