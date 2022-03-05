do = {0: [], 1: [], 2: [], 3: [[6,4]], 4: []}
for neiCost, nei in do[3]:
    7
    #print(neiCost, nei,4,do)
po = [[0,0],[2,2],[3,10],[5,2],[7,0]]

import heapq


d =[[7, 3], [7, 4], [13, 2], [9, 2]]
print(d)

#heapq.heapify(d)

heapq.heappush(d, [3, 3])
print(d)



def min_cost_connect_points(pointss):
    N = len(pointss)

    adj = {i:[] for i in range(N)}   # [cost , node]
    print(adj)
    for i in range(N):
        x1, y1 = pointss[i]
        for j in range(i+1, N):
            x2, y2 = pointss[j]
            dist = abs(x1-x2) + abs(y1-y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    print("")
    print(adj[0])
    print(adj[1])
    print(adj[2])
    print(adj[3])
    print(adj[4])
    res = 0
    visited = set()
    minH = [[0,0]]   # [cost , point]
    while len(visited) < N:
        cost, i = heapq.heappop(minH)
        print("----")
        print(cost, i,"cost, i")
        if i in visited:
            continue
        res += cost
        visited.add(i)
        print(visited,"visited")
        for neiCost, nei in adj[i]:
            print("")
        
            print("")
            print(neiCost, nei,"neiCost, nei")
            if nei not in visited:
                print(minH)
                print("heapq.heappushssgshshshsh")
                heapq.heappush(minH, [neiCost, nei])
                print(minH)
    return res


s = min_cost_connect_points(po)
print(s)
