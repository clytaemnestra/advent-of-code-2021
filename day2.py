positions = [position.strip('\n') for position in open('data/day2.csv')]

horizontal = 0
depth = 0
units = 0

for position in positions:
    units = int(position[-1])
    if "forward" in position:
        horizontal += units
    elif "down" in position:
        depth += units
    # up
    else:
        depth -= units
print(horizontal * depth)    

horizontal = 0
units = 0
aim = 0
depth = 0

for position in positions:
    units = int(position[-1])
    if "forward" in position:
        horizontal += units
        if horizontal != 0:
            depth += aim * units
    elif "down" in position:
        aim += units
    # up
    else:
        aim -= units
print(horizontal * depth) 
