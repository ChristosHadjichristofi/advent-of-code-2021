import numpy as np

def findPaperLen(pairs):
    max_x = 0;
    max_y = 0;
    for (x, y) in pairs:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    return (max_x, max_y)

def day13_part1(paper, foldcmd):
    (axis, val) = foldcmd
    if axis == 'y':
        top = paper[:val]
        bottom = paper[val + 1:]        
        revBottom = np.flip(bottom, axis = 0)

        firstFold = [['#' if top[i][j] == '#' or revBottom[i][j] == '#' else '.' for j in range(len(top[0]))] for i in range(len(top))]
    else:
        left = []
        right = []

        for i in range(len(paper)):
            subLeft = []
            subRight = []
            for j in range(len(paper[0])):
                if j < val:
                    subLeft.append(paper[i][j])
                elif j > val:
                    subRight.append(paper[i][j])
            
            left.append(subLeft)
            right.append(subRight[::-1])
        
        firstFold = [['#' if right[i][j] == '#' or left[i][j] == '#' else '.' for j in range(len(left[0]))] for i in range(len(left))]

    return firstFold

def day13_part2(paper, folds):
    # same code as part1 but complete all the folds
    for (axis, val) in folds:
        if axis == 'y':
            top = paper[:val]
            bottom = paper[val + 1:]        
            revBottom = np.flip(bottom, axis = 0)

            paper = [['#' if top[i][j] == '#' or revBottom[i][j] == '#' else '.' for j in range(len(top[0]))] for i in range(len(top))]
        else:
            left = []
            right = []

            for i in range(len(paper)):
                subLeft = []
                subRight = []
                for j in range(len(paper[0])):
                    if j < val:
                        subLeft.append(paper[i][j])
                    elif j > val:
                        subRight.append(paper[i][j])
                
                left.append(subLeft)
                right.append(subRight[::-1])
            
            paper = [['#' if right[i][j] == '#' or left[i][j] == '#' else '.' for j in range(len(left[0]))] for i in range(len(left))]

    # print answer
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] == '#':
                print('#', end='')
            else:
                print(' ', end='')
                
        print('\n', end='')

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n\n')
    
    pairsInput = input[0]
    foldsInput = input[1]
    
    # construct the list of pairs
    pairs = []
    for p in pairsInput.split('\n'):
        x, y  = map(int, p.split(','))
        pairs.append((x, y))
    
    # after list of pairs is constructed, find the dimensions of the paper
    (x, y) = findPaperLen(pairs)

    # create the paper and add the # in place
    paper = [['.' for i in range(x + 1)] for j in range(y + 1)]
    for (y, x) in pairs:
        paper[x][y] = '#'

    # create the folds list (has pairs of (axis, value))
    folds = []
    for fold in foldsInput.split('\n'):
        axis, val = fold.split('=')
        folds.append((axis[-1], int(val)))

    firstFold = day13_part1(paper, folds.pop(0))
    print("Part 1:", sum([line.count('#') for line in firstFold]))
    day13_part2(firstFold, folds)

if __name__ == "__main__":
    main()