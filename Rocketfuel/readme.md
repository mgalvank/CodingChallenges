'''''''''
  Rocket Fuel Problem: Given a deque that supports only push_front,
  push_back and pop_back, we want to push the values from 1 to N
  into the deque in sorted order, and pop them out too. We can do
  pop_back at any time. If we are given a permutation of 1~N, how
  can we push and pop elements so that the elements that are popped
  out will be in the order of the given permutation?

  For example, suppose N = 5, and pop-out order is { 2, 3, 1, 4, 5 },
  the operations required should be:

    push back 1
    push back 2
    pop back 2
    push back 3
    pop back 3
    pop back 1
    push back 4
    pop back 4
    push back 5
    pop back 5

  To solve this problem, we maintain a deque of ranges, and initialize
  the expected value to 1. Then we scan the  input pop order array from
  left to right.
  Suppose the current element is x and x > expected_value,
  we push range 1~1 to the deque, and push 2~(x-1) to both front and back
  sides of the deque. The corresponding sequences will be to push 2~(x-1),
  but we do not know whether it is push_back or push_front yet.

  If x == expected_value, we simply push_back and pop_back x;

  If x < expected_value, we keep popping back the ranges in the deque,
  until either the deque is empty, or the last range in the deque covers
  x. Then we pop_back x, and change the last range's upper limit. If last
  range is descending from left to right, then x was push_back-ed into the
  deque; otherwise x was push_front-ed into the deque.

  If we popped out all ranges but couldn't find any range that covers x,
  then the input pop list is not valid.

  Note that the operations may not be unique. For example, if pop order is
  { 1, 2 }, we have the following two approaches:

  #1: Always pop back the element when it is ready.
       push back 1
            pop back 1
       push back 2
            pop back 2

  #2: When an element is ready for opo back, hold it and keep pushing
 & elements to the front.
       push back  1
       push front 2
            pop back 1
            pop back 2

  But in the algorithm above, if input pop list has a valid solution
  in #2, then it must have a valid solution in approach #1, because
  in #2, the new elements are only added to the front side, but in #1,
  we consider adding new elements on both front and back sides.


'''''

