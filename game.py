import random
from words import words
import string
from hangman_visual import lives_visual_dict

# First we need to correct the words list because in the list we have '-' and ' ' so to valid these words we need to use a function

def valid_words(words):
    word = random.choice(words)
    while ('-' in word) or (' ' in word):
        word = random.choice(words)
    
    #Iam here converting all the word that computer choose and user choice into uppercase
    return word.upper()    

# Main function which game starts here...

def hangman():
    lives = 7
    word = valid_words(words)
    # we need to store this computer choice in a set 
    computer_letter = set(word)   # letters in the word
    alphabets = set(string.ascii_uppercase)  
    used_letters = set() # what letters user has guessed
    
    while len(computer_letter) > 0 and lives > 0:

        print(f"You have {lives} left and you have used these letters: {' '.join(used_letters)}")

        word_list = [i if i in used_letters else '-' for i in word ] 
        # result = []
        # for i in word:
        #     if i in used_letters:
        #         result.append(i)
        #     else:
        #         print('_')


        print(f"current word : {' '.join(word_list)}")

        user_letter = input("Guess a letter for the word :").upper()

        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in computer_letter:
                computer_letter.remove(user_letter)
            else:
                lives -= 1
                print("letter not in the word!")
                x = lives_visual_dict.keys()
                y = lives_visual_dict
                visual_lst = list(x)
                for i in range(len(visual_lst)):
                    for k,values in lives_visual_dict.items():
                        if k == i:
                            if i == lives:
                                print(values)

            

                    


        elif user_letter in used_letters:
            print("You already used this letter. Try guessing other")

        else:
            print("You have entered a invalid character!, Please enter a valid alphabet")

    if lives == 0:
        print(f"Sorry you lost the game and the word is {word}")
    else:    
        print(f"Congratulations you guessed the  word {word} correctly!!")


hangman()

#also add the visual in next commit

