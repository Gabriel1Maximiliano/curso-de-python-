from random import randint

tries = 0
estimate = 0
secret_number = randint(1,100)
name = input("Tell me your name: ")

print(f"Okey {name},I have thought of a number between 1 and 100\nYou have 8 attempts to guess")

while tries < 8:
    estimate = int(input("Cuál es el número?: "))
    tries += 1

    if estimate < secret_number:
        print("Mi numero es mas alto")
    elif estimate > secret_number:
        print("Mi numero es mas bajo")
    else:
        print(f"Congratulations {name}! you guessed in {tries} tries")
        break

if estimate != secret_number:
    print(f"Sorry attemps exhausted . The secret number was {secret_number}")