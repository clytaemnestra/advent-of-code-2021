import csv 

depths = []
count_depth = 0 
count_depth_triples = 0
sums = []

with open('./data/day1.csv', newline = '') as csvfile:
    reader = list(csv.reader(csvfile, delimiter = ' '))

    for i in reader:
        k = int(', '.join(i)) 
        depths.append(k)
    for n in range(1, len(depths)-1):
        if depths[n] > depths[n - 1]:
            count_depth += 1
    for n in range(0, len(depths)-2):
        sum = depths[n] + depths[n+1] + depths[n+2]
        sums.append(sum)
    for j in range(0, len(sums)-1):
        if sums[j] < sums[j+1]:
            count_depth_triples += 1

print(count_depth)
print(count_depth_triples)