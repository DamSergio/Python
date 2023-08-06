from words import words
import random
import string

def get_valid_word(words_list):
    word = random.choice(words_list) #Elige una palabra aleatoria de la lista

    while "-" in word or " " in word:
        word = random.choice(words_list)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #Letras de la palabra
    alphabet = set(string.ascii_uppercase) #Letras del abecedario
    used_letters = set() #Letras usadas

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word is: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You already used that character.")
        
        else:
            print("Invalid character.")
    
    if lives > 0:
        print(f"You guess it. The word was: {word}")

    else:
        print(f"You lost all your lives. The word was {word}")

hangman()