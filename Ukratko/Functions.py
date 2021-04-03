#zagrada funkcije moze biti prazna u slucaju kada funkcija ne ovisi o ostatku koda
def greet_user (x , y):   # tj. ako ne ubacujemo u funkciju neku vrijednost koja je definirana u ostatku koda
    print(f'Hi {x} {y}')  #varijabla u zagradi ne mora biti ista kao izvan definicije funkcije
    print ('Welcome aboard') #nakon sto definiram funkciju najbolje pustiti dva razmaka izmedu ostatka koda i funkcije

name= input("What's your name: ")
surname= input ("What's your surname: ")
print ('Start')
greet_user(name, surname)  #u zagradu upisujemo ono sto ce postati varijabla funkcije
print('Finish')