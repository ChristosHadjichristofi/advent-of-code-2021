def day14_pt1_pt2(polymer, rules, lettersFreq):
    for step in range(40):
        updPolymer = {}
        for rule in rules:
            pair, addon = rule
            if pair in polymer.keys():
                lettersFreq[addon] = lettersFreq.get(addon, 0) + polymer[pair]
                updPolymer[pair[0] + addon] = polymer[pair] + updPolymer.get(pair[0] + addon, 0)
                updPolymer[addon + pair[1]] = polymer[pair] + updPolymer.get(addon + pair[1], 0) 

        polymer = updPolymer

        if step == 9:
            print("Part 1:", max(lettersFreq.values()) - min(lettersFreq.values()))

    print("Part 2:", max(lettersFreq.values()) - min(lettersFreq.values()))

def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')
    
    polymer = input[0]

    polymerMap = {}
    lettersFreq = {}
    for i in range(len(polymer) - 1):
        polymerMap[polymer[i] + polymer[i + 1]] = polymerMap.get(polymer[i] + polymer[i + 1], 0) + 1
        lettersFreq[polymer[i]] = lettersFreq.get(polymer[i], 0) + 1
    
    lettersFreq[polymer[-1]] = lettersFreq.get(polymer[-1], 0) + 1 
    
    rules = []
    for row in input[2:]:
        pair, addon = row.split(' -> ')
        rules.append((pair, addon))
    
    day14_pt1_pt2(polymerMap, rules, lettersFreq)
   
if __name__ == "__main__":
    main()