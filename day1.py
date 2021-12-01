import csv 

depth = []
depths = []

with open('./data/day1.csv', newline = '') as csvfile:
    reader = list(csv.reader(csvfile, delimiter = ' '))

    for i in reader:
        k = int(', '.join(i)) 
        depths.append(k)
    print(len(depths))
    for n in range(1, len(depths)-1):
        if depths[n] < depths[n - 1]:
        # print(reader)
            depth.append('decrease')
        else:
            depth.append('increase')

#print(depth)
print(depth)

counter = 0 
for m in depth:
    if m == 'increase':
        counter += 1
print(counter)
