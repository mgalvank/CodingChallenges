# a = "1,2,3"
#
# for i in a.split(','):
#     print i
#
# b = [int(x) for x in a.split(',')]
# print b
# c = ",".join(str(x) for x in b)
# print c

a = [1,2,3,4,5,1]
del a[:1]
print a