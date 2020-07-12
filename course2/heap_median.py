import heapq
def medians(nums):
    if nums[0] < nums[1]:
        heap_low = [-nums[0]] # we invert the max heap because heapq does not have support for max heaps, but inverting the value is the same result
        heap_high = [nums[1]]
    else:
        heap_low = [-nums[1]]
        heap_high = [nums[0]]
    ans = [nums[0], -heap_low[0]]
    for j, num in enumerate(nums[2:]):
        i = j + 3 # j == 0 => nums[2], i is 1 indexed
        if -num <= heap_low[0]:
            heapq.heappush(heap_high, num)
        elif num < heap_high[0]:
            heapq.heappush(heap_low, -num)
        else:
            print("Yikes")

        if len(heap_high) - 1 > len(heap_low):
            shift = heapq.heappop(heap_high)
            heapq.heappush(heap_low, -shift)
        elif len(heap_low) - 1 > len(heap_high):
            shift = -heapq.heappop(heap_low)
            heapq.heappush(heap_high, shift)

        if i % 2 == 0:
            stat = i / 2
        else:
            stat = (i + 1)/2
        if stat > len(heap_low):
            ans.append(heap_high[0])
        else:
            ans.append(-heap_low[0])
    return sum(ans) % 10000

def alg(file):
    with open(file) as f:
        inp = list(map(int, f.readlines()))
        return medians(inp)
