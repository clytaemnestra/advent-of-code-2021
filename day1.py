import csv 

depth = []
depths = []
counter = 0 

with open('./data/day1.csv', newline = '') as csvfile:
    reader = list(csv.reader(csvfile, delimiter = ' '))

    for i in reader:
        k = int(', '.join(i)) 
        depths.append(k)
    for n in range(1, len(depths)-1):
        if depths[n] > depths[n - 1]:
            counter += 1

print(counter)