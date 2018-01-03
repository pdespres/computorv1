#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade
import sys
import re

def parser(string):
	original = string

	#looking for unauthorized characters (lexical errors)
	regex = r"([^0-9x.*^ +=-]+)"
	p = re.search(regex, string, re.I)
	if p != None:
		exit_error("unkown string(s) " + ', '.join("'" + x + "'" for x in re.findall(regex, string, re.I)) + \
			" in the argument", string, regex)

	#looking for the right number of '=' (start of syntax errors)
	if string.count("=") != 1:
		exit_error("the argument is not an equation", string, r"=")

	#split each side, then split on +- (except first one)
	#string = string.lower().replace(' ', '')
	split = string.split('=')
	left = re.sub(r"(?<=.)-", "+-", split[0]).split('+')
	right = re.sub(r"(?<=.)-", "+-", split[1]).split('+')

	#looking for blanks
	if (len(left) == 1 and ' '.join(left[0].split()) == ''):
		exit_error("equation left side is blank", "_" + original, r"_")
	if (len( right) == 1 and ' '.join(right[0].split()) == ''):
		exit_error("equation right side is blank", original + "_", r"_")

	#check format for each side
	regex = r"^\s*-?\s*[0-9]*\s*\.?\s*[0-9]*\s*\*?\s*(x?$|x\s*\^\s*[0-9]+)\s*"
	for s in left:
		if (not s.strip() or s.strip() == '-'):
			exit_error("equation left side has a blank after a +/-")
		p = re.match(regex, s, re.I)
		if p == None:
			s = s.strip()
			exit_error("syntax error " + s, original, "", s)
		s = s.replace('*', '').replace('^', '')
	for s in right:
		if (not s or s == '-'):
			exit_error("equation right side has a blank after a +/-")
		p = re.match(regex, s, re.I)
		if p == None:
			s = s.strip()
			exit_error("syntax error " + s, original, "", s)
		s = s.replace('*', '').replace('^', '')

	#if at last one error and not in test, prog quits
	if (exit_error.status == True and __name__ == "__main__"):
		exit_error("")

	return(left, right)

def computorv1(string):
	split_eq = parser(string)
	print split_eq[0]
	print split_eq[1]
	return

def usage():
	print "usage: python %s [-?] [polynomial equation]" % sys.argv[0]
	sys.exit(0)

def exit_error(error_mes, string, regex, find = ""):
	exit_error.status = True
	offset = 0
	str_color = ""
	if (regex != ""):
		for m in re.finditer(regex, string, re.I):
			str_color += string[offset:m.start()] + "\033[7;31m" + m.group(0) + "\033[0m"
			offset = m.end()
		str_color += string[offset:]
	elif (find != ""):
		str_color = string.replace(find, "\033[7;31m" + find + "\033[0m")
	if error_mes != "":
		print("Error: " + str_color + "  " + error_mes)
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
	else:
		computorv1(sys.argv[-1])