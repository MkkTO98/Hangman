import random
import hangman_words
import hangman_art

def check_input(inp, mg):
    if isinstance(inp, str) and len(inp)==1:
        if len(mg)>0:
            for g in mg:
                if inp == g:
                    print(f"You already guessed {inp}, try again.")
                    return False
                else:
                    return True
        else:
            return True
    else:
        print("Invalid input, please input a single letter.")
        return False


def check_result(inp):
    if "".join(inp) == chosen_word:
        return True
    else:
        return False


made_guesses = []
total_guesses = int(6)
guesses_left = int(6)
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print(chosen_word)

guessed_letters_in_chosen_word = []
for letter in list(chosen_word):
    guessed_letters_in_chosen_word.append("_")



while not check_result(guessed_letters_in_chosen_word) and guesses_left > 0:
    guess = input("You have "+"❤" * guesses_left + "♡" * (total_guesses - guesses_left)+" lives left. Guess a letter:\n")

    #Checks that the input is a new single letter:
    while not check_input(guess, made_guesses):
        guess = input("Guess a letter:\n").lower()
    else:
        made_guesses.append(guess)

    #If the guess is correct it fills in the letter in the randomly chosen word,
    #then the word is printed revealing only the guessed letters. If the guess
    #is incorrect it is subtracted from the remaining guesses:
    num_letter = int(0)
    correct_guess = False
    for letter in list(chosen_word):
        if guess == letter:
            guessed_letters_in_chosen_word[num_letter] = guess
            correct_guess = True
        num_letter += 1
    if not correct_guess:
        guesses_left -= 1

    print(hangman_art.stages[guesses_left])
    print("❤" * guesses_left + "♡" * (total_guesses - guesses_left))
    print(guessed_letters_in_chosen_word)


if 0 >= guesses_left:
    print(hangman_art.stages[guesses_left])
    print("❤"*guesses_left+"♡"*(total_guesses-guesses_left))
    print("***************************YOU LOST****************************")
    print(f"The answer was: {chosen_word}")

else:
    print("****************************YOU WIN****************************")
    print("The word is: " + "".join(guessed_letters_in_chosen_word))