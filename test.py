#!/usr/bin/env python 2.7
# waloo le encoding: utf-8 de malade

import compute

test = [
"1xsd¨^4=gddd sz",
"5 * X^0 + 4 * X^1 = - 9.3 * X^2 = 1 * X^0",
"5 *** x^1 = 0",
"4 * X =",
"5 * X^0 + 4 * X^1 = 5 * X^0 + 4 * X^1 -",
"5 * X^0 + 4.3.2 * X^1 = 5 * X^0 + 4..16 * X^1 -",
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
]

for s in test:
	print ""
	print "Equation: ", s
	compute.computorv1(s)