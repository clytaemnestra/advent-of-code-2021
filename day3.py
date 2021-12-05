from typing import final


# bits = [bit.strip('\n') for bit in open('data/day3.csv')]

bits = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

gamma = []

for position in range(len(bits[0])):
    zeros = 0
    ones = 0
    for bit in bits:
        if bit[position] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma.append(0)
    elif zeros < ones:
        gamma.append(1)

epsilon = []

for g in gamma: 
    if g == 0:
        epsilon.append(1)
    else:
        epsilon.append(0)
    
decimal_gamma = int(''.join(map(str, gamma)), 2)
decimal_epsilon = int(''.join(map(str, epsilon)), 2)

print("Consumption: ", decimal_gamma * decimal_epsilon)
