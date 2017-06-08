class inversions:
    def readfile(self,fpath):
        f = open(fpath, 'r')
        lines = f.readlines()
        f.close()
        lines = [int(line) for line in lines]
        return lines
    def invCount(self,arr):
        if len(arr) < 2:
            return 0
        m = int ((len(arr) + 1) / 2)
        left = arr[0:m]
        right = arr[m:]
        return self.invCount(left) + self.invCount(right) + self.merge(arr, left, right);
    def merge(self, arr, left, right):
        i = 0
        j = 0
        count = 0
        while i < len(left) or j < len(right) :
            if i == len(left):
                arr[i+j] = right[j]
                j+=1
            elif j == len(right) :
                arr[i+j] = left[i]
                i+=1
            elif left[i] <= right[j] :
                arr[i+j] = left[i]
                i+=1
            else:
                arr[i+j] = right[j]
                count += len(left)-i
                j+=1
        return count
obj = inversions()
lines = obj.readfile('IntegerArray.txt')
print (obj.invCount(lines))
