noi = int(input())

for _ in range(noi):
    _ = input()
    qs = {
        "START38": 0,
        "LTIME108": 0,
    }
    
    for q in input().split():
        qs[q] += 1

    print(qs["START38"], qs["LTIME108"])