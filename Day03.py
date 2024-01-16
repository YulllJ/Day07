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