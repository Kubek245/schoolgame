from random import randint, random;
#---------------------------------- HISTORIA
print('Jesteś na sali treningowej. Przed sobą masz 8 różnych przeszkód, przetestuj swoje umiejętności, przed podejściem do napadu.')
# ---------------------------------START
nick = input('Podaj swój nick: ')
life = 300
skill = 200
#---------------------------------ITEMY
def woda():
    return randint(0, 10)

def kij_golfowy():
    global skill
    skill -= 5
    return randint(10, 15)

def hammer():
    global skill
    skill -= 10
    return randint(15, 20)

def baton():
    global skill
    skill -= 15
    return randint(20, 25)

def maczeta():
    global skill
    skill -= 20
    return randint(25, 30)

def lom():
    global skill
    skill -= 25
    return randint(30, 35)

def wybierz_atak():
    print('a/A - Wylej butelke wody')
    print('b/B - Wyciągnij kij golfowy i uderz')
    print('c/C - Wyjmij młotek i uderz')
    print('d/D - Rozłóż batona i walnij')
    print('e/E - Chwyc maczete z pleców i ciachnij')
    print('f/F - Wbij łom')
    print('Wybierz jeden z ataków: ')
    co = input()
    if co.upper() == 'A':
        return woda()
    elif co.upper() == 'B':
        if skill >= 10:
            print("="*20)
            return kij_golfowy()  
        else:
            print("="*20)
            print("Niski skill ! Wybierz coś innego")
            return wybierz_atak()
    elif co.upper() == 'C':
        if skill >= 20:
            print("="*20)
            return hammer()
        else:
            print("="*20)
            print("Niski skill ! Wybierz coś innego")
            return wybierz_atak()
    elif co.upper() == 'D':
        if skill >= 25:
            print("="*20)
            return baton()
        else:
            print("="*20)
            print("Niski skill ! Wybierz coś innego")
            return wybierz_atak()
    elif co.upper() == 'E':
        if skill >= 20:
            print("="*20)
            return maczeta()
        else:
            print("="*20)
            print("Niski skill ! Wybierz coś innego")
            return wybierz_atak()
    elif co.upper() == 'F':
        if skill >= 25:
            print("="*20)
            return lom()
        else:
            print("="*20)
            print("Niski skill ! Wybierz coś innego")
            return wybierz_atak()
    else:
        print("\nNie posiadzasz takiego przedmiotu")
        print("\nWybierz jeszcze raz")
        print("="*20)
        return 0
#---------------------------------Hack
# Hack - 0 # Hp - 1 # moc uderzenia 2 #
power = ["Wyłączanie zasilania",10,20]
zabsejf = ["Wyłączanie zabezpieczenia sejfu",35,15]
password = ["Pobieranie hasła",25,10]
doorg = ["Otwieranie głównych drzwi",50,25]
doors = ["Otwieranie drugich drzwi",60,23]
sejfg = ["Otwieranie głównego sejfu",100,30]
sejfm = ["Otwieranie małego sejfu",75,22]
sejfd = ["Otwieranie dużego sejfu",80,18]
list_Hack = [power, zabsejf, password, doorg, doors, sejfg, sejfm, sejfd]

def random_hack():
    Hack =  list_Hack[randint(0,7)].copy()
    return Hack
#---------------------------------Game
liczba_wykonanych = 0
while life > 0:
    Hack = random_hack()
    print("="*20)
    while Hack[1] > 0:
        print(f"{nick} cwiczy {Hack[0]}")
        print("="*20)
        print(f"{Hack[0]} ma {Hack[1]} Hp")
        print("="*20)
        print(f"Ten hack zadaje Ci {Hack[2]} Hp")
        print("="*20)
        life = life - Hack[2]
        if life < 0:
            break
        print(f"Zostało ci:{life} hp")
        print("="*20)
        print(f"Twój poziom wynosi:{skill}")
        print("="*20)
        atak = wybierz_atak()
        Hack[1] = Hack[1] - atak
        print(f"Zadałeś {atak} obrażeń")
        print("="*40)
    print("="*20)
    print('Wykonałeś ten hack !!!')
    liczba_wykonanych += 1
    print(f"Zabiles {liczba_wykonanych} przeciwników")
    if life <= 0:
        print("="*20)
        print(f"{Hakc[0]} zadało ci bardzo dużo obrażeń! Nie żyjesz! PRZEGRAŁEŚ!")
        print("%"*20)
        print(f"Wykonałeś {liczba_wykonanych} hacków")
    elif liczba_wykonanych == 8:
        print("Jestes gotowy")
        break


print('\n \n \n \nJakub Kunda  3C')