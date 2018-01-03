#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

import compute

lib = [
"caracteres en plus",
"plusieurs =",
"mauvaise syntaxe",
"equation incomplete",
"equation incomplete 2",
"mauvaise syntaxe 2",
"manque exposant",
"ok 1",
"naturel"
]

test = [
"1xsd¨^4=gddd sz",
"5 * X^0 + 4 * X^1 = - 9.3 * X^2 = 1 * X^0",
"5 *** x^1 = 0",
"4 * X = ",
"5 * X^0 + 4 * X^1 = 5 * X^0 + 4 * X^1 - ",
"5 * X^0 + 4.3.2 * X^1 = 5 * X^0 + 4..16 * X^1",
"5 * X^0 + 4 * X^1 - 9.3 * X^ = 1 * X^0",
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
" -5 + 4X + X^2 -9.3X^2 = -1 +X"
]

i = 0
for s in test:
	print ""
	print lib[i]
	print "Equation: ", s
	i += 1
	compute.computorv1(s)