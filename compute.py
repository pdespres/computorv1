#!/usr/bin/env python
# espece de encoding: utf-8 putain cong
import sys

def computorv1(polynom):
	sys.exit(42)

def usage():
	print "usage: python %s [-?] [polynomial function]" % sys.argv[0]
	sys.exit(42)

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc not in range(2, 4):
		usage()
	if argc == 3:
		#traitement params
		if 1 != 1:
			print "params a faire"
		else:
			usage()
	computorv1(sys.argv[-1])