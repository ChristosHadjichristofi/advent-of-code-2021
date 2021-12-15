
adjList = {}

visited = set()
ans_pt1 = 0

# simple dfs
def day12_part1(cave):
    global ans_pt1

    # if reached end one more solution found
    if cave == "end":
        ans_pt1 += 1
        return

    # if cave is small and already visited we can not use this again and the path is invalid
    if cave.islower() and cave in visited:
        return
    
    # if the previous check is passed, then it's the first time we found this small cave, so add it to visited
    if cave.islower():
        visited.add(cave)
    
    # for every neighbour of the current examined cave
    for neighbour in adjList[cave]:
        # if neighbour is not start do dfs for this neighbour
        if neighbour != "start":
            day12_part1(neighbour)
    
    # when all the checks for the neighbours are completed, remove cave (backtrack)
    if cave.islower():
        visited.remove(cave)

visitedTimes = {}
ans_pt2 = 0

def day12_part2(cave):
    global ans_pt2

    # if reached end one more solution found
    if cave == "end":
        ans_pt2 += 1
        return

    # if the previous check is passed, then it's the first time we found this small cave, so add it to visited
    if cave.islower():
        visitedTimes[cave] = visitedTimes.get(cave, 0) + 1
    
        should_be_one = 0
        for node, times in visitedTimes.items():
            # add one each time we find a node that was visited more than once
            # only one node should be visited twice, and all others should be visited once
            if times > 1:
                should_be_one += 1

            # if any of the nodes was visited more than twice, this path is not valid
            # so remove one from current cave because it was not actually visited
            if times > 2:
                visitedTimes[cave] -= 1
                return

        # if more than one nodes are visited more than once, remove one from current cave 
        # because it was not actually visited and return (invalid path)
        if should_be_one > 1:
            visitedTimes[cave] -= 1
            return

    # for every neighbour of the current examined cave
    for neighbour in adjList[cave]:
        # if neighbour is not start do dfs for this neighbour
        if neighbour != "start":
            day12_part2(neighbour)
    
    # when all the checks for the neighbours are completed, remove cave (backtrack)
    if cave.islower():
        visitedTimes[cave] -= 1

def main():

    for line in open('input.txt', 'r').readlines():
        node1, node2 = line.strip().split('-')
        adjList.setdefault(node1, []).append(node2)
        adjList.setdefault(node2, []).append(node1)

    day12_part1("start")
    print("Part 1:", ans_pt1)
    
    day12_part2("start")
    print("Part 2", ans_pt2)

if __name__ == "__main__":
    main()