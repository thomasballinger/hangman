

guesses = []
max_wrong_guesses = 6


def image(stage):
    """shows a various portions of a hanging man"""
    print stage, max_wrong_guesses - stage, ' guessses left'




def main():
    word = 'hangman'
    blanks = [None] * len(word)
    while True:
        image(len(guesses))
        print blanks
        guess = raw_input('guess ')
        if guess in word:
            blanks = [letter if letter == guess else blank for blank, letter in zip(blanks, word)]
        else:
            guesses.append(guess)
        
        if len(guesses) == max_wrong_guesses:
            image(len(guesses))
            print 'you lose!'
            return
        if not None in blanks:
            print 'you win!'
            return

main()
