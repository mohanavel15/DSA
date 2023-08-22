TotalInputs = int(input())

Inputs = []

for _ in range(TotalInputs):
    Inputs.append(sum([int(i) for i in input().split(" ")]))

Output = 0

for i in Inputs:
    if i >= 2:
        Output += 1

print(Output)
