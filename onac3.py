# made by Goov.
# ver 0.1 NR.
import random
import time
import sys

ldoor = "open"
rdoor = "open"
dfase = 1
energy = 5

def scat_attack(ldoor, rdoor, rand1):
    if rdoor == "open":
        print("+ На вас напали с правой стороны. Вы проиграли +")
        sys.exit()
    if rdoor == "close":
        print("+ На вас напали с правой стороны. Вы защитились. Все двери открылись. +")
def dcat_attack(ldoor, rdoor):
    if ldoor == "open":
        print("+ На вас напали с левой стороны. Вы проиграли +")
    elif ldoor == "close":
        print("+ На вас напали с левой стороны. Вы защитились. Все двери открылись. +")

print("-----ONAC 3-----")
print("-----START (s)-----")
print("-----HELP (h)-----")
a = input("~1: ")
if a == "s":
    ifOffice = False
    dfase = 2
    print("Мяяяууу!!!")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    ifOffice = True
    print("Жарковато...")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    rand1 = random.randint(1, 2)
    i = 1
    scat_attack(ldoor, rdoor, rand1)
    ldoor = "open"
    rdoor = "open"
    ifOffice = False
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    dfase = 3
    print("* Звуки котячей ярости *")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    dfase = 4
    print("* ОЧЕНЬ злой мяу *")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    dcat_attack(ldoor, rdoor)
    ldoor = "open"
    rdoor = "open"
    dfase = 1
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    ifOffice = True
    print("Горячо!")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    rand1 = random.randint(1, 2)
    i = 2
    scat_attack(ldoor, rdoor, rand1)
    ldoor = "open"
    rdoor = "open"
    ifOffice = False
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    dfase = 2
    print("* Холодный воздух прошёлся по оффису *")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    dfase = 3
    print("Так, готовимся к чёрному коту...")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        if dfase != 4:
            print("+ Чёрный кот на " + str(dfase) + " стадии. +")
        else:
            print("+ Чёрный кот бежит к вам! +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if ldoor == "close" or rdoor == "close":
        energy -= 1
        print("- Утрата! У вас осталось " + str(energy) + " енергии. -")
    print("* Скример серой кошки *")
    time.sleep(5)
    print("+ Вы прошли onac 3! +")
    print("+ Так же само, субтитров не будет, всё зделал Goov ;) +")
    sys.exit()

elif a == "h":
    print("-----КОМАНДЫ-----")
    print("1-открыть левую дверь.")
    print("2-открыть правую дверь.")
    print("3-стадия злости чёрного кота.")
    print("4-закрыть левую дверь.")
    print("5-закрыть правую дверь.")
    print("!!! ЧЁРНИЙ КОТ ВСЕГДА НАПАДАЕТ С ЛЕВОЙ СТОРОНЫ !!!")
    print("Перезапустите игру.")