def countSplitInversions(A, B):
    n = len(A) + len(B)
    num_inversions = 0
    output = []
    i = 0
    j = 0

    for k in range(n):
        if i == len(A) or j == len(B):
            break

        if A[i] < B[j]:
            output.append(A[i])
            i += 1
        elif B[j] < A[i]:
            output.append(B[j])
            num_inversions += len(A) - i
            j += 1

    output += A[i:]
    output += B[j:]

    return output, num_inversions

def countInversions(A):
    n = len(A)
    if n == 1:
        return A, 0
    srt1, left = countInversions(A[:n//2])
    srt2, right = countInversions(A[n//2:])
    B, split = countSplitInversions(srt1, srt2)

    return B, left + right + split

#print(countInversions([4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]))

def alg(file):
    with open(file) as f:
        inp = list(map(int, f))
        return countInversions(inp)[1]