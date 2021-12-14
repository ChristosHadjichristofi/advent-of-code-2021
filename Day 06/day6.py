# when a fish reaches 0 it becomes 6 and a new fish is added as 8 in the end of
# the list. However, the fish that reached 0 and became 6 as well as the new fish
# that was added must remain unchanged for this round. So because at line 11
# i subtract 1 from every fish, I add +1 to the fish that reached 0 as well as to the new fish
def day6_part1(fishes):
    for _ in range(80):
        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    return len(fishes)

# for part 2 naive approach was not good. So the fishes were represented by a dictionary
# where key was the state of the fish and as value how many fishes were in that state
# so each iteration we save how many fishes are in state zero (to add them to state 6 and 8)
# and every other state gives its value to the previous state (state 2 gives its value to state 1, state 1 gives its value to state 0 etc)
# after that we add to state 6 and 8 the dayZero variable that was saved at the begining
def day6_part2(fishes):
    for _ in range(256):
        dayZero = fishes[0]
        fishes = { f : fishes.get(f + 1, 0) for f in fishes }
        fishes[6] += dayZero
        fishes[8] += dayZero
    return sum(v for k, v in fishes.items())

def main():
    with open('input.txt', 'r') as f:
        fishes = f.read().strip().split(',')
        fishes = list(map(int, fishes))
    
    fishDict = { i: fishes.count(i) for i in range (9) }
    
    print("Part 1:", day6_part1(fishes))
    print("Part 2:", day6_part2(fishDict))

if __name__ == "__main__":
    main()