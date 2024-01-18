# 과제9.16 242 다
#9.1
def good():
    return ['Harry','Ron','Hermione']
print(good())
#9.2
def get_odds():
    odd=0
    for i in range(10) :
        if i % 2 !=0 :
            odd += 1 #python에서는 odd++로 못쓴다. odd += 1로 써준다.
            if odd==3:
                yield i
for x in get_odds():
    print(x)
#9.3
def test(f):
    def inner():
        print("start")
        print(f())
        print("end")
    return inner #inner함수 꼭 반환 해줘야한다.
@test
def good():
    return ['Harry','Ron','Hermione']
print(good())
#9.4
short_list=[1,2,3]
position=5
try:
    short_list[position]
except:
    print("Caught an oops")