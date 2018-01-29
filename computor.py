#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

"""
\033[32musage:	python computor.py [-svgf] [polynomial equation]

Supported options:
	-s 		silent		don't show the parsing error messages
	-v 		verbose		show intermediary steps
	-g 		graph 		popup window with the equation graph
	-f 		fraction 	display numbers with fractions\033[0m
"""

#TODO fractions

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
		exit_error("","","")
	return(left, right)

def reduce(split_eq):
	reduce.naturalScript = False
	#format each side
	split_eq = [[s.upper().replace(' ', '').replace('*', '').replace('^', '') for s in split] for split in split_eq]
	#calculate every distinct nome in one equation/side
	lst_nome = []
	for i1, split in enumerate(split_eq):
		for s in split:
			found = 0
			if s.find('X') >= 0:
				if not s.split('X')[0]:
					reduce.naturalScript = True
					d1 = 1.0
				else:
					d1 = float(s.split('X')[0])
				if not s.split('X')[-1]:
					reduce.naturalScript = True
					d2 = 1
				else:
					d2 = int(s.split('X')[-1])
			else:
				reduce.naturalScript = True
				d1 = float(s)
				d2 = 0
			for i2, nome in enumerate(lst_nome):
				if nome[0] == d2:
					found = 1
					nome[1] += (d1 if i1 == 0 else -d1)
					if nome[1] == 0:
						del lst_nome[i2]
					break
			if not found and d1 != 0:
				if i1 == 0:
					lst_nome.append([d2, d1])
				else:
					lst_nome.append([d2,-d1])
	if not lst_nome:
		lst_nome.append([0, 0])
	if params.verbose:
		print_eq(lst_nome, " \033[32mgroup nomes:\t")

	#ordering from highest power to lowest
	lst_nome = sorted(lst_nome, reverse=True)
	if params.verbose:
		print_eq(lst_nome," \033[32msorted:\t")

	#calculate pgcd and if exists reduce further the equation
	lst_mult = [s[1] for s in lst_nome]
	if len(lst_mult) > 1:
		p = pgcd(lst_mult[0], lst_mult[1])
		if len(lst_mult) > 2:
			for x in lst_mult[2:]:
				p = pgcd(p, x)
		if p != 1:
			lst_nome = [[s[0], s[1] / p] for s in lst_nome]
			print_eq(lst_nome, " \033[32mpgcd:\t\t")

	return(lst_nome)

def solve(eq, degree):
	x1 = x2 = 0.0
	if degree == 0:
		if eq[0][1] == 0:
			print("The equation is always true, all numbers are solutions.")
		else:
			print("The equation is always false, there is no solution.")
		return (None, None)
	elif degree == 1:
		if len(eq) == 1:
			x1 = x2 = 0
			print("The solution is:\n0")
		else:
			x1 = x2 = (-eq[1][1] / eq[0][1])
			print("The solution is:\n%g" % (-eq[1][1] / eq[0][1]))
	else:
		#calculate the discriminant
		a = b = c = 0
		for s in eq:
			if s[0] == 2:
				a = s[1]
			elif s[0] == 1:
				b = s[1]
			elif s[0] == 0:
				c = s[1]
		discriminant = b**2 - 4 * (a * c)
		if params.verbose:
			print " \033[32mdiscriminant:\t%g\033[0m" % discriminant
		if discriminant > 0:
			x1 = (-b + discriminant**0.5) / (2 * a)
			x2 = (-b + discriminant**0.5) / (2 * a)
			print "Discriminant is strictly positive, the two solutions are:"
			print "%g" % ((-b + discriminant**0.5) / (2 * a))
			print "%g" % ((-b - discriminant**0.5) / (2 * a))
		elif discriminant == 0:
			x1 = x2 = -b / (2 * a)
			print "Discriminant is nul, the solution is:"
			print "%g" % (-b / (2 * a))
		else:
			x1 = (-b / (2 * a))
			x2 = (-b / (2 * a))
			print "Discriminant is strictly negative, the two complex solutions are:"
			print "%g" % (-b / (2 * a)) + " + i " + "%g" % ((-discriminant**05) / (2 * a))
			print "%g" % (-b / (2 * a)) + " - i " + "%g" % ((-discriminant**05) / (2 * a))
	return (x1, x2)

def print_eq(eq, text):
	r = ""
	for s in eq:
		if reduce.naturalScript:
			if s[1] == -1:
				if r != "":
					r += "- "
				else:
					r += "-"
			else:
				if s[1] < 0:
					if r != "":
						r += "- "
					else:
						r += "-"
				else:
					if r != "":
						r += "+ "
			if abs(s[1]) != 1:
				r += "%g" % abs(s[1]) + " "
			if s[0] == 1:
				r += "X "
			elif s[0] != 0:
				r += "X^" + "%g" % s[0] + " "
		else:
			if s[1] < 0:
				if r != "":
					r += "- "
				else:
					r += "-"
				#r += "%g" % abs(s[1]) + " * X^" + "%g" % s[0] + " "
			else:
				if r != "":
					r += "+ "
			r += "%g" % s[1] + " * X^" + "%g" % s[0] + " "
	print text, r[:-1] + " = 0\033[0m"

def pgcd(a,b) :
	if a % 1 > 0 or b % 1 > 0:
		return 1
	while a % b != 0:
		a, b = b, a % b
	return abs(b)

def params(param):
	#load params according to the command line options
	params.silent = False
	params.verbose = False
	params.graph = False
	params.fraction = False
	if param in (1, 3, 5, 7, 9,11,13,15):
		params.verbose = True
	if param in (2, 3, 6, 7,10,11,14,15):
		params.silent = True
	if param in (4, 5, 6, 7,12,13,14,15):
		params.graph = True
	if param in (8, 9,10,11,12,13,14,15):
		params.fraction = True

def computorv1(string, param=0):
	params(param)
	exit_error.status = False
	split_eq = parser(string)
	if (exit_error.status == True):
		return
	reduced_eq = reduce(split_eq)
	print_eq(reduced_eq, "Reduced form:\t")
	degree = reduced_eq[0][0]
	print "Polynomial degree: %g" % degree
	if (degree > 2):
		print("The polynomial degree is strictly greater than 2, I can't solve.")
	else:
		(x1, x2) = solve(reduced_eq, degree)
		if x1 is not None and x2 is not None:
			if params.graph:
				import graph
				formula = ""
				for i, s in enumerate(reduced_eq):
					formula += ("+" if (s[1] > 0 and i > 0) else "") + "%g" % s[1] + \
					("*x" if s[0] > 0 else "") + ("**%g" % s[0] if s[0] > 1 else "")
				x1 -= 10
				x2 += 10
				graph.graph(formula, int(round(x1)), int(round(x2)))
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
		if (sys.argv[1][0] == '-' and len(sys.argv[1]) in range(2,5)):
			if sys.argv[1].find('v') > 0:
				param += 1
			if sys.argv[1].find('s') > 0:
				param += 2
			if sys.argv[1].find('g') > 0:
				param += 4
			if sys.argv[1].find('f') > 0:
				param += 8				
			if param > 0:
				computorv1(sys.argv[-1], param)
			else:
				print(__doc__)
		else:
			print(__doc__)
	else:
		computorv1(sys.argv[-1])