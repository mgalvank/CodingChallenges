# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys


def deque_result(a):
    solution = []
    solution.append('pushBack')
    x = {}
    x[1] = 0
    tracker = []
    tracker.append(1)
    curr = 2
    for i in xrange(0, len(a)):
        temp = a[i]
        while curr < temp:
            solution.append("push")
            x[curr] = len(solution) - 1
            tracker.append(curr)
            curr += 1

        if temp not in x:
            x[temp] = len(solution)
            solution.append("pushBack")
            solution.append("popBack")

        else:
            solution.append("popBack")
            if len(solution[x.get(temp)]) < 5:
                solution[x.get(temp)] += "Back"

            tracker.sort()
            if tracker != []:
                temp2 = tracker.index(temp)
                for j in xrange(temp2, len(tracker)):
                    if len(solution[x.get(tracker[j])]) < 5:
                        solution[x.get(tracker[j])] += "Front"

                # tracker = copy.deepcopy(tracker[:tracker.index(temp)])
                del tracker[temp2:]

        if a[i] == curr:
            curr += 1

    return solution


def verify_result(k):
    d = deque()
    counter = 0
    possible_solution = []
    for i in k:
        if i == "pushBack":
            counter += 1
            d.append(counter)
        elif i == "pushFront":
            counter += 1
            d.extendleft([counter])

        elif i == "popBack":
            possible_solution.append(d.pop())
    return possible_solution


a = sys.stdin.readline()
b = [int(x) for x in a.split(',')]
k = deque_result(b)
x = verify_result(k)
if b == x:
    result = ",".join(str(x) for x in k)
else:
    result = "impossible"
print result