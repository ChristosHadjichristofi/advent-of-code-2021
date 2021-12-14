from functools import reduce
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
    minVals = [(paddedHeightmap[i][j], (i, j)) for i in range(1, len(paddedHeightmap) - 1) for j in range(1, len(paddedHeightmap[0]) - 1) if paddedHeightmap[i][j] < min(paddedHeightmap[i - 1][j], paddedHeightmap[i + 1][j], paddedHeightmap[i][j - 1], paddedHeightmap[i][j + 1])]
    # return the sum of all minValues + len of min values (cause the risk level is 1 + height)
    return minVals

def day9_part2(heightmap, locations):
    # same as part 1
    paddedHeightmap = np.pad(heightmap, [(1, ), (1, )], constant_values = 9)
    # keep basins in dictionary and all the locations that are part of the basin
    basins = {}
    # for every location that the lowest points where found
    for x, y in locations:
        # current list of all locations that are part of that specific basin
        curr = []
        # find the first four neighbours
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        # while neigbours exist
        while neighbours:
            # get the neighbour at the first position
            neighbour = neighbours.pop()
            (currX, currY) = neighbour
            # if the value in the heighmap is less than 9 and the neighbour is not already in the list
            # of all locations that are part of the basin
            if paddedHeightmap[currX][currY] < 9 and neighbour not in curr:
                # append the neighbour
                curr.append(neighbour)
                # update neighbours
                neighbours = neighbours + [(currX + 1, currY), (currX - 1, currY), (currX, currY + 1), (currX, currY - 1)]
        
        basins[(x, y)] = curr
    
    # construct the list with the size of each basin
    basinSizes = [len(v) for _, v in basins.items()]
    
    # return the multiplication of the largest 3 basin sizes
    return reduce((lambda x, y: x * y), sorted(basinSizes, reverse = True)[:3])

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        heightmap = [list(map(int, list(s))) for s in lines]
        minVals = day9_part1(heightmap)

        print("Part 1:", len(minVals) + sum(i for i, _ in minVals))
        # for part 2
        locations = [j for _, j in minVals]
        print("Part 2:", day9_part2(heightmap, locations))

if __name__ == "__main__":
    main()  