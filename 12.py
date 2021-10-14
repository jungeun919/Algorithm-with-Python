# 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.

# <여기에 class를 작성하세요.>

# x = Wizard(health = 545, mana = 210, armor = 10)
# print(x.health, x.mana, x.armor)
# x.attack()

# >> 출력 예시
# 545 210 10
# 파이어볼

class Wizard:
    # 초기화 메서드: 객체가 만들어질 때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print("파이어볼")

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()