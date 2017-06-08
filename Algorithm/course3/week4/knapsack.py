class knapsack:
    def loadData(self,fPath="knapsack.txt"):
        itemList = []

        with open(fPath, 'r') as fileObj:
            lines = fileObj.readlines()
            Capacity, Items = map(int, lines[0].split())
            for line in lines[1:]:
                value, weight = map(int, line.split())
                itemList.append((value, weight))
        return itemList, Capacity, Items


    def optimalSubproblems(self,items, Capacity):
        optArray = [[]]
        for w in range(Capacity+1):
            if items[0][1] <= w:
                optArray[0].append(items[0][0])
            else:
                optArray[0].append(0)
        for i, item in enumerate(items[1:]):
            i = i + 1
            optArray.append([])
            curVal, currW = item

            for w in range(Capacity+1):
                optArray[i].append(optArray[i-1][w])
                if currW > w:
                    continue
                v1 = optArray[i-1][w - currW] + curVal
                v2 = optArray[i-1][w]

                if v1 >= v2:
                    optArray[i][w] = v1

        return optArray


obj = knapsack()
itemList, totalWeight, numItems = obj.loadData()
optArray = obj.optimalSubproblems(itemList, totalWeight)
print(optArray[-1][-1])
