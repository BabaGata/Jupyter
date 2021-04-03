import random


members= ['John', 'Mary', 'Bob','Mosh']
leader = random.choice(members)
print(leader)
for i in range(3):
    print( random.random())
    print(random.randint(10,20))


class Dice:
    def roll(self):
        result = (random.randint(1, 6),random.randint(1, 6))
        print(f'Kocka je bačena {result}')


dice=Dice()
dice.roll()

