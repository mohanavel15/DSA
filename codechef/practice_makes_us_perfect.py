solved = [int(x) for x in input().split()]
above10 = 0

for i in solved:
    if i >= 10:
        above10 += 1

print(above10)