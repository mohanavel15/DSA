nots = int(input())

for _ in range(nots):
    noi = int(input())
    dolls = {}
    for _ in range(noi):
        doll = int(input())
        if doll not in dolls:
            dolls[doll] = 1
        else:
            dolls[doll] += 1
    
    for key, value in dolls.items():
        if value % 2 != 0:
            print(key)