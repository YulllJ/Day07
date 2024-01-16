#원시 문자열 Raw r'으로 하면 \문자열 무시됨
# print('university')
# number1=int(input("number1 ;"))
# number2=int(input("number2 ;"))
# print('university' * number1)
#immutable이라 할당은 안됨 but replace함수로 가능함
#사본만들어서도 가능
#할당대신 slicing 1번방부터 끝까지 등으로 해결가능함
name="Henry"
print("p"+ name[1:])
#end-1까지 가져오는거 유의
univ="Inha\tuniversity"
#인하 가져올거면 처음부터 3번방까지이므로 end-1을 가져오기때문에 4까지로 설정해줘야 한다.
print(univ[:4])
#university까지 가져오고 싶으면
print(univ[5:15])
print(univ[::3])#마지막은 증가개수
alphabet='abcdefghijklmnopqrstuvwxyz'
print(alphabet[:-3])#뒤에서 3개전까지 꺼내기
print(alphabet[-3:])#뒤 3개만 꺼내기 역방향 인덱스
print(alphabet[-3:-1])
print(alphabet[18:-3])#18번부터 뒤에서 3개 이전까지 꺼내기
print(alphabet[18])
print(alphabet[::-1])#역방향으로 꺼내기
#split 문자열 분리 후에 list로 담아주는 함수
#split전에 인풋으로 받은거는 string그 이후에 split하고 담기는 것은 list형식 list형식에 담기는거 잘알아야

course='2024 KEB BootCamp'
print(course.split('B'))
# numbers1, numbers2 =input("First Number Second Number:").split()
# print(numbers1)
# print(numbers2)
# number =input("First Number Second Number:").split()
# print((number[0])+(number[1]))#concatenation
# print(int(number[0])+int(number[1]))#arithmetic
#csv comma separate value
subjects=['python', 'database','data structure']
print(','.join(subjects))
print(course.replace('KEB','INha'))
#old, new는 replace치면 자동생성 되는거 그냥 replace에 인수 두개 넣어주면 된다.
#strip시 ".!#*"없앨때 연속으로 있는 양쪽 끝의 애들만 제거됨
_course=course+'#****!...'
print(_course)
print(_course.strip('#*!.'))
#rfind는 reverse find 뒤부터 찾아서 인덱스를 반환
#없으면 return값이-1 find는 있으면 인덱스를 반환한다
# 인덱스 함수 index()로 처리하려구 하면 인덱스는 -1을 리턴하지 않으니까 예외처리 필요
#if 0돼도 문제가 발생함 false처럼 처리됨
#
# subjects="python c++ database linux"
# subjects=input("수강신청 과목 입력: ").split()
# try:
#     print(f'해당과목이 존재합니다. 위치는 {subjects.index(subjects)}번 인덱스입니다.')
# except ValueError:
#     print("해당과목이 존재하지 않습니다.")
#
#     #이거 수정해야됨 코드 이상 어떤식으로 예외처리한다는건지 다시 이해하기
#인덱스는 찾는게 없으면 예외를 발생시킨다.
# subjects = "python c++ database linux"
# user_input = input("수강신청 과목 입력: ")
#
# # Split the subjects string into a list of individual subjects
# subject_list = subjects.split()
#
# try:
#     index = subject_list.index(user_input)
#     print(f'해당 과목이 존재합니다. 위치는 {index}번 인덱스입니다.')
# except ValueError:
#     print("해당 과목이 존재하지 않습니다.")
# print('%s' % 42)
# print('%x' % 42)
# print('%d' % 42)
# print('%o' % 42) #오른쪽에 있는 수를 왼쪽의 형식에 맞게 print
# print('%s' % 7.03)
# print('%f' % 7.03)
# print('%e' % 7.03)
# print('%g' % 7.03) #오른쪽에 있는 수를 왼쪽의 형식에 맞게 print
# actor='Richard Geer'
# cat='chester'
# weight=28
# print(type(weight))
# print("our cat %s weight %s pounds" %(cat, weight))
#정렬시 - 붙으면 오른쪾 기준으로 왼쪽으로 이동하게 돼(old style)
#dictionary의 key value로 풀수있다.
subjects={'python':'kim', 'C++':"Sung", 'data structure':'kim', 'data base':'kang'}
print("{0[python]} {0[data structure]}".format(subjects))
#dictionary형 key가 들어가서 value가 나옴
#빈공간을 문자로 채워서 정렬도 가능
#자료구조에서 반복문 조건문을 잘써야된다.
#continue는 위로 다시 올라가는것
# while True:
#     value = input ("Integer, please [q to quit]; ")
#     if value =='q':
#         break
#     number=int(value)
#     if number % 2==0:
#         continue#짝수의 경우 continue를 만나서 위로 올라감
#     print(number, "squared is ", number*number)
# #홀수만 제곱돼서 출력됨
# number = int(input("input number: "))
# is_prime = True #int를 bool로
# #cnt = 0
# i = 2
# while i < number:
#     if number % i == 0:
#         #cnt = cnt + 1
#         is_prime = False  #remove count
#         break#약수가 발생하는 시점에서 탈출해야 그 뒤는 돌 필요 없으니까
#     i = i + 1
#     print(i, 'end')# break 유무 확인해보자 break로 프로그램이 쓸데없이 돌아가는 횟수 훨씬 줄임
# #if cnt == 0:
# if is_prime :    #bool이라 비교없이 바로 가능
#     print(f'{number} is prime number')
# else:
#     print(f'{number} is not prime number')
#     #이후 버전은 그냥 교수님거 봐도 될듯,,
univ='Inha'
i=0
while i <len(univ):
    print(univ[i],end=' ')
    i = i + 1
print()
#python에서는 아래와 같이 iterator를 사용하여 간단하게 간으 여러 자료구조에서 사용가능하다는 장점이 있다.
for letter in univ:
    print(letter, end=' ')

#range라고 하는 generator로 구간도 설정할 수 있다.
for k in range(0, len(univ),1):
    print(univ[k], end =' ')

for k in range(len(univ)): #이렇게 써도 됨 다 default로 설정돼있어서 짧게 쓸수 있어
    print(univ[k], end =' ')
#상세하게 설정이 필요할때 범위 구체적으로 지정해주면 된다.
#iterator로 사용하면 side effect없이 가능하다.
#코드에 변화가 발생하는 거싱 side effect?
#while문으로 했을때 길던게 for로 하면 훨씬 짧아진다.
print('\n')
for x in range(0, 3):
    print(x)
#(0,3)으로 적어두면 범위는 0에서 2까지가 출력된다.
#range자체는 ganerator(숫자만 발생시키지 기억을 못함)의 역할을 하는 것 그냥 print하면 안되기 떄문에 list에 담아서 출력해야한다.
print(list(range(0, 3)))
print(tuple(range(0, 3)))
print((range(0, 3)))


#역순으로 출력하는 방법도 range 설정해서 가능함
#숫자 두개 입력해서 50과 100 사이에서 소수가 출력되는 함수를 만들어라
#innput두개 따로 받거나 split하거나 해서 받아오면됨 21 10 입력받아도 10 21 입력 받아도 그사이의 출력 값을 하자


