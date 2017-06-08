def max_independent_set_problem():
	with open("mwis.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	del content[0]
	content = map(int, content)
	a = find_max_is_weight(content)
	print ('max is weight: ' + str (a[-1]))
	s = find_max_is_set(content, a)
	print ('max IS: {0}'.format(s))

def find_max_is_weight(w):
	a = [0] * len(w)
	a[0] = w[0]
	a[1] = w[1]
	for i in range(2, len(w)):
		a[i] = max(a[i-1], a[i-2]+w[i])
	return a

def find_max_is_set(w, a):
	s = []
	i = len(a) - 1
	while i >= 1:
		if a[i-1] >= a[i-2] + w[i]:
			i = i - 1
		else:
			s.append(i+1)
			i = i - 2
	if i >= 0:
		s.append(i+1)
	return s

max_independent_set_problem()
