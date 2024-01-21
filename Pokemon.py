# 주말과제-포켓몬 게임 만들어오기
# attack 진화 ...? text기반 게임 프로그램 시작하면 안내문구 야생의 누가 나타났다.
# 이런거 player선택 뭐 이런거 ,,? 어뜨케 하라는겨
# list, dictionary로 레벨별로 공격방법..? attack할지 모르는데
# 포켓몬 도감..? 미완말고 최소한으로 만들어서 한다라던가 도망도 하고 ..
# 도망갔을때 랜덤하게 한다규..? 어케 한다는겨 도망가고 싶어도 못가는 경우도 있다..?
# 기획해서 해보라는 거 인듯   # 점수 메기기 보다는 수준 체크.. 예외처리도 확실히 해야한다.
# 컴퓨터와 전투하는 포켓몬 게임 만들기
# 물불풀 물이 불한테 강해 불은 풀한테 강해 풀은 물이 강해 상성에 맞게 hp감소는 1,2,3
# 내가 0이면 졌습니다 끝나고 내가 이기면 상대방 캐릭터 나한테 저장

class Player:
    def __init__(self,_id):
        self.name = _id
        self.level = 0
        print(f"Player: {self.name}, Level: {self.level}")
        self.my_monster = []  # monster list 형태로 저장 객체들을 받아야돼

    def get_monster(self,monster):
        new_monster = {}
        monster_name=input("Create your monster name: ")
        new_monster=Monster(monster_name,monster)
        self.my_monster.append(new_monster)
    def monster_dictionary(self):
        print(f"내가 가진 monster : ")
        try:
            for i in self.my_monster:
                print(f'name: [{i.name}] character: [{i.character}] level: [{i.level}]')
        except:
            print("monster도감 오류")


class Monster:
    def __init__(self,name,character_pair):
        #print(character_pair,type(character_pair))
        self.name = name
        self.character,self.type_skill=character_pair#dictionary로 받아야 character는 key, skill은 values
        #print(type(self.character),type(self.type_skill)) string, tuple
        self.level = 0
        self.type_skill=list(self.type_skill)
        self.type, self.skill = self.type_skill[0], self.type_skill[1:]
        self.hp = 10
    def attack(self,attack):
        print(f"{self.name}이(가) {attack} 공격을 했다!")
    def attacked(self,monster_attack):
        print(f"{self.name}이(가) {monster_attack} 공격을 받았다!")#여기 수정 요함
    def information(self):
        print(f'name: [{self.name}] character: [{self.character}] level: [{self.level}] hp: [{self.hp}]')
def print_initial_state():
    print("Welcome to Pokemon World!")
    while True:
        temp = input("Select the mode: 1. Player  2. Guest 3. Reset player info 4. Save: 5. terminate game")
        if temp not in ('1', '2', '3','4','5'):
            print("Retry!")
        else:
            global mode
            mode = int(temp)
            break
def set_player():
        global mode, start
        # 여기서 mode가 1이나 2나 3이됨
        if mode == 1 and start == 1:
            if memo is None:
                print("There is no player information. Create a new one")
                _id = input("Please enter Player name : ")
                player = Player(_id)
                start = 0
                return player
            else:
                pass  # 파일 입출력으로 setting
        elif mode == 2 and start== 1:
            print("Guest Mode!")
            _id = input("Please enter Player name : ")
            player = Player(_id)
            start = 0
            return player

        elif mode == 3 and start == 1:
            pass  # 파일 입출력으로 setting
        elif mode == 4 and start == 1:
            pass  # save 파일 입출력으로 setting
        elif mode == 5 :
            print("terminate the game")
            sys.exit(0)

        elif start == 1:
            print("mode error")
def print_game():

    while True : #대문자 아님 주의...
        menu=input("1.싸운다 2.my pokemon 3.도망친다")
        if menu == '1':
            print("Start!")
            return 1
        elif menu == '2':
            return 2
            pass
        elif menu == '3':
            return 3
            pass
        else:
            print("Retry")
def select(player):
    print("Select a monster:")
    for index, each_monster in enumerate(player.my_monster):
        print(f"{index + 1}. {each_monster.name}")

    while True:
        try:
            selected_index = int(input("Enter the number of the monster you want to select: ")) - 1
            if 0 <= selected_index < len(player.my_monster):
                selected_monster = player.my_monster[selected_index]
                print(f"You selected: {selected_monster.name}")
                return selected_monster
            else:
                print("Invalid index. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def battle(player, monster,selected_monster):
    print(monster.information())
    while monster.hp > 0 or selected_monster.hp > 0:
        print(f'name: {selected_monster.name} skill:{selected_monster.skill}')
        choice = input("어떤 공격을 하시겠습니까? 1,2,3")
        if choice == '1' :
            selected_monster.attack(selected_monster.skill[0])
            if (monster.type == '풀' and selected_monster.type == '물') or (
                    monster.type == '불' and selected_monster.type == '풀') or (
                    monster.type == '물' and selected_monster.type == '불'):
                print("효과가 미미했다.")
                monster.hp -= 1

            elif (monster.type == '물' and selected_monster.type == '풀') or (
                    monster.type == '풀' and selected_monster.type == '불') or (
                    monster.type == '불' and selected_monster.type == '물'):
                print("효과가 굉장했다.")
                monster.hp -= 3

            else:
                monster.hp -= 2
        elif choice == '2' :
            selected_monster.attack(selected_monster.skill[1])
            monster.hp -= 2
        elif choice == '3' :
            selected_monster.attack(selected_monster.skill[2])
            monster.hp -= 2

        else:
            print("공격 if문에서 문제발생함")
        print(f'{monster.name} HP :{monster.hp} {selected_monster.name} HP :{selected_monster.hp}')
        if monster.hp <= 0 or selected_monster.hp <= 0: break

        #AI공격 시작
        random_number = random.randint(0, 2)
        if random_number == 0 :
            monster.attack(monster.skill[0])
            if (monster.type == '풀' and selected_monster.type == '물') or (
                    monster.type == '불' and selected_monster.type == '풀') or (
                    monster.type == '물' and selected_monster.type == '불'):
                print("효과가 굉장했다.")
                selected_monster.hp -= 3
            elif (monster.type == '물' and selected_monster.type == '풀') or (
                    monster.type == '풀' and selected_monster.type == '불') or (
                    monster.type == '불' and selected_monster.type == '물'):
                print("효과가 미미했다.")
                selected_monster.hp -= 1
            else:
                selected_monster.hp -= 2
        elif random_number == 1 :
            monster.attack(monster.skill[1])
            selected_monster.hp -= 2
        elif random_number == 2 :
            monster.attack(monster.skill[2])
            selected_monster.hp -= 2
        else:
            print("공격 if문에서 문제발생함")
        print(f'{monster.name} HP :{monster.hp} {selected_monster.name} HP :{selected_monster.hp}')

    if monster.hp <= 0 and selected_monster.hp > 0:
        print(f'{player.name}이(가) 이겼습니다')
        print(f'{player.name}이(가) {monster.character}를 획득합니다!')
        new_monster=[monster.character,monster.type_skill]
        player.get_monster(new_monster)
    elif monster.hp <= 0 and selected_monster.hp > 0:
        print(f'{player.name}이(가) 졌습니다')
def main():
    state = "Start"
    global mode
    global memo
    global start
    mode = None  # mode 변수를 전역 변수로 선언 및 초기화
    memo = None  # memo 변수가 어디서 정의되는지에 따라 초기값을 설정

    start = 1
    while True:
        print_initial_state()
        character_dict = {'이상해씨': ("풀", "덩굴채찍-풀", "몸통박치기", "울음소리"),
                          '파이리': ("불", "불꽃세례-불", "할퀴기", "울음소리"),
                          '꼬부기': ("물", "물대포-물", "몸통박치기", "꼬리흔들기")}
        player1 = set_player()
        print("랜덤으로 몬스터를 한마리 갖습니다.")
        initial_key = random.choice(list(character_dict.keys()))
        initial_pair = [initial_key, (character_dict[initial_key])]
        player1.get_monster(initial_pair)#여기서 프린트
        # player정보 setting끝
        print("Game Start!")
        print("야생의 AI monster가 나타났다.")
        selected_monster = select(player1)
        while True:

            game = print_game()
            if game ==1:
                random_key = random.choice(list(character_dict.keys()))
                character_pair = [random_key, (character_dict[random_key])]
                AImonster = Monster("AImonster", character_pair)
                # AI monster setting 끝
                battle(player1,AImonster,selected_monster)

            elif game == 2:
                player1.monster_dictionary()
            elif game == 3:
                break
            else:
                print("print game error")
       # print(print_game())
        #print(AImonster.type, AImonster.skill)
       # AImonster.attack(2)

import random
import sys
if __name__ == "__main__":
   main()

