secret_number = 7

guess = 0

while guess != secret_number:
    guess = int(input("What's the number? "))

    if guess == secret_number:
        print("You Won! ")
    elif guess < secret_number:
        print("too low, try guess it again")
    elif guess > secret_number:
        print("too high, try guess it again")
    else:
        print("Wrong,guess again")


