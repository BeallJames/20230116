import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')
    return True

def is_lose(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's')
    return True