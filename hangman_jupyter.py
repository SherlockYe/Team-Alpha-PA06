import random
def generate_random_word(word):
    return list(word)
words= 'happy brandeis alpha quarantine coronavirus zoom computerscience programming'
word = generate_random_word(words)
def play_hangman():
    want_to_play = True
    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        letter = input('Please choose a letter')
        done = False
        while not done:
            if letter in guessed_letters:
                guesses_left-=1 ##subtract one from guesses_left
                print('You just guessed',letter)##and tell them they already guessed that letter
            elif letter not in word:
                guessed_letters.append(letter)##add letter to guessed letters
                print('Sorry, the word you guessed is not in the word')#tell user the letter is not in the word
                guesses_left-=1##subtract one from the guesses_left
            else:
                guessed_letters.append(letter)##add letter to guessed letters
                print('Congrats!! The letter you guessed is in the word')##tell user the letter is in the word
            if guessed_letters in word: ##all the letters in the word have been guessed
                print('Congrats!! You found the word!!')
                done ##set done to be true and tell the user they won!
            elif guesses_left==0:##the number of guesses left is zero
                print('Sorry, you have used up all your attempts. You lost.')
                done ##set done to be true and tell the user they lost!
            else:
                print('The word is', word,'-----',letter not in word)##print the word with a dash for each letter not in guessed_letters
                letter =input('Please enter another letter.') ##ask the user for another letter
        want_to_play = input('Do you want to play another game? Y/N')##ask the user if they want to play another game...
        if want_to_play=='Y':
            continue
        else:
            break
play_hangman()