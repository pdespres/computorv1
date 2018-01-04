#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

import computor

lib = [
"caracteres en plus",
"plusieurs =",
"mauvaise syntaxe",
"equation incomplete",
"equation incomplete 2",
"mauvaise syntaxe 2",
"manque exposant",
"exposant neg",
"exposant non entier",
"puissance 3+",
"ok 1",
"naturel"
]

test = [
"a1xsd¨^4=gddd xz",
"5 * X^0 + 4 * X^1 = - 9.3 * X^2 = 1 * X^0",
"5 *** x^1 = 0",
"4 * X = ",
"5 * X^0 + 4 * X^1 = 5 * X^0 + 4 * X^1 + ",
"5 * X^0 + 4.3.2 * X^1 = 5 * X^0 + 4..16 * X^1",
"5 * X^0 + 4 * X^1 - 9.3 * X^ = 1 * X^0",
"8 * X^-4 - 9.3 * X^2 = 1 * X^0",
"8 * X^4 - 9.3 * X^2.1 +x^4= 1 * X^0",
"8 * X^4 - 9.3 * X^2 + 6 +x^4= 1 * X^0 + X^6",
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
" -5 + 4X + X^2 -9.3X^2 = -1 +X"
]

i = 0
for s in test:
	print ""
	print lib[i]
	print "Equation: ", s
	i += 1
	computor.computorv1(s, 1)