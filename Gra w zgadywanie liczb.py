from random import randint

my_number = randint(0, 100)

guessed = False

while not guessed:
    the_guess = input("Guess the number: ")

    try:
        the_guess = int(the_guess)
    except ValueError:
        print("not a number!")
        continue

    if the_guess > my_number:
        print("Too big")
        continue
    elif the_guess < my_number:
        print("Too small")
        continue
    elif the_guess == my_number:
        print("you win!")
        guessed = True

