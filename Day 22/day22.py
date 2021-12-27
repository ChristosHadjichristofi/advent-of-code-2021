def day22_part1(instructions):
    grid = {}

    for instruction in instructions:
        
        if instruction["x_from"] < -50 or instruction["x_to"] > 50 \
           or instruction["y_from"] < -50 or instruction["y_to"] > 50 \
           or instruction["z_from"] < -50 or instruction["z_to"] > 50:
            continue
        
        for x in range(instruction["x_from"], instruction["x_to"] + 1):
            for y in range(instruction["y_from"], instruction["y_to"] + 1):
                for z in range(instruction["z_from"], instruction["z_to"] + 1):
                    grid[x, y, z] = 1 if instruction["state"] == "on" else 0
    
    return sum(1 for v in grid.values() if v == 1)


def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip().split('\n')

    # parse input into a list of dictionaries
    # each dictionary is one line of the input file
    # has the form of 
    # { state: stateValue, x_from: x_fromValue, x_to: x_toValue,
    #   y_from: y_fromValue, y_to: y_toValue, z_from: z_fromValue, z_to: z_toValue }
    instructions = []
    for instr in input:
        instruction = {}
        instruction["state"] = instr[:3].strip()
        for coordinate in instr[3:].strip().split(','):
            bounds = coordinate.split('..')
            instruction[bounds[0][0] + "_from"] = int(bounds[0][2:])
            instruction[bounds[0][0] + "_to"] = int(bounds[1])
        instructions.append(instruction)
    
    print("Part 1:", day22_part1(instructions))

if __name__ == "__main__":
    main()