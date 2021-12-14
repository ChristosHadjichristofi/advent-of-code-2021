from io import SEEK_CUR


def day10_part1(input):
    score = 0
    incomplete = []
    # keep the pairs of opening and closing symbols of chunks
    pairs = {'[' : ']', '(' : ')', '{' : '}', '<' : '>'}
    # points that each illegal char costs
    points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    # for every sequence
    for syntaxStr in input:
        illegal = False
        # create a stack every time
        stack = []
        # for every char in the sequence
        for char in syntaxStr:
            # if it's an opening bracket push to stack
            if char in "[({<":
                stack.append(char)
            # if its a closing bracket and does not matches the top of the stack - illegal char, update score, continue to next sequence
            elif pairs[stack.pop()] != char:
                score += points[char]
                illegal = True
        
        if not illegal:
            incomplete.append(stack)
    
    return (score, incomplete)

def day10_part2(incomplete):
    scores = []
    pairs = {'[' : ']', '(' : ')', '{' : '}', '<' : '>'}
    points = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
    for sequence in incomplete:
        score = 0
        while sequence:
            score = score * 5 + points[pairs[sequence.pop()]]
        scores.append(score)
    
    middleElement = int(len(scores) / 2)
    
    return sorted(scores)[middleElement]

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')

    # return score of part 1 and the incomplete sequences to calc score in part 2
    (score, incomplete) = day10_part1(input)

    print("Part 1:", score)
    print("Part 2:", day10_part2(incomplete))

if __name__ == "__main__":
    main()  