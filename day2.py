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
    else:
        depth -= units

print(horizontal * depth)    
