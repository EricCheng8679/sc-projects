

def main():
	recursion()


def recursion():
	count = [0]
	num = b(5, 2, count)
	print(num)
	# print(sum(count))
	print(count[0])


def b(n, k, count):
	# count.append(1)  ## count the number of stack frame
	count[0] += 1
	if k == 0 or k == n:
		print('Base Case!')
		return 2
	else:
		return b(n-1, k-1, count) + b(n-1, k, count)


if __name__ == '__main__':
	main()