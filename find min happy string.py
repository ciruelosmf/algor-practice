aa, bb , cc = 1, 1, 7




import heapq


g = ["a" for a in range(1)] + ["b" for b in range(1)] + ["c" for c in range(7)] 
print(g)



def find_min_happy_string(a_times,b_times,c_times):
    res, max_heap = "", []

    for count, char in [(-a_times, "a"),(-b_times, "b"),(-c_times, "c")]:
            #print(count, char)
            if count != 0:
                    heapq.heappush(max_heap, (count, char))
    print(max_heap)
    while max_heap:
            count, char = heapq.heappop(max_heap)
            print(count, char)
            print(res)
            
            if len(res) > 1 and res[-1] == res[-2] == char:
                    
                    
                    if not max_heap:
                            break
                    count2, char2 = heapq.heappop(max_heap)
                    res += char2
                    count2 += 1
                    if count2:
                            heapq.heappush(max_heap, (count2, char2))
            else:
                    res += char
                    count += 1
            if count:
                heapq.heappush(max_heap, (count, char))
    return res
    




find = find_min_happy_string(aa,bb,cc)



print(find)
