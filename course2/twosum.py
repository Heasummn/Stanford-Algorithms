"""
I don't like this implementation, because it does not make use of hashing, and is O(n^2) if our numbers are not distributed evenly.
"""
def two_sum(nums, t):
    head = 0
    tail = len(nums) - 1
    # iterate over sorted array using two pointers
    sums = set()
    while head < tail:
        if nums[head] + nums[tail] < -t:
            head += 1
        elif nums[head] + nums[tail] > t:
            tail -= 1
        else: # when we're in range, keep finding sums until we're out of range
            inner_head = head
            two_sum = nums[head] + nums[tail]
            while two_sum >= -t and two_sum <= t:
                sums.add(two_sum)
                inner_head += 1
                two_sum = nums[inner_head] + nums[tail]
            tail -= 1
    return len(sums)




def alg(file):
    with open(file) as f:
        inp = sorted(list(set(map(int, f.readlines()))))
        return two_sum(inp, 10000)