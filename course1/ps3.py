"""
This is not correct, I am unsure why.
"""
import random
count = 0

def partition(A, l, r, pivot):
    A[l], A[pivot] = A[pivot], A[l]

    p = A[l]
    i = l + 1
    for j in range(l + 1, r):
        global count
        count += 1
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[l], A[i-1] = A[i - 1], A[l]
    return i

def _quicksort(A, l, r, choosePivot=None):
    if choosePivot is None:
        choosePivot = lambda A, l, r: l
    if r - l <= 1:
        return 0
    pivot = choosePivot(A, l, r)
    p = partition(A, l, r, pivot)
    cnt1 = _quicksort(A, l, p - 1)
    cnt2 = _quicksort(A, p, r)

    return cnt1 + cnt2 + (r - l - 1)

def quicksort(A, choosePivot=None):
    return _quicksort(A, 0, len(A), choosePivot)

"""with open('ps2.txt') as f:
    inp = list(map(int, f))
    print(quicksort(inp, choosePivot=lambda A, l, r: random.randrange(l, r)))"""

A = [3, 2, 1, 4, 5]
print(quicksort(A))
print(count)
