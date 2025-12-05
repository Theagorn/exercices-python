import random

mystery_number = random.randint(0, 123)
resolved = False
while not resolved:
    user_answer = int(input("Devinez le nombre mystère entre 0 et 123 : "))
    if user_answer == mystery_number:
        print("Bravo !")
        resolved = True
    elif user_answer < mystery_number:
        print("C'est plus !")
    else:
        print("C'est moins !")

#-------------------------------fin du 6.5---------------------------------