# def main():
#     print(5)
#
# if __name__ =="__main__":
#     main()
#
# subjects=['python', 'linux','data structure','database']
# print(subjects)
# subjects[3]='C++'
# print(subjects)
# a_=5
# print(a_)
#
# first_number = int(input("first no:"))
# second_number = int(input("second no:"))
#
# # divmod 함수의 결과를 변수에 저장
# quotient, remainder = divmod(first_number, second_number)
#
# # f-string을 사용하여 문자열 생성
# result_string = f'몫은 {quotient} 나머지는 {remainder}'
#
# # 결과 출력
# print(result_string)
# #따로 받는 경우와 튜플로 한번에 받는 경우 모두 가능하다
#
# first_number = int(input("first no:"))
# second_number = int(input("second no:"))
#
# # divmod 함수의 결과를 튜플로 받아 직접 사용
# result_string = f'몫은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}'
#
# # 결과 출력
# print(result_string)

#
# dec=65
# octal=0o101
# hexadecimal=0x41
# binary=0b01000001
# print(binary)
# print(chr(octal))
# sub=dec-octal
# print(sub)
# print(ord('B'))#대문자 알파벳은 65에서 시작
# #소문자 알파벳은 97에서 시작
# #숫자는 48에서 시작


# temp=[]  #비어있어야 false로 취급함
# if temp:
#     print("원소 존재")
# else :
#     print("비어있는 리스트")
#
#
# temp=[0]
# if temp:
#     print("원소 존재")
# else :
#     print("비어있는 리스트")
#
#
# #vowels='aeiou'
# vowels={'a','e','i','o','u'}
# letter=input("alphabet letter: ")
# print(type(letter))
# if letter in vowels :
#     print(letter,'is a vowel')
# else:
#     print(f'{letter} is a conconant!')
# #중괄호: set , 대괄호:list, 소괄호: tuple, 중괄호 & 키 밸류: dictionary
l=[1,3,3,2,4] #list
s={1,3,3,2,4} #set
print(l, s) #list는 그대로 출력, set은 원소 하나씩만나오고 정렬됨
#둘다 mutable한 자료형이라 안에 원소 바꾸기 가능함
print(type(l), type(s))