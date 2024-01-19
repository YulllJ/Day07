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


