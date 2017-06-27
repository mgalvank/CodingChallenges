import sys

a = [21, 6, 27,18]
target = 15

min1 = sys.maxint
min2 = sys.maxint

diff1 = sys.maxint - target
diff2 = sys.maxint - target

for i in a:
    diff = abs(i - target)
    if(diff <= diff1):
        min2 = min1
        diff2 = diff1
        diff1 = diff
        min1 = i

    elif(diff > diff1 and diff <= diff2):
        diff2 = diff
        min2 = i

print min1,min2