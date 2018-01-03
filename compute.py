#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade
import sys
import re

def parser(string):
	original = string.lstrip()

	#looking for unauthorized characters (lexical errors)
	regex = r"([^0-9x.*^ +=-]+)"
	p = re.search(regex, string, re.I)
	if p != None:
		exit_error("unkown string(s)  " + ', '.join("'" + x + "'" for x in re.findall(regex, string, re.I)) + \
			" in the argument", string, regex)

	#looking for the right number of '=' (start of syntax errors)
	if string.count("=") != 1:
		exit_error("the argument is not an equation", string, r"=")

	#split each side, then split on +- (except first one)
	split = string.split('=')
	left = re.sub(r"(?<=.)-", "+-", split[0].strip()).split('+')
	right = re.sub(r"(?<=.)-", "+-", split[1].strip()).split('+')

	#looking for blanks
	if (len(left) == 1 and ' '.join(left[0].split()) == ''):
		del left[0]
		exit_error("equation left side is blank", "_" + original, r"_")
	if (len( right) == 1 and ' '.join(right[0].split()) == ''):
		del right[0]
		exit_error("equation right side is blank", original + "_", r"_")

	#check format for each side
	regex = r"^\s*-?\s*[0-9]*\s*\.?\s*[0-9]*\s*\*?\s*(x?$|x\s*\^\s*[0-9]+)\s*"
	for s in left:
		s = s.strip()
		if (not s or s == '-'):
			exit_error("equation left side has a blank after a +/-", original, "", s)
		p = re.match(regex, s, re.I)
		if p == None:
			exit_error("syntax error  " + s, original, "", s)
	for s in right:
		s = s.strip()
		if (not s or s == '-'):
			exit_error("equation right side has a blank after a +/-", original, "", s)
		p = re.match(regex, s, re.I)
		if p == None:
			exit_error("syntax error  " + s, original, "", s)
	

	#if at last one error and not in test, prog quits
	if (exit_error.status == True and __name__ == "__main__"):
		exit_error("")

	#format each side
	left = [s.upper().replace(' ', '').replace('*', '').replace('^', '') for s in left]
	right = [s.upper().replace(' ', '').replace('*', '').replace('^', '') for s in right]

	return(left, right)

def reduced_eq(split_eq):
	print split_eq[0]
	print split_eq[1]
	
	return(3)

def computorv1(string):
	exit_error.status = False
	split_eq = parser(string)
	if (exit_error.status == True):
		return
	degree = reduced_eq(split_eq)
	print "Polynomial degree: " + str(degree)
	if (degree > 2):
		print("The polynomial degree is strictly greater than 2, I can't solve.")
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
		print("Error: " + error_mes + (('\n' + str_color) if (str_color != "") else ""))
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