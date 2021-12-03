```python
    for n in range(0, len(depths)-2):
        sum = depths[n] + depths[n+1] + depths[n+2]
        sums.append(sum)
    for j in range(0, len(sums)-1):
        if sums[j] < sums[j+1]:
            count_depth_triples += 1
```
se dá napsat jako: 
```python
for n in range(len(measurements) - 3):
    if sum(measurements[n+1:n+4]) > sum(measurements[n:n+3]):
        increases += 1
```