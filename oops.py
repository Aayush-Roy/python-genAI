class ChaiCup:
    cup = 150

    def describe(self):
        return f'A {self.cup}ml cup chai'

cup = ChaiCup()
print(cup.describe())
print(ChaiCup.describe(cup))

cup_two = ChaiCup()
cup_two.cup = 100
print(ChaiCup.describe(cup_two))