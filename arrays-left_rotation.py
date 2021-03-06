"""
A left rotation operation on an array of size n shifts each of the array's
elements 1 unit to the left. For example, if 2 left rotations are performed on
array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

Given an array of n integers and a number, d, perform d left rotations on the
array. Then print the updated array as a single line of space-separated integers.

"""


def array_left_rotation(a, n, k):
    for i in range(k):
        new = a.pop(0)
        a.append(new)

    for i in range(n):
        print a[i],
