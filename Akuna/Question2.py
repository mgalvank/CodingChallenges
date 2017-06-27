a = [4,4,4,3,2,4,1,1]
n = 4

for i in set(a):
    if a.count(i) == n:
        b = sorted([x for x in a if x != i])

print b