#reverse는 자체적으로 값을 바꿈 인덱싱으로 하면 재할당을 해줘야한다.
subjects=["C++","Java","Python", "Java"]
print(subjects[::-1])
print(subjects)#index쓰면 원본이 변하지는 않아.
subjects.reverse()
print(subjects)
#insert는 집어넣는 것, *는 반복시에도 사용이 가능하다
#append는 통째로 리스트 안에 리스트 형식으로 들어가져버려 더하기 하면 그냥 이어붙인것처럼
#list는 어떤 타입이든 담을수있따. list를 list에 담는 것도 가능하다.

# index slicing
# list slicing에서 집어넣을때, tuple string다 원소별로 리스트에 들어가게 돼
# 지우는건 del, remove, pop으로 가능하다
# subjects.remove("Java")
# print(subjects)
# del subjects[-2]
# print(subjects)
# subjects.pop()#안에 아무것도 없으면 뒤를 지움 pop(0)은 앞을 지움 지우고 싶은 인덱스 pop안에 넣음
# pop성능은 뒤를 지우는 .pop()일때가 성능이 좋아 성능에 맞게 지우면됨
# print(subjects)#python에는 배열이 존재하지 않아 그에 따른 오버헤드가 존재함
# .clear해서 리스트 통으로 지울수있어
# 배열 인덱스 반환하는 함수는 find, index find는 -1을 던지고 index는 invalid value?를 내뱉음 기억하고 있어야..
# list를 문자열로 바꿀떄 사용하는게 join ','.join(list)
# sort는 원본을 바꿔, sorted는 원본은 그대로 두고 사본을 만들게 되는 것
sorted_subjects= sorted(subjects)
print(subjects)
subjects.sort(reverse=True) # 기본값은 false인데 true로 해서 정렬가능해짐
print(subjects) # 정렬시 타입 같아야한다. 숫자랑 string이랑 같이 못해 숫자 str으로 바꾸게 되면 가능 한글 숫자 영어 정렬 우선순위 존재함
# 숫자 알파벳 한글순으로 우선순위가 있음
# shallow copy를 하면 type이 바뀌게 돼 immutable mutable?
import copy
subjects = ['a', ['b', 'c'], 'd']
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)#deepcopy한 e만 바뀌지 않아 나머지는 그냥 a를 참조하기 때문에 a가 바뀌면 바뀐다.
print(subjects)
subjects[1][1]='x'
print(a,b,c,d,e)
# 파이썬 deepcopy shallow copy 완벽하게 이해하고 있어야
# startwith, endswith return type은 boolean임
# zip은 제일 작은 애 기준으로 한번에 돌릴수 있다?
# zip으로 list묶어 같이 보낼주잇따.? dictionary형태면 키 밸류 형태로 가능해져
#요소가 3 3 3 4면 가장 짧은 시퀀스인 3에 맞춰서 묶이기 때문에 4번째는 묶이지 않고 종료된다. zip으로 한번에 출력이 가능하다.
#다른 묶음들을 하나씩 꺼내서 묶는 느낌
# list comprehension=list 축약
# append안쓰고 만드는법
squares=list()
for i in range(1,6,1):
    squares.append(i*i)
print(squares)
print(id(squares))
# list comprehension
squares=[i*i for i in range(1,6,1)]#이렇게 줄여서 쓰기 가능함
print(squares)
print(id(squares))#새로 넣어주는게 아니라 새로 할당하게 되는것 다른 id가지고 있어
even_squares=[i*i for i in range(1,6) if i % 2 == 0]
print(even_squares)
# 왜 tuple을 다 list로 바꾸지 않을까?
# tuple은 메모리 적게 차지함 ,side effect 안발생함 tuple을 dictionary key로 사용이 가능하다. key는 immutable한 타입만 사용이 가능하다.
# immutable은 comprehension 사용못함
# dictionary는 순서 없어, key value만 있을 뿐
# C++에서 map은 pair라고 하는 struct를 사용함
# tuple안에 list가 존재한다.
#dictionary는 이미 값으 존재함 mutable value 오버라이딩 가능함
#get 찾지못했을때의 값을 적을수도 있어
sugang = dict(python="kim", cpp='sung', db='kang' )
print(sugang)
sugang['data structure']='kim'#이런식으로 add가능함
sugang['data structure']='park'#update도 가능함
print(sugang)
print(sugang['db'])
print(sugang.get('db'))
print(sugang.get('opensource'))
print(sugang.get('opensource','not exist'))#없으면 우측에 넣어준 값이 출력
#dictionary전용 함수도 존재함 keys는 key값들만 꺼내줌 value는 value값만 꺼내줌 items는 pair로 값을 꺼내줌
for subject, professor in sugang.items():#dictionary는 순서 안정해져있음 순서 다르게 나와도 틀린건 아냐
    print(f'{subject}과목 담당 교수는 {professor}입니다.')
for k in sugang.keys():
    print(k)
for k in sugang:
    print(k)#sugang.keys가 디폴트라 안써줘도 제대로 출력되는 것
for v in sugang.values():
    print(v)
for s in sugang.items():
    print(s)


################################################
import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}
# drink=input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods)
#del drinks_foods["위스키"]
japan_drinks_foods = {"사케": '광어회', '고량주': "꿔바로우"}#위에서 del로 위스키 안지우면 4번쨰 위치에 위치한 사케는 안보일뿐 실제로는 이어붙어진것 #키가 동일한 것은 새로 덮어씌워짐
drinks_foods.update(japan_drinks_foods)
print(drinks_foods)
drinks_foods_keys = list(drinks_foods)
# print(drinks_foods_keys)
# import는 남이 만든거 가져옴
# print(random.choice(drinks_foods_keys))#시퀀스 데이터이기만 하면돼 타입 크게 상관 없
random_drink = random.choice(drinks_foods_keys)
while True:
    menu = input(
        f'다음 술 중에 고르세요\n 1) {drinks_foods_keys[0]}, 2) {drinks_foods_keys[1]}, 3) {drinks_foods_keys[2]}, 4) {drinks_foods_keys[3]}, 5) 아무거나  6) 종료:')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
    elif menu == '5':
        # pass#에러 안나게
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')  # random_drink는 list형이라{}사용해서 쓸피룡 없어

    else:
        print(f'다음에 또 오세요')
        break
# key는 중복이 안돼 dictionary합칠때 겹치게 써야
# a=b하면 a는 copy가 아니라 참조를 하는 것 slicing 하고 이런저런 함수쓸때 문제가 발생함
# immutable mutable에서 list안에 list안으로 문제가 발생하게 된다.
# 즉, shallow copy, deep copy문제가 발생하게됨 여기가 중요하니까 다시 제대로 이해할 것
# mutable은 공용..?shallow copy하고있던 애들 다 바뀌게 돼 참조하고 있던 애들 다 바뀜
# 별도의 공간에 생긴것으로 만들고 싶으면 deepcopy를 해야한다.
# pop은 삭제하고 리턴함
# remove와 pop의 차이를 제대로 이해하자
# deepcopy한거는 안바뀌어, shallow copy는 바뀌어
# set은 dictionary와 비슷함 하나씩만 존재한다?

# tuple은 comprehension없어 dictionary랑 list만 존재한다
# 예약어 키워드 띄어쓰기 특수기호 있는 문자로 dict로 불가능하다.
# key값은 immutable한 값만 가능하다.
