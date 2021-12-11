with open('input.txt', 'r') as f:
    lines = [line.replace(' -> ', ',') for line in f.read().split('\n')]

straightLines = {}
diagonalLines = {}

for entry in lines:
    x1, y1, x2, y2 = map(int, entry.split(','))
    (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
    # straight lines
    if x1 == x2 or y1 == y2:
        for i in range (x1, x2 + 1):
            for j in range (y1, y2 + 1):
                straightLines[(i, j)] = straightLines.get((i, j), 0) + 1
                diagonalLines[(i, j)] = diagonalLines.get((i, j), 0) + 1
    # diagonal lines
    elif y1 > y2:
        j = y1
        for i in range (x1, x2 + 1):
            diagonalLines[(i, j)] = diagonalLines.get((i, j), 0) + 1
            j = j - 1
    else:
        j = y1
        for i in range (x1, x2 + 1):
            diagonalLines[(i, j)] = diagonalLines.get((i, j), 0) + 1
            j = j + 1

print("Part 1:", sum(1 for k, v in straightLines.items() if v >= 2))
print("Part 2:", sum(1 for k, v in diagonalLines.items() if v >= 2))
