from functools import lru_cache 
from itertools import product

roll_combinations = list(product([1, 2, 3], repeat = 3))

def turn(dice, pos, score):
    dice += 3
    rolls = sum([i + 1 for i in range(dice - 3, dice)])
    pos = (pos + rolls) % 10
    score += pos + 1
    return dice, pos, score

def deterministicDice(pos_p1, pos_p2):
    dice = score_p1 = score_p2 = 0
    isWinnerP1 = False

    while True:
        dice, pos_p1, score_p1 = turn(dice, pos_p1, score_p1)
        if score_p1 >= 1000:
            isWinnerP1 = True
            break
        dice, pos_p2, score_p2 = turn(dice, pos_p2, score_p2)
        if score_p2 >= 1000:
            break
    
    if isWinnerP1:  return dice * score_p2
    else:           return dice * score_p1

@lru_cache(maxsize = None)
def quantumDice(p1, p2, s1, s2):
    if (s2 >= 21): return (0, 1)

    total_p1_wins = total_p2_wins = 0
    
    for r1, r2, r3 in roll_combinations:
        new_position = (p1 + r1 + r2 + r3) % 10
        new_score = s1 + new_position + 1

        p2_wins, p1_wins = quantumDice(p2, new_position, s2, new_score)

        total_p1_wins += p1_wins
        total_p2_wins += p2_wins
    
    return (total_p1_wins, total_p2_wins)

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')

    start_pos_p1 = int(input[0].split(': ')[1]) - 1
    start_pos_p2 = int(input[1].split(': ')[1]) - 1
    print("Part 1:", deterministicDice(start_pos_p1, start_pos_p2))
    print(max(quantumDice(start_pos_p1, start_pos_p2, 0, 0)))
if __name__ == "__main__":
    main()