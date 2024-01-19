# 상속
# class들 간의 관계: assocition(연관관계) has-a 관계 클래스안에 다른 클래스의 ???
# depandency(의존관계) use-a 관계 가져다가 쓰는.. 클래스 안 클래스가 아니라 별도의 클래스인데 다른 클래스의 객체를 사용할떄
# Inheritance(상속관계) is-a 관계
# 리스코프(Liscov) 치환법칙: SOLID에서 L에 해당하는 원칙 상위클래스(부모클래스)의 객체가 들어가는 자리에는 자식 클래스의 객체가 100% 호환이 된다.
class Pokemon:
    def __init__(self,name):
        self.name=name
    def attack(self,target):
        print(f"{self.name}이(가) {target.name} 을(를) 공격")
class Pikachu(Pokemon): # is-a 관계가 됨
    def __init__(self,name,type):
        super().__init__(name)# 부모의 init 호출시켜서함 super로 부모님거 가져와서 사용하게 됨
        self.type=type
    def attack(self, target):
        print(f"{self.name}이(가) {target.name} 을(를) {self.type}공격") # 오버라이드된 것
class Squirtle(Pokemon):
    pass
class Agumon:
    pass

p1=Pikachu("피카츄","전기")
p2=Pokemon("Agumon")
p1.attack(p2)
# is로 시작하는 함수 이름은 boolean type
# override method 대체하는 것
# 다중상속: 부모 클래스가 두개 이상인 경우

# 같은 계층이면..? 다중상속한 순서대로
#__mro__ 우선순위 보여준다.
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):#B,C,A순으로 우선순위
    pass

# D의 MRO 확인
print(D.__mro__)
#Super()은 부모 메서드 사용하고 싶을떄 사용하는 함수 C++에서는 그냥 사용하면 되지만 파이썬에서는 Super로 사용함
class FlyingMixin:
    def fly(self):
        return f"{self.name} 이(가) 하늘을 훨훨 날아갑니다~"
class SwimmingMixin:
    def swim(self):
        return f"{self.name} 이(가) 수영을 합니다~"
class Pokemon:
    def __init__(self,name):
        self.name=name
    def attack(self):
        print("공격!")
class Charizard(Pokemon,FlyingMixin):
    pass
class Gyarados(Pokemon,SwimmingMixin):
    pass

g1=Gyarados("갸라도스")
c1=Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# c1.attack()
#Charizard.attack()#이거는 에러가 남
Charizard.attack(c1)# 이렇게 쓰면 누가 공격주체인지 self에 값을 넘겨줘야 가능 리자몽인 c1을 넣어주면 된다.

#hidden_name으로 private하게 가능

print(g1.name)
g1.name="잉어킹"
print(g1.name) #외부에서 접근해서 바꿀 수 있어 좋지 않아 private하게 설정 바꿈
