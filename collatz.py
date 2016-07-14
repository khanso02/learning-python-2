def collatzconjecture(n, i=0):
	

	if n<=1:
		return i
	if n%2==0:
		return collatzconjecture(n/2, i +1)
	else:
		return collatzconjecture((n*3)+1, i + 1)

print collatzconjecture(6)