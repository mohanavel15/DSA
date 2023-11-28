nor = int(input())

p1 = 0
p2 = 0

p1_max_lead = 0
p2_max_lead = 0

for _ in range(nor):
    scores = [int(x) for x in input().split()]
    
    p1 += scores[0]
    p2 += scores[1]

    if (p1 > p2):
        if p1_max_lead < p1-p2:
            p1_max_lead = p1-p2
    else:
        if p2_max_lead < p2-p1:
            p2_max_lead = p2-p1

if p1_max_lead > p2_max_lead:
    print(1, p1_max_lead)
else:
    print(2, p2_max_lead)