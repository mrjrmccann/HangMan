import random

word_list = [
    "dead",
    "hotdog",
    "workshop",
    "overwhelm",
    "main",
    "disk",
    "priority",
    "assist",
    "conclusion",
    "racism",
    "sweat",
    "weigh",
    "harass",
    "crisis",
    "inside",
    "embark",
    "genuine",
    "stool",
    "diplomat",
    "reptile",
    "pressure",
    "kidnap",
    "voyage",
    "stream",
    "wisecrack",
    "force",
    "terminal",
    "date",
    "trolley",
    "oh",
    "wonder",
    "coverage",
    "maid",
    "splurge",
    "woman",
    "courtship",
    "instinct",
    "extension",
    "tick",
    "socialist",
    "expenditure",
    "pastel",
    "practical",
    "connection",
    "selection",
    "bag",
    "offend",
    "ordinary",
    "depression",
    "father"
]

selected_word = random.choice(word_list)
randomized = []
randomized.append(selected_word)
random_word = ''.join(randomized)
letter_list = []
for letter in str(random_word):
    letter_list.append(letter)

blank_spaces = []
for i in range(len(letter_list)):
    blank_spaces.append("_")

wrong_guesses = []

def guess():
    guesses = 10
    while guesses > 0:
        letter_guess = input("Guess a letter: ").lower()
        if letter_guess.isalpha() is False or len(letter_guess) > 1:
            print("That is not a single letter, try again")
        elif letter_guess in letter_list and letter_list.count("*") == len(letter_list) - 1:
            print("The word was: " + str(selected_word) + " Congratulations! You Win!")
            break
        elif letter_guess in letter_list:
            space_to_replace = letter_list.index(letter_guess)
            blank_spaces[space_to_replace] = letter_guess
            letter_list[space_to_replace] = "*"
            if letter_guess in letter_list and letter_guess in letter_list:
                space_to_replace = letter_list.index(letter_guess)
                blank_spaces[space_to_replace] = letter_guess
                letter_list[space_to_replace] = "*"
            print("Wrong Guesses: " + str(wrong_guesses))
            print(blank_spaces)
            print("Correct! You have " + str(guesses) + " guesses left")
        elif letter_guess in blank_spaces:
            print("You already correctly guessed " + str(letter_guess))
        elif letter_guess in wrong_guesses:
            print("You already incorrectly guessed " + str(letter_guess))
        else:
            wrong_guesses.append(letter_guess)
            guesses -= 1
            print("Wrong Guesses: " + str(wrong_guesses))
            print(blank_spaces)
            print("Wrong. You have " + str(guesses) + " guesses left.")
    else:
        print("Sorry, you are out of guesses. The word was: " + str(selected_word))


def main():
    start_game = input("Would you like to play Hangman (Y/N)? ").upper()
    if start_game == "Y":
        print(blank_spaces)
        guess()
    elif start_game == "N":
        print("Goodbye")
    else:
        print("Invalid Selection, Try again")


main()
