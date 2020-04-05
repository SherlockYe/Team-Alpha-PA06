import random
def play_hangman():
    want_to_play = True
    words= list('happy', 'brandeis', 'alpha', 'quarantine','coronavirus','zoom','computerscience','programming')
    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        word = random.choice(words)
        letter = input('Please choose a letter')
        done = False
        while not done:
            if letter in guessed_letters:
                "subtract one from guesses_left"
                "and tell them they already guessed that letter"
            elif letter not in word:
                "add letter to guessed letters"
                "tell user the letter is not in the word"
                "subtract one from the guesses_left"
            else:
                "add letter to guessed letters"
                "tell user the letter is in the word"
            if "all the letters in the word have been guessed":
                "set done to be true and tell the user they won!"
            elif "the number of guesses left is zero":
                "set done to be true and tell the user they lost!"
            else:
                "print the word with a dash for each letter not in guessed_letters"
                letter = "ask the user for another letter"
        want_to_play = "ask the user if they want to play another game..."