import sys
import os
import random


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power

    def nomal_attack(self, target):
        damage = random.randint(self.power - 2, self.power + 2)
        target.hp = max(target.hp - damage, 0)
        print(f'{self.name}이 {target.name}에게 {damage}의 일반공격 데미지를 입혔습니다.')
        if target.hp == 0:
            print(f'{target.name}이 쓰러졌습니다.')

    def check_status(self):
        print(f'{self.name}의 체력 : {self.hp} / {self.max_hp}')


class Player(Character):
    def __init__(self, name, hp, mp, power, magic_power):
        super().__init__(name, hp, power)
        self.mp = mp
        self.max_mp = mp
        self.magic_power = magic_power

    def magic_attack(self, target):
        damage = random.randint(self.magic_power - 10, self.magic_power + 10)
        target.hp = max(target.hp - damage, 0)
        self.mp = max(self.mp - 20, 0)
        print('MP 20 소모했습니다')
        print(f'{self.name}이 {target.name}에게 {damage}의 마법공격 데미지를 입혔습니다.')
        if target.hp == 0:
            print(f'{target.name}이 쓰러졌습니다.')

    def check_status(self):
        print(
            f'{self.name}의 HP : {self.hp} / {self.max_hp}, MP {self.mp} / {self.max_mp}')


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


os.system('cls')
name = input('플레이어의 이름을 입력해주세요 : ')
player = Player(name, 100, 60, 20, 30)
monster_list = [Monster('슬라임', 100, 10),
                Monster('주황버섯', 200, 20),
                Monster('골렘', 300, 30),]
monster_dict = {i: x for i, x in enumerate(monster_list, 1)}
monster_select = int(input('몬스터를 선택해주세요. 1:슬라임 2:주황버섯, 3:골렘'))
monster = monster_dict[monster_select]
while player.hp > 0 or monster.hp > 0:
    if player.hp == 0:
        print('패배')
        print('게임을 종료합니다.')
        sys.exit()
    player.check_status()
    monster.check_status()
    print('=' * 50)
    action = input('행동을 선택해주세요. 1.일반공격 / 2.마법공격(MP 20소모) / exit 게임종료')
    print('=' * 50)
    if action == "1":
        player.nomal_attack(monster)
    elif action == "2":
        if player.mp < 20:
            print('MP가 부족합니다!')
            continue
        player.magic_attack(monster)
    elif action == 'exit':
        sys.exit()
    else:
        print('제대로 입력해주세요!')
        continue

    if monster.hp == 0:
        print('승리')
        print('게임을 종료합니다.')
        sys.exit()
    monster.nomal_attack(player)
    print('=' * 50)
