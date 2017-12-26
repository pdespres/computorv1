#!/usr/bin/env python
# waloo le encoding: utf-8 de malade
import sys
import re

def parser(string):
	string = string.replace(' ', '').replace('*', '')
	regex = r"(^[0-9xX^+=-]+$)"
	if not re.match(regex, string):
		exit_error("Unknown character in polynomial function")
	
	return("")

def computorv1(string):
	parser(string)
	return

def usage():
	print "usage: python %s [-?] [polynomial function]" % sys.argv[0]
	sys.exit(0)

def exit_error(error_mes):
	if error_mes != "":
		sys.exit(error_mes)
	else:
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