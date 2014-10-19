# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

secret_number = 0
low = 0
high = 100
guess_times = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guess_times
    i = 0
    while i < high / 10:
        if (2 ** i) >= (high - low + 1):
            guess_times = i
            break
        i += 1
    secret_number = random.randrange(low, high)
    print ''
    print 'New game. Range is from', low, 'to', high
    print 'Number of remaining guesses is', guess_times
    # remove this when you add your code


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high, guess_times
    high = 100
    new_game()
    # remove this when you add your code    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high, guess_times
    high = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here 
    global guess_times
    guess_times = guess_times - 1
    guess = int(guess)
    print ''
    print "Guess was", guess
    if guess_times >= 0:
        if guess - secret_number > 0:
            print 'Lower!'
            print 'Number of remaining guesses is', guess_times
        elif guess - secret_number < 0:
            print 'Higher!'
            print 'Number of remaining guesses is', guess_times
        else:
            print 'Correct!'
            new_game()
    else:
        print 'You ran out of guesses. The answer is', secret_number
        new_game()

    # remove this when you add your code

    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
button100 = frame.add_button('Range in 0 to 100', range100, 200)
button1000 = frame.add_button('Range in 0 to 1000', range1000, 200)
text = frame.add_input('Enter the Number', input_guess, 200)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
