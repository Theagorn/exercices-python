import random

mystery_number = random.randint(0, 123)
resolved = False
minimum = 0
maximum = 123
tentatives = 0


while not resolved:
    tentatives += 1
    answer = (minimum + maximum) // 2
    print(f"Je propose : {answer}")
    if answer == mystery_number:
        print("Bravo ! Le nombre était :", mystery_number)
        print("Nombre de tentatives :", tentatives)
        resolved = True
    elif answer < mystery_number:
        print("C'est plus !")
        minimum = answer + 1
    else:
        print("C'est moins !")
        maximum = answer - 1

#-------------------------------fin du 6.5.2---------------------------------