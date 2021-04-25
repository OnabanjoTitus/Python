from random import randint

counter = 1


def message_for_ten_or_less(counter):
    value: str
    if counter == 10:
        value = "Aha! You know the secret!"
        return value
    message_randomizer = randint(1, 2)
    if message_randomizer == 1:
        value = "You know the secret"
        return value
    if message_randomizer == 2:
        value = "You got lucky"
        return value


def message_for_more_than_ten():
    value = "You should be able to do better!"
    return value


def modified_guessing_game(user_guess):
    global counter
    random_number = randint(1, 10)
    user_guess = int(user_guess)
    if user_guess == random_number and counter <= 10:
        print(message_for_ten_or_less(counter))
    if user_guess == random_number and counter > 10:
        print(message_for_more_than_ten())
    counter += 1
    if user_guess != random_number:
        modified_guessing_game(input("Enter the user guess between 1 and 10"))


print(modified_guessing_game(input("Enter the user guess between 1 and 10")))
