from collections import Counter
from collections import OrderedDict


a = [5,0,1,2,2,2,2,1,0,5,1,1]
b = Counter(a).most_common()

print b
print b[1][0]