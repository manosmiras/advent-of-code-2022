from enum import Enum
import string

ABC = string.ascii_uppercase[0:3]
XYZ = string.ascii_uppercase[23:26]
class Outcome(Enum):
    LOSS = 0
    DRAW = 1
    VICTORY = 2

class TheirMove(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class MyMove(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

def score_for_outcome(outcome):
    return outcome * 3

def calculate_outcome(their_move, my_move):
    their_move_value = ABC.find(their_move)
    my_move_value = XYZ.find(my_move)
    if (my_move_value + 1) % 3 == their_move_value:
        return Outcome.LOSS.value
    elif my_move_value == their_move_value:
        return Outcome.DRAW.value
    else:
        return Outcome.VICTORY.value

def calculate_my_score_p1(their_move, my_move):
    score = XYZ.find(my_move) + 1
    return score + score_for_outcome(calculate_outcome(their_move, my_move))

def get_required_move(their_move, required_outcome):
    their_move_value = ABC.find(their_move)
    required_outcome_value = XYZ.find(required_outcome)
    if required_outcome_value == Outcome.DRAW.value:
        return XYZ[their_move_value]
    elif required_outcome_value == Outcome.VICTORY.value:
        return XYZ[(their_move_value + 1) % 3]
    else:
        return XYZ[(their_move_value - 1) % 3]
def calculate_my_score_p2(their_move, required_outcome):
    my_move = get_required_move(their_move, required_outcome)
    score = XYZ.find(my_move) + 1
    return score + score_for_outcome(calculate_outcome(their_move, my_move))

file = open("input.txt", "r")
data = file.read()
lines = data.splitlines()
total_score_p1 = 0
total_score_p2 = 0
for line in lines:
    moves = line.split()
    total_score_p1 += calculate_my_score_p1(moves[0], moves[1])
    total_score_p2 += calculate_my_score_p2(moves[0], moves[1])
print("Part 1 score: ", total_score_p1)
print("Part 2 score: ", total_score_p2)
file.close()