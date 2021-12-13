import numpy as np
def day9_part1(heightmap):
    # add 9s around the 2d array in order to check up down left right without extra checks
    # adding 9s so as not to affect anything (leave input as it was)
    # for example
    # 1 2 3        9 9 9 9 9
    # 4 5 6  --->  9 1 2 3 9
    # 7 8 6        9 4 5 6 9
    #              9 7 8 9 9
    #              9 9 9 9 9
    paddedHeightmap = np.pad(heightmap, [(1, ), (1, )], constant_values = 9)
    # find all minimum values
    minVals = [paddedHeightmap[i][j] for i in range(1, len(paddedHeightmap) - 1) for j in range(1, len(paddedHeightmap[0]) - 1) if paddedHeightmap[i][j] < min(paddedHeightmap[i - 1][j], paddedHeightmap[i + 1][j], paddedHeightmap[i][j - 1], paddedHeightmap[i][j + 1])]
    # return the sum of all minValues + len of min values (cause the risk level is 1 + height)
    return sum(minVals) + len(minVals)

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        heightmap = [list(map(int, list(s))) for s in lines]
        
        print("Part 1:", day9_part1(heightmap))

if __name__ == "__main__":
    main()  