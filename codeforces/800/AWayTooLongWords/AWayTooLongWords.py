TotalInputs = int(input())

Inputs = []

for _ in range(TotalInputs):
    Inputs.append(input())

for i in Inputs:
    if len(i) < 10:
        print(i)
    else:
        print(f"{i[0]}{len(i)-2}{i[-1]}")
        