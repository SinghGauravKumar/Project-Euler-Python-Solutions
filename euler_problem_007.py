
import eulerlib, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter


def compute():
	ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
	return str(ans)


if __name__ == "__main__":
	print(compute())
