def reverse(l):
	if len(l) < 2:
		return l
	else:
		halfL = len(l) // 2
		return reverse(l[halfL:]) + reverse(l[:halfL])

l=[1,'an',345]
print(reverse(l))
