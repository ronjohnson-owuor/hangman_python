import random

letters_to_be_guessed = [
    'Apple', 'Banana', 'Carrot', 'Dolphin', 'Elephant',
    'Flamingo', 'Giraffe', 'Helicopter', 'Ice Cream', 'Jaguar',
    'Kangaroo', 'Lemon', 'Monkey', 'Octopus', 'Penguin', 'Quokka',
    'Rainbow', 'Strawberry', 'Turtle', 'Umbrella'
]

hangman_body_parts = [
    'Head', 'Body', 'Left Arm', 'Right Arm', 'Left Leg', 'Right Leg'
]

# get the guessed letter and its word count
guessed = random.choice(letters_to_be_guessed).lower()
length = len(guessed)
print(f"its a {length} letter word!")
game_over = False


def end_game():
    global guessed
    global game_over
    global hangman_body_parts

    should_end = input("Do you want to start again: (y/n)").lower()
    if should_end == 'n':
        game_over = True
    else:
        hangman_body_parts = [
            'Head', 'Body', 'Left Arm', 'Right Arm', 'Left Leg', 'Right Leg'
        ]
        guessed = random.choice(letters_to_be_guessed).lower()


def handle_logic(guessed_letter):
    global guessed
    if guessed_letter in guessed:
        print("you found a letter!")
        guessed = guessed.replace(guessed_letter, '')
    else:
        removed_body_part = hangman_body_parts.pop(0)
        print(f'we removed {removed_body_part}')

    if len(guessed) == 0:
        print("You won by a mile!🎉")
        end_game()
    elif len(hangman_body_parts) == 0:
        print("sorry, you lost try next time 😔")
        end_game()


while len(hangman_body_parts) != 0:
    while True:
        user_guessed_letter = input("guess a letter in the word: ").lower()
        if len(user_guessed_letter) == 1:
            handle_logic(user_guessed_letter)
            break
        else:
            print("one letter at a time")

    if game_over:
        break
