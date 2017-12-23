#!/usr/bin/env python
# espece de encoding: utf-8 putain cong
import sys

def parser(string):
	return("test_error")

def computorv1(string):
	error_mes = parser(string)
	if error_mes != "":
		sys.exit(error_mes)
	return

def usage():
	print "usage: python %s [-?] [polynomial function]" % sys.argv[0]
	sys.exit()

def exit_error(error_mes):
	if error_mes != "":
		sys.exit(error_mes)
	else
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