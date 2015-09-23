# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
"""
Rock defeats lizard.
Scissors defeats lizard.
Lizard defeats paper.
Lizard defeats Spock.
Paper defeats Spock.
Spock defeats rock.
Spock defeats scissors.
"""
import random

# helper functions

def name_to_number(name):
    """
    Converts the parsed strings into numbers
    """
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        print "Error N2#"
    return name

def number_to_name(number):
    """
    Converts the integers back into strings
    """
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors"
    else:
        print "Error #2N"
    return number

def rpsls(player_choice): 
    """
    Runs the game
    """
    print "\n" #blank line to separate consecutive games
    print "Player chose " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "AI chose " + comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    if difference == 1 or difference == 2:
        print "Computer wins"
    elif difference == 3 or difference == 4:
        print "Player wins"
    else:
        print "Draw"    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")