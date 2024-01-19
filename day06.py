# java는 객체지향언어 but 완전한 객체지향언어는 아니다.
class Pokemon: #괄호 안써도 됨
    def __init__(self, name):#self는 기본적으로 들어가는 자동으로 들어간다. (C++에서 this)와 같아
        self.name=name
        print(f"{name} 포켓몬스터 생성")
        print("포켓몬스터 생성")
        #init은 객체마다 딱 한번만 생성됨

    #pass
    def attack(self,target):
        print(f"{self.name}이(가) {target.name} 을(를) 공격!")
pikachu=Pokemon("피카츄")
squirtle=Pokemon("꼬부기")
charizard=Pokemon("리자몽")
charizard.attack(squirtle)
#pikachu.name=
pikachu.nemesis=squirtle
#squirtle.name=
pikachu.nemesis.name="꼬부기"
print(pikachu.nemesis.name)
print(squirtle.name)
# 개별객체 다른 객체인것


# method는 class와 object의 함수를 method라고 불러 C++에서 멤버함수와 같은 개념 자바에서는 다 클래스 안에있어 함수랑 같은개념..
# self는 예약어는 아니지만 일반적으로 사용 이런건 다 self라고 쓰자 실행시점의 객체 메모리를 가지고 있는 변수를 self라고 부름(c++의 this라는 의미)
# __init__은 생성자는 아니야 객체는 이미 만들어졌고 그것을 초기화하기 위한 메서드
# 자바는 모든 것을 힙에 저장. new로 해서..?
# 상속
# class들 간의 관계: assocition(연관관계) has a 관계 클래스안에 다른 클래스의 ???
# depandency(의존관계) use a 관계? 가져다가 쓰는.. 클래스 안 클래스가 아니라 별도의 클래스인데 다른 클래스의 객체를 사용할떄
# Inheritance(상속관계) is a 관계?
# 리스코프(Liscov) 치환법칙: SOLID에서 L에 해당하는 원칙 상위클래스(부모클래스)의 객체가 들어가는 자리에는 자식 클래스의 객체가 100% 호환이 된다.

