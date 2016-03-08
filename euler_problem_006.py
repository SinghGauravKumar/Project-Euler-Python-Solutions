

def compute():
	x = sum(i for i in range(1, 101))**2
	y = sum(i**2 for i in range(1, 101))
	return str(x - y)


if __name__ == "__main__":
	print(compute())
