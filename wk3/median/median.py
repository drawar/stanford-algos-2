import heapq


class Median:
    def __init__(self, instream):
        self.outstream = []
        minQ = []
        maxQ = []
        for i, num in enumerate(instream):
            if i == 0:
                heapq.heappush(maxQ, -num)
            elif i == 1:
                if -maxQ[0] < num:
                    heapq.heappush(minQ, num)
                else:
                    item = heapq.heappushpop(maxQ, -num)
                    heapq.heappush(minQ, -item)
            else:
                if num <= -maxQ[0]:
                    heapq.heappush(maxQ, -num)
                elif num >= minQ[0]:
                    heapq.heappush(minQ, num)
                else:
                    heapq.heappush(maxQ, -num)
            # balance size
            while len(maxQ) < len(minQ):
                heapq.heappush(maxQ, -heapq.heappop(minQ))

            while len(maxQ) > len(minQ) + 1:
                heapq.heappush(minQ, -heapq.heappop(maxQ))

            self.outstream.append(-maxQ[0])

    def cum_med(self):
        """ Return list of cumulative medians """
        return self.outstream

    def sum_mod(self, mod):
        """ Return sum of all cumulative medians modulo mod """
        return sum(self.outstream) % mod


