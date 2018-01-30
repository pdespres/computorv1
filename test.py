#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

import computor

lib = [
"caracteres inconnus",
"plusieurs '='",
"equation incomplete",
"equation incomplete 2",
"mauvaise syntaxe",

"mauvaise syntaxe 2",
"manque exposant",
"exposant neg",
"exposant non entier",
"degree 3+",

"degree 0 no solution",
"degree 0 all solutions",
"degree 1 + fraction",
"degree 2 discriminant < 0 + pgcd",
"degree 2 discriminant = 0",

"degree 2 discriminant > 0"
]

test = [
"a1xsd¨^4=gddd xz",
"5 * X^0 + 4 * X^1 = - 9.3 * X^2 = 1 * X^0",
"4 * X = ",
"5 * X^0 + 4 * X^1 = 5 * X^0 + 4 * X^1 + ",
"5 *** x^1 = 0",

"5 * X^0 + 4.3.2 * X^1 = 5 * X^0 + 4..16 * X^1",
"5 * X^0 + 4 * X^1 - 9.3 * X^ = 1 * X^0",
"8 * X^-4 - 9.3 * X^2 = 1 * X^0",
"8 * X^4 - 9.3 * X^2.1 +x^4= 1 * X^0",
"8 * X^4 - 9 * X^2 + 6 +x^4= 1 * X^0 + X^6",

"- 9.3 = 1 * X^0",
"7 + X = 7 + X",
" -5 + 4X = -1 +X",
"3 x^2 + 5x + 7 = 0",
"4x^2 + 4x + 1 = 0",

"2x^2 + 9x = 5"
]

i = 0
for s in test:
	print ""
	print lib[i]
	print "Equation:\t", s
	i += 1
	computor.computorv1(s, 13)