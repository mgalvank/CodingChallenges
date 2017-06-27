#Sum and average of odd numbers in a list
import math

a = [0,0,0]
count = 0
sum  = 0

for index,i in enumerate(a):

    if index%2 == 0:
        print i
        sum += i
        count += 1


average = math.floor(sum/count)


print "Sum :",sum,"Average :",average