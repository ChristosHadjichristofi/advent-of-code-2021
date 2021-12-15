import numpy as np
from numpy.lib.arraypad import pad


# spread the energy to all neighbours up down right left and diagonal
def spread_energy(paddedOctopuses, i, j):
    flashed = []
    neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
                  (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]

    for ni, nj in neighbours:
        # if it's -1 its the padding that was added around the input so as not to check if we're in bounds
        if paddedOctopuses[ni][nj] != -1 and paddedOctopuses[ni][nj] != 10:
            paddedOctopuses[ni][nj] += 1
            if paddedOctopuses[ni][nj] == 10:
                flashed.append((ni, nj))
    
    return flashed

def day11_part1(octopuses):
    paddedOctopuses = np.pad(octopuses, [(1, ), (1, )], constant_values = -1)

    flashes = 0

    for step in range (100):
        flashed = []
        for i in range (1, len(paddedOctopuses) - 1):
            for j in range (1, len(paddedOctopuses[0]) - 1):
                # add 1 to this octopus
                paddedOctopuses[i][j] += 1
                # if reached 10 needs to flash
                if paddedOctopuses[i][j] == 10:
                    flashed.append((i, j))
        
        # for every octopus that flashed we need to spread the energy and 
        # continue if their neighbours reached 10 too
        for i, j in flashed:
            flashed += spread_energy(paddedOctopuses, i, j)
        
        # total flashes
        flashes += len(flashed)

        # set to zero every octopus that flashed
        for i, j in flashed:
            paddedOctopuses[i][j] = 0

    return flashes

def day11_part2(octopuses):
    paddedOctopuses = np.pad(octopuses, [(1, ), (1, )], constant_values = -1)

    steps = 0

    while True:
        flashed = []
        
        for i in range (1, len(paddedOctopuses) - 1):
            for j in range (1, len(paddedOctopuses[0]) - 1):
                # add 1 to this octopus
                paddedOctopuses[i][j] += 1
                # if reached 10 needs to flash
                if paddedOctopuses[i][j] == 10:
                    flashed.append((i, j))
        
        # for every octopus that flashed we need to spread the energy and 
        # continue if their neighbours reached 10 too
        for i, j in flashed:
            flashed += spread_energy(paddedOctopuses, i, j)
        
        steps += 1
        
        # 956 because the input is surrounded by -1
        if np.sum(paddedOctopuses) == 956:
            break

        # set to zero every octopus that flashed
        for i, j in flashed:
            paddedOctopuses[i][j] = 0

    return steps

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')
        octopuses = [list(map(int, i)) for i in input]    

    print("Part 1:", day11_part1(octopuses))
    print("Part 2:", day11_part2(octopuses))

if __name__ == "__main__":
    main()