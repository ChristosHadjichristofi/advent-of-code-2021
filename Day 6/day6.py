# when a fish reaches 0 it becomes 6 and a new fish is added as 8 in the end of
# the list. However, the fish that reached 0 and became 6 as well as the new fish
# that was added must remain unchanged for this round. So because at line 11
# i subtract 1 from every fish, I add +1 to the fish that reached 0 as well as to the new fish
def day6_part1(fishes):
    for day in range(80):
        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    return len(fishes)

def day6_part2(fishes):
    pass

def main():
    with open('input.txt', 'r') as f:
        fishes = f.read().strip().split(',')
        fishes = list(map(int, fishes))
    
    print("Part 1:", day6_part1(fishes))
    print("Part 2:", day6_part2(fishes))

if __name__ == "__main__":
    main()