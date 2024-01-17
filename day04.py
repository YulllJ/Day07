
#empty tuple은 ,없어도 tuple가능하다.
t0 = ()#boolean에서 empty는 false로 처리됨
print(type(t0), type(tuple()))
t1 = (5)
t2 = 5,
t3 = (5,)
t4 = (5, 7)
t5 = 5, 7
print(type(t1),type(t2),type(t3),type(t4),type(t5)) #괄호는 option tuple은 꼭 ,가 있어야 한다.
t6= "python", "kim" #packing
print(type(t6),t6[1])#소괄호는 함수 호출시에 []는 원소 꺼낼떄
subjects, prof = t6 #unpacking 시퀀스를 가진 자료형이라 가능한 것
print(prof)
print(type(subjects)) #unpacking해서 string형이 됨
#unpacking시 개수가 맞아야한다. value error발생
#swap대신 packing unpacking 동시에


#빈 ()도 아니고 ,도 없어 tuple이 아니라 그냥 string이 됨
marx_tuple = ("groucho")
print(type(marx_tuple))# string


print(type("groucho",))# 그냥 string에 , 찍은걸로 인식함 덩어리의 연속으로 받아들임
print(type(("groucho",)))# ,까지 한덩어리여야 tuple형이 되는 것
#다른 자료구조를 tuple로 형변환시킬때 사용함

t9 = 1, 2, 3
t10 = 1, 2
print(type(t9))
print(t9 <= t10)
t10 = 1, 21
print(t9 <= t10)
#tuple간 비교연산이 가능하다 원소 개수가 아닌 원소끼리 차례대로 계산해내는 것
#tuple,list는 sequence가 존재하는 자료형 iteration으로 꺼낼 수 있어
words= ('fresh')
#튜플은 immutable임, t1+=t2를 하면 값이 바뀌는게 아니라 새로운 id를 만들어서 집어넣는것
t1 ='say', 'ery', 'fdsf', 'fdf'
t2 = 'fdf', 'fdsf'
t1 += t2
print(t1)
#머신러닝에서는 list대신해서 numpy배열로 대체됨
l=[200,'fd',()]#list는 배열과 다르게 다른 타입도 담을 수 있다.
#tuple은 원래 못바꿔 list로 바꿔서 바꿀수 있도록 한다음에 다시 tuple로 해서 바꿀수 있어 ( 참조 이름만 같을뿐 새로 만들어진거라 원본과 다름, 메모리 위치가 달라지게 된다.)
#split은 list로 바꿔준다. 역방향 인덱싱도 가능함. [0:2]0에서 시작해서 2번 앞에 까지
