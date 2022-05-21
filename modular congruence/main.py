import sys


# a = b mod c
# b = a mod c

a = int(sys.argv[1])
c = int(sys.argv[2])

b = a % c

if b % c == b:
	print(b)
