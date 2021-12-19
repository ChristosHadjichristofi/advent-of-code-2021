def do_step(position, velocity):
    upd_position = (position[0] + velocity[0], position[1] + velocity[1])
    upd_velocity = None

    if velocity[0] > 0:
        upd_velocity = (velocity[0] - 1, velocity[1] - 1)
    else:
        upd_velocity = (velocity[0], velocity[1] - 1)
    
    return (upd_position, upd_velocity)

def is_inbounds(position, target):
    return (target[0][0] <= position[0] <= target[0][1]) and (target[1][0] <= position[1] <= target[1][1])

def is_past(position, target):
    return position[0] > target[0][1] or position[1] < target[1][0]

def in_probe(velocity, target):
    position = (0, 0)
    while not is_past(position, target):
        if is_inbounds(position, target):
            return True
        
        position, velocity = do_step(position, velocity)

def find_distinct_ans(target):
    ans = 0
    y_vel = abs(target[1][0])

    while y_vel >= target[1][0]:
        for x_vel in range (0, target[0][1] + 1):
            if in_probe((x_vel, y_vel), target):
                ans += 1
        y_vel -= 1
    
    return ans
                
def main():
    with open('input.txt', 'r') as f:
        input = f.read().strip()

    input = input[len("target area: x="):].split(', y=')
    
    x_target = list(map(int, input[0].split('..')))
    y_target = list(map(int, input[1].split('..')))

    target = (x_target, y_target)

    print("Part 1:", y_target[0] * (y_target[0] + 1) //  2)
    print("Part 2:", find_distinct_ans(target))

if __name__ == "__main__":
    main()