import random
class Starting_Pokemon:
    def __init__(self):
        self.username = self
    def username(self):
        username = input("트레이너의 이름을 입력하세요: ")
        print(f'{username}, 환영합니다!')
    def choosepokemon(self):
        starting = ['모부기', '팽도리', '불꽃숭이']

class Pikachu:
    def __init__(self, name, hp, fly):
        self.name = name
        self.hp = hp
        self.fly_behavior = fly


