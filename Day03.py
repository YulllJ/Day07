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
print(alphabet[:-3])
print(alphabet[-3:])
print(alphabet[18:-3])#18번부터 뒤에서 3개 이전까지 꺼내기
print(alphabet[18])
print(alphabet[::-1])#역방향으로 꺼내기
#split 문자열 분리 후에 list로 담아주는 함수


