def day15_pt1_pt2(riskMap):
    rows, cols = (len(riskMap), len(riskMap[0]))
    # keep best distance for each cell
    distance = [[None for i in range(cols)] for j in range(rows)]
    # dx and dy combined create the adjacent cells
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # keep cells that found the ans for them (the ans might change if we find a better one)
    cells = {(0, 0)}
    # distance of cell 0,0 is 0
    distance[0][0] = 0

    # while he have not found the best solution for each cell
    while cells:
        # get cell at the leftmost position of the set
        currX, currY = cells.pop()
        for i in range(4):
            # create each time the adjacent cell
            x = currX + dx[i]
            y = currY + dy[i]

            # if out of bounds continue to next iter
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue

            # if distance of dest cell is greater than the one trying to calculate
            # update the distance of the dist cell
            if distance[x][y] is None or distance[x][y] > distance[currX][currY] + riskMap[x][y]:
                distance[x][y] = distance[currX][currY] + riskMap[x][y]
                cells.add((x, y))
    
    return distance[rows - 1][cols - 1]

def extend(riskMap):
    extendedRiskMap = []

    for j in range(5):
        for row in riskMap:
            updRow = []
            for i in range(5):
                updRow += [el + i + j if el + i + j <= 9 else (el + i + j) % 9 for el in row]

            extendedRiskMap.append(updRow)

    return extendedRiskMap

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')
        riskMap = [list(map(int, i)) for i in input]    

    print("Part 1:", day15_pt1_pt2(riskMap))
    print("Part 2:", day15_pt1_pt2(extend(riskMap)))

if __name__ == "__main__":
    main()