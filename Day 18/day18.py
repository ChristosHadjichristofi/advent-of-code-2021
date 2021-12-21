from functools import reduce
from itertools import permutations
import math

# calculates the magnitude as the puzzle says
# recursive function
def magnitude(snailNumber):
    if len(snailNumber) > 1:
        for i in range (len(snailNumber) - 1):
            reg1, depth1 = snailNumber[i]
            reg2, depth2 = snailNumber[i + 1]

            if depth1 != depth2:
                continue

            snailNumber = snailNumber[:i] + [[reg1 * 3 + reg2 * 2, depth1 - 1]] + snailNumber[i + 2:] 

            return magnitude(snailNumber)
    
    return snailNumber[0][0]

# splits numbers that are geq than 10 and replaces them with [number/2 rounded down, number/2 rounded up]
def split(snailNumber):
    for i in range(len(snailNumber)):
        reg, depth = snailNumber[i]
        if (reg >= 10):
            round_down = math.floor(reg / 2.0)
            round_up = math.ceil(reg / 2.0)
            return snailNumber[:i] + [[round_down, depth + 1], [round_up, depth + 1]] + snailNumber[i + 1:], True
    
    return snailNumber, False

# performs an explosion. Explosion occurs when a pair's depth is greater or equal to 4
def explode(snailNumber):
    for i in range(len(snailNumber) - 1):
        reg1, depth1 = snailNumber[i]
        reg2, depth2 = snailNumber[i + 1]

        if depth1 < 5 or depth1 != depth2:
            continue

        if i > 0:
            snailNumber[i - 1][0] += reg1
        if i < len(snailNumber) - 2:
            snailNumber[i + 2][0] += reg2
        
        return snailNumber[:i] + [[0, depth1 - 1]] + snailNumber[i + 2:], True
    
    return snailNumber, False

# function that adds 2 snailfish numbers
# its used on part 1 with reduce function
def add(leftSN, rightSN):
    action = True
    result = [[regularNum, depth + 1] for regularNum, depth in leftSN + rightSN]
    while action:
        result, action = explode(result)
        if action:
            continue
        result, action = split(result)
        if not action:
            break
    
    return result

def main():
    snailnumbers = []

    for l in open('input.txt', 'r').readlines():
        snailNumber = []
        depth = 0
        for character in l:
            if character == '[':
                depth += 1
            elif character == ']':
                depth -= 1
            elif character.isdigit():
                snailNumber.append([int(character), depth])
        
        snailnumbers.append(snailNumber)
    
    print("Part 1:", magnitude(reduce(add, snailnumbers)))
    part2ans = max(magnitude(add(sn1, sn2)) for sn1, sn2 in permutations(snailnumbers, 2))
    print("Part 2:", part2ans)

if __name__ == "__main__":
    main()