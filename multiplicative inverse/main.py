import sys

# g * d = 1 mod p

print(pow(int(sys.argv[1]), -1, int(sys.argv[3])))