import simplegui
import random
import math

def new_game(range):
    """
    Begins new game given current or default range
    """
    if range == 100:
        range100()
    else:
        range1000()
        
def maxguesses(low, high):
    """
    Computes maximum amount of guesses
    """
    return int(math.ceil(math.log(high - low + 1, 2)))

def range100():
    """
    Sets the prereqs for a range to [0,100) game
    """
    global secret_number, guesses_left, max_num
    max_num = 100
    secret_number = random.randrange(0, max_num)
    guesses_left = maxguesses(0, max_num)
    print "||New game|| Range is 0 - 100"
    print "You have %s lives." %guesses_left
        
def range1000():
    """
    Sets the prereqs for a range to [0,1000) game
    """
    global secret_number, guesses_left, max_num
    max_num = 1000
    secret_number = random.randrange(0, max_num) 
    guesses_left = maxguesses(0, max_num)
    print "||New game|| Range is 0 - 1000"
    print "You have %s lives." %guesses_left

           
def input_guess(guess):
    global guesses_left, max_num
    guess = int(guess)
    print "You guessed %s." %guess
    if guess == secret_number and guesses_left > 1:
        print "Correct!"
        if max_num == 1000:
            new_game(1000)
        else:
            new_game(100)
    elif guess < secret_number and guesses_left > 1:
        guesses_left = guesses_left - 1
        print "Higher"
        print "You have %s lives remaining." %guesses_left
    elif guess > secret_number and guesses_left > 1:
        guesses_left = guesses_left - 1
        print "Lower"
        print "You have %s lives remaining." %guesses_left
    else:
        print "You Lose"
        print "You have 0 lives remaining; the number was %s." %secret_number
        if max_num == 1000:
            new_game(1000)
        else:
            new_game(100)

frame = simplegui.create_frame("Input Guess", 200, 200)
inp = frame.add_input("Input Guess", input_guess, 100)
button100 = frame.add_button("Range: 0-100", range100)
button1000 = frame.add_button("Range: 0-1000", range1000)

new_game(100)