import random

to_guess_number=random.randrange(100)
guess_counter=0
print("Please choose a level :\n\t 1. Easy   [","-"*5,"7 Chances","-"*5,"]\n\t 2. Medium [","-"*5,"5 Chances","-"*5,"]\n\t 3. Hard   [","-"*5,"3 Chances","-"*5,"]\n\t 4. Insane [","-"*5,"1 Chances","-"*5,"]")
level=int(input("Level : "))
match level:
    case 1:
        chances=7
        while guess_counter<chances:
            guess_counter+=1
            my_guess=int(input("Guess the number between 1 to 100 : "))
            if my_guess==to_guess_number:
                print(f"You Won!, {to_guess_number} is the number .")
                break
            elif guess_counter>=chances and my_guess!=to_guess_number:
                print(f"Oops! you lost ,{to_guess_number} was the number")
            elif my_guess > to_guess_number:
                print('Your guess is higher ')
            elif my_guess < to_guess_number:
                print('Your guess is lesser')
    case 2:
        chances=5
        while guess_counter<chances:
            guess_counter+=1
            my_guess=int(input("Guess the number between 1 to 100 : "))
            if my_guess==to_guess_number:
                print(f"You Won!, {to_guess_number} is the number .")
                break
            elif guess_counter>=chances and my_guess!=to_guess_number:
                print(f"Oops! you lost ,{to_guess_number} was the number")
            elif my_guess > to_guess_number:
                print('Your guess is higher ')
            elif my_guess < to_guess_number:
                print('Your guess is lesser')
            
    case 3:
        chances=3
        while guess_counter<chances:
            guess_counter+=1
            my_guess=int(input("Guess the number between 1 to 100 : "))
            if my_guess==to_guess_number:
                print(f"You Won!, {to_guess_number} is the number .")
                break
            elif guess_counter>=chances and my_guess!=to_guess_number:
                print(f"Oops! you lost ,{to_guess_number} was the number")
            elif my_guess > to_guess_number:
                print('Your guess is higher ')
            elif my_guess < to_guess_number:
                print('Your guess is lesser')
    case 4:
        chances=1
        while guess_counter<chances:
            guess_counter+=1
            my_guess=int(input("Guess the number between 1 to 100 : "))
            if my_guess==to_guess_number:
                print(f"You Won!, {to_guess_number} is the number .")
                break
            elif guess_counter>=chances and my_guess!=to_guess_number:
                print(f"Oops! you lost ,{to_guess_number} was the number")
            elif my_guess > to_guess_number:
                print('Your guess is higher ')
            elif my_guess < to_guess_number:
                print('Your guess is lesser')
    