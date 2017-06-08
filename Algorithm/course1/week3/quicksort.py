def readFile():
    data = []
    with open('data.txt', 'r') as f:
        for l in f.readlines():
            data = list(map(int, l.split()))
    return data


def quickSort(Alist,low,high):
	if(high - low < 2):
		return 0
	pivot = Alist[low]
	i = low
	j = low + 1
	while(j < high and i < high ):
		if( Alist[j] < pivot ):
			temp = Alist[i+1]
			Alist[i+1] = Alist[j]
			Alist[j] = temp
			i += 1
			j += 1
		else:
			j += 1
	temp = Alist[i]
	Alist[i] = Alist[low]
	Alist[low] = temp
	a = quickSort(Alist,low,i)
	b = quickSort(Alist,i+1,high)

	return (high - low - 1) + a + b



Alist = readFile()
a = quickSort(Alist,0,len(Alist))
print (a)
