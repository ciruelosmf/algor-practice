e = [7,1, 4,2,1,5]

kk = 2
import heapq


def klargest(nums_Array, k_int):
    maxHeap = [-int(n) for n in nums_Array]
    heapq.heapify(maxHeap)
    print(maxHeap)
    while k_int > 1:
        print(maxHeap)
        d = heapq.heappop(maxHeap)
        print(maxHeap, "22222222---------")
        k_int -= 1
        print(d)
    return str(-maxHeap[0])

def klargest2(nums_Array, k_int):
    nums_Array.sort()
    ll = len(nums_Array) - k_int
    print(nums_Array)

    return nums_Array[ll]


t = klargest(e, kk)
print(t)

t2 = klargest2(e, kk)
print(t2)    
