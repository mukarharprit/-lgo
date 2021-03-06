import heapq
class median:

    low = []
    high = []
    y = 0

    def main(self):
        file = open('median.txt')
        lines = file.readlines()
        data = map(int,lines)
        medians = []
        for x in data:
            if (len(self.low) == 0):
                heapq.heappush(self.low, -x)
            else:
                m = -self.low[0]
                if x > m:
                    heapq.heappush(self.high, x)
                    if len(self.high) > len(self.low):
                        y = heapq.heappop(self.high)
                        heapq.heappush(self.low, -y)
                else:
                    heapq.heappush(self.low, -x)
                    if len(self.low) - len(self.high) > 1:
                        y = -heapq.heappop(self.low)
                        heapq.heappush(self.high, y)
            median = -self.low[0]
            medians.append(median)
        print (sum(medians) % 10000)

obj = median()
obj.main()
