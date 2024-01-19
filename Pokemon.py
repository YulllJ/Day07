# 주말과제-포켓몬 게임 만들어오기
# attack 진화 ...? text기반 게임 프로그램 시작하면 안내문구 야생의 누가 나타났다 이런거 player선택 뭐 이런거 ,,? 어뜨케 하라는겨
# list, dictionary로 레벨별로 공격방법..? attack할지 모르는데
# 포켓몬 도감..? 미완말고 최소한으로 만들어서 한다라던가
# 도망도 하고 ..
# 도망갔을때 랜덤하게 한다규..? 어케 한다는겨 도망가고 싶어도 못가는 경우도 있다..?
# 기획해서 해보라는 거 인듯
# 점수 메기기 보다는 수준 체크.. 예외처리도 확실히 해야한다.
# 컴퓨터와 전투하는 포켓몬 게임 만들기





class Player:
    def __init__(self,_id):
        self.name = _id
        self.level = 0
        print(f"Player: {self.name}, Level: {self.level}")

class Monster:
    def __init__(self,name,character):
        self.name = name
        self.character=character
        self.level = 0
    def attack(self):
        print(f"{self.name}이(가) {self.skill} 공격을 했다!")
    def information(self):
        print(f'name: {self.name} character: {self.character} level: {self.level}')
def print_initial_state():
    print("Welcome to Pokemon World!")
    while True:
        temp = input("Select the mode: 1. Player  2. Guest 3. Reset player info 4. Save: ")
        if temp not in ('1', '2', '3','4'):
            print("Retry!")
        else:
            global mode
            mode = int(temp)
            break
def set_player(start):
    while start:
        print_initial_state()
        # 여기서 mode가 1이나 2나 3이됨
        if mode == 1 and start == 1:
            if memo is None:
                print("There is no player information. Create a new one")
                _id = input("Please enter Player name : ")
                player = Player(_id)
                start = 0
                return player
                print("이거?")
            else:
                pass  # 파일 입출력으로 setting
        elif mode == 2 and start == 1:
            print("Guest Mode!")
            _id = input("Please enter Player name : ")
            player = Player(_id)
            start = 0
            return player
        elif mode == 3 and start == 1:
            pass  # 파일 입출력으로 setting
        elif mode == 4 and start == 1:
            pass  # save 파일 입출력으로 setting
        elif start == 1:
            print("mode error")




import random
if __name__ == "__main__":
    state = "Start"
    mode = None  # mode 변수를 전역 변수로 선언 및 초기화
    memo = None  # memo 변수가 어디서 정의되는지에 따라 초기값을 설정
    global start
    start=1
    my_monster = []  # monster list 형태로 저장
    character_dict={'pikachu':("electric","skill 1","skill 2","skill 3") , 'charizard':("타입","skill 1","skill 2","skill 3"), '이름':("타입","skill 1","skill 2","skill 3")}
    player1=set_player(start)
    random_pair= random.choice(list(character_dict.items()))
    #player정보 setting끝
    AImonster=Monster("AImonster",random_pair)

    print(AImonster.information())

