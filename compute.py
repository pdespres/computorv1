#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade
import sys
import re

def parser(string):
	string = string.lower().replace(' ', '')
	#rajout coloration syntaxique?
	regex = r"([^0-9x.*^+=-]+)"
	p = re.search(regex, string)
	if p != None:
		exit_error("unkown string(s) " + ', '.join("'" + x + "'" for x in re.findall(regex, string, re.I)) + \
			" in the argument")
	if string.count("=") != 1:
		exit_error("the argument is not an equation")
	regex = r"[*]{2,}"
	p = re.search(regex, string)
	if p != None:
		exit_error("too many '" + p.group(0) + "' in the argument")
	string = string.replace('*', '')
	split = string.split('=')
	left = split[0].replace('-', '+-').split('+')
	right = split[1].replace('-', '+-').split('+')
	if left[0] == '':
		exit_error("equation left side is blank")
	if right[0] == '':
		exit_error("equation right side is blank")
	print left
	print right
	return(left, right)

def computorv1(string):
	split_eq = parser(string)
	return

def usage():
	print "usage: python %s [-?] [polynomial equation]" % sys.argv[0]
	sys.exit(0)

def exit_error(error_mes):
	if error_mes != "":
		#sys.exit("Error: " + error_mes)
		print("Error: " + error_mes)
	else:
		sys.exit(42)

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc not in range(2, 4):
		usage()
	if argc == 3:
		#traitement params
		#if ?:
		#	?
		#else:
			usage()
	if sys.argv[-1].lower() == "-test":
		test = [
		"1xsd¨^4=gddd sz",
		"5 * X^0 + 4 * X^1 = - 9.3 * X^2 = 1 * X^0",
		"5 *** x^1 = 0",
		"4 * X =",
		"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
		]
		for s in test:
			print ""
			print "Equation: ", s
			computorv1(s)
	else:
		computorv1(sys.argv[-1])