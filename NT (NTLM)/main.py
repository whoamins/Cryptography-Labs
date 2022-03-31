import hashlib
import sys

hash = hashlib.new('md4', sys.argv[1].encode('utf-16le')).hexdigest()

print(hash)
