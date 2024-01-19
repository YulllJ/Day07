#비슷한 개념인 property가 존재

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
    '''
    property 1
    def get_name(self):
        return self.hidden_name

    def set_name(self, new_name):
        self.hidden_name = new_name
    
    name = property(get_name, set_name)# hidden name은 노출되지 않고 property name으로 하는 것
    '''
    # property 2
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())
# setter와 getter만 property로..?
# property 1
print(g1.name)
g1.name = "잉어킹"
# #g1.__name="잉어킹" #이거 있으면 안에 맹글링 된애 말고 새로 설정한애 처럼 보여서 돌아감 다른 개념????
#이걸로해도 값이 안바뀐다고????

# print(g1.__name) #property로만 접근이 가능해 direct access x
print(g1._Pokemon__name)
g1._Pokemon__name = "잉어킹"#이렇게 하면 또 보인다.

# get_name set_name등록할 필요없이 바로 사용 가능 적용한 함수위에 annotation만 붙이면된다.
# get은 @property로 @name.setter로
# property 개념 제대로 이해하기 일반변수가 아님
# property지만 private하게 설정돼있는게 아니면 보인다 직접 접근이 가능하다. (파이썬은 접근 제한이 없다)
# 비슷하게 접근제한을 흉내내는 방법 #숨기고 싶은 변수 앞에 __을 붙이면 private하게 돼서 접근하지 못해
# 다음주 오후에 시험 지금까지 작성한 코드들 클론해서 사용해도 되고 점심시간때 미리 다 세팅해놔야 시험범위는 파이썬 전체까지
# invitation에 초대돼서 할 예정
# 한번에 하면 부정행위라고 할거기 때문에 중간중간 커밋해서 로그 남겨야돼
