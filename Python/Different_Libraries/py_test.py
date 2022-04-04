import py_test

def inc(x):
	return x + 1


def test_answer():
	assert inc(3) == 5


if __name__ == '__main__':
	py_test.test_answer()