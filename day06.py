class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f'{name} 포켓몬스터 생성')

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

pikachu = Pokemon("피카츄")
squietle = Pokemon("꼬부기")
charizard = Pokemon("리자몽")
print(pikachu.name)
print(squietle.name)
charizard.attack(squietle)