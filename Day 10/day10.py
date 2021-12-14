def day10_part1(input):
    score = 0
    # keep the pairs of opening and closing symbols of chunks
    pairs = {'[' : ']', '(' : ')', '{' : '}', '<' : '>'}
    # points that each illegal char costs
    points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    # for every sequence
    for syntaxStr in input:
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
                break
    
    return score


def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')

    print("Part 1:", day10_part1(input))

if __name__ == "__main__":
    main()  