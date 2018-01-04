#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

"""
\033[32musage:	python computor.py [OPTIONS] [polynomial equation]

Supported options:
	-s 		silent		don't show the parsing error messages
	-v 		verbose		show messages about intermediary steps\033[0m
"""

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
		return

	#split each side, then split on +- (except first one and power)
	split = string.split('=')
	left = re.sub(r"(?<!\^)(?<=.)-", "+-", split[0].strip()).split('+')
	right = re.sub(r"(?<!\^)(?<=.)-", "+-", split[1].strip()).split('+')

	#looking for blanks
	if (len(left) == 1 and ' '.join(left[0].split()) == ''):
		del left[0]
		exit_error("equation left side is blank", "_" + original, r"_")
	if (len( right) == 1 and ' '.join(right[0].split()) == ''):
		del right[0]
		exit_error("equation right side is blank", original + "_", r"_")

	#check format for each side
	regex = r"^\s*-?\s*[0-9]*\s*\.?\s*[0-9]*\s*\*?\s*(x?$|x\s*\^\s*[0-9]+)\s*$"
	for s in left:
		s = s.strip()
		if (not s or s == '-'):
			exit_error("equation left side has a blank after a +/-", original, "", s)
		p = re.match(regex, s, re.I)
		if p == None:
			s2 = (s[1:].strip()) if (s[0] == "-") else s
			exit_error("syntax error  " + s2, original, "", s2)
	for s in right:
		s = s.strip()
		if (not s or s == '-'):
			exit_error("equation right side has a blank after a +/-", original, "", s)
		p = re.match(regex, s, re.I)
		if p == None:
			s2 = (s[1:].strip()) if (s[0] == "-") else s
			exit_error("syntax error  " + s2, original, "", s2)

	#if at last one error and not in test, prog quits
	if (exit_error.status == True and __name__ == "__main__"):
		exit_error("")
	return(left, right)

def reduce(split_eq):
	#format each side
	split_eq = [[s.upper().replace(' ', '').replace('*', '').replace('^', '') for s in split] for split in split_eq]

	#calculate every distinct nome in one equation/side
	lst_nome = []
	for index, split in enumerate(split_eq):
		for s in split:
			found = 0
			if s.find('X') >= 0:
				if not s.split('X')[0]:
					d1 = 1.0
				else:
					d1 = float(s.split('X')[0])
				if not s.split('X')[-1]:
					d2 = 1
				else:
					d2 = int(s.split('X')[-1])
			else:
				d1 = float(s)
				d2 = 0
			for index, nome in enumerate(lst_nome):
				if nome[0] == d2:
					found = 1
					nome[1] += (d1 if index == 0 else -d1)
					break
			if not found:
				if index == 0:
					lst_nome.append([d2, d1])
				else:
					lst_nome.append([d2,-d1])

	if params.verbose:
		print_eq(lst_nome)
	#ordering from highest power to lowest
	lst_nome = sorted(lst_nome, reverse=True)
	if params.verbose:
		print_eq(lst_nome)
	return(lst_nome)

def params(param):
	#load params according to the command line options
	params.silent = False
	params.verbose = False
	if param in (1,3):
		params.verbose = True
	if param in (2,3):
		params.silent = True

def computorv1(string, param=0):
	params(param)
	exit_error.status = False
	split_eq = parser(string)
	if (exit_error.status == True):
		return
	reduced_eq = reduce(split_eq)
	degree = reduced_eq[0][0]
	print "Polynomial degree: " + str(degree)
	if (degree > 2):
		print("The polynomial degree is strictly greater than 2, I can't solve.")
	return

def exit_error(error_mes, string, regex, find = ""):
	if params.silent and not exit_error.status:
		print("Error")
	exit_error.status = True
	if params.silent:
		return
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
		print(__doc__)
	elif argc == 3:
		#traitement params
		param = 0
		if (sys.argv[1][0] == '-' and len(sys.argv[1]) in range(2,3)):
			if sys.argv[1].find('v') > 0:
				param += 1
			if sys.argv[1].find('s') > 0:
				param += 2
			if param > 0:
				computorv1(sys.argv[-1], param)
			else:
				print(__doc__)
		else:
			print(__doc__)
	else:
		computorv1(sys.argv[-1])