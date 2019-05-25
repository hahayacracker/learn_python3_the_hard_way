def print_two(*args):
	arg1, arg2 = args
	print('arg1:%r, arg2:%r'%(arg1, arg2))


def print_two_again(*args):
	arg1, arg2 = args
	print('arg1:%r, arg2:%r'%(arg1, arg2))

def print_one(arg1):
	print('arg1: %r'%arg1)


def print_none():
	print('I got nothing')


if __name__ == '__main__':
	print_one('hahaya')
	print_none()
	print_two('hahaya','后续')
	print_two_again('hahaya','后续')