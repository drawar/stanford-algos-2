
minQ = []
maxQ = []
heapq.heappush(minQ, -7)
heapq.heappush(minQ, -4)
heapq.heappush(minQ, -5)

while minQ:
    print(-heapq.heappop(minQ))