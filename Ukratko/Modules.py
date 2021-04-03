import converters
from converters import lbs_to_kg

print(lbs_to_kg(30))

print(converters.kg_to_lbs(70))



from utils import find_max
numbers=list()
b=int(input("How many numbers do you want in list? "))
for y in range(b):
    a=int(input("Write a number: "))
    numbers.append(a)

print (f'Max number in list={numbers} is {max(numbers)}.')
#da bi pozvala funkciju find_max mogu i cijelu napisat pod print