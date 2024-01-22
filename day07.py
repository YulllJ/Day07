#클래스도 클래스 자체의 속성을 가진다 대문자로 시작하는 걸로 출력이 가능하다 클래스에 속성 할당 가능하고 이는 상속하고 이를 자식 객체에게 할당한다.자식객체가 변한다고 해서 클래스가 변하진 않는다
#클래스 전체에 적용돼서 클래스로매서드로
#Static method 인수없이 사용 가능한 정적인수-객체 생성안해도 돼
#자식클래스에서 init하면 알아서 오버라이드 되는 것
#속성은 상속이 돼 객체가 안돼
#해당함수 안쪽에서 객체를 받아서 출력하는 것을 덕타이핑된다. 다른 객체도 받아서 처리가 가능하다. >>각 객체의클래스들이 모두 같은 멤버함수 가지고 있어야 가능한 것
def who_says(obj):
    print(obj.who(), 'says', obj.says()) #obj자리에 클래스가 다른 객체 들이 들어갈수있다. 이때 각 클래스안에 who와 says가 들어가야한다.>>덕타이핑
# __하나나 양쪽에 있는 것은 내부적으로 정의돼있어 magic mathod:C++의 연산자 오버로딩과 같다.
# == 는 isequal과 같아... magic method를 통해서 인수 받아서 만드는 함수가 아니라 연산자에 새로운 기능을 설정해서 사용할수있도록 한것
#magic method
class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.__name = name

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #클래스에 문자열 들어가면 바로 str magic method로 이름으로만 나오도록 된게 입니다까지 같이 출력되도록...
    #+도 magic method로 설정했으면 원래 안되는 +가 되는 것 set,repr도 다 그냥 기본 클래스에 넣어주면 출력되는거인듯
    def __str__(self):
        return self.__name + " 입니다"
    def __add__(self,target):
        return self.__name +' + '+ target.__name
    def __repr__(self):
        return self.__name+"repr임"
class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1)
print(repr(g1))
print(c1)
print(g1+c1)
print(str(g1))
#클래스 전체가 공유: 클래스 객체로 만들어야 객체당 공유하면 인스턴스로 생성
#__repr__ 메서드는 주로 개발자와 디버깅을 위한 목적으로 객체의 더 명확하고 정보-rich한 문자열 표현을 제공하는 데 사용됨
#(representation)
#대화형 인터프리터(prompt창>>>)에서 직접 입력하면 __repr__이 호출