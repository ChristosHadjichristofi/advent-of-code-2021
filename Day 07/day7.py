def calcDistancePart1(horizontal, distanceFrom):
    return sum(abs(x - distanceFrom) for x in horizontal)

def calcDistancePart2(horizontal, distanceFrom):
    return sum(i for x in horizontal for i in range(1, abs(x - distanceFrom) + 1))

def binarySearch(lower, upper, horizontal, part1DistFunction = True):
    result = 0
    while (lower < upper):
        middle = lower + (upper - lower) // 2

        if (part1DistFunction):
            a = calcDistancePart1(horizontal, middle)
            b = calcDistancePart1(horizontal, middle + 1)
        else:
            a = calcDistancePart2(horizontal, middle)
            b = calcDistancePart2(horizontal, middle + 1)

        result = min(a, b)
        
        if (a > b):
            lower = middle + 1
        elif a < b:
           upper = middle
        else:
            break

    return result 

def main():
    with open('input.txt', 'r') as f:
        horizontal = f.read().strip().split(',')
        horizontal = sorted(list(map(int, horizontal)))

    print("Part 1:", binarySearch(min(horizontal), max(horizontal), horizontal))
    print("Part 2:", binarySearch(min(horizontal), max(horizontal), horizontal, False))

if __name__ == "__main__":
    main()