import sys
import os
import pytest

# Load the grammar classes from a grammar/ folder in the root dir
grammarpath = os.path.join(os.path.dirname(__file__), '..', 'grammar')
sys.path.append(grammarpath)

from antlr4 import *
from nintLexer import nintLexer
from nintParser import nintParser

def driver(input_stream):
	lexer = nintLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = nintParser(stream)
	tree = parser.prog()
	return parser.getNumberOfSyntaxErrors()


# Tests
# -----------------------------------------------------------------------------------

def test_a():
	""" Here's what this test does """
	iiss = InputStream('int a = a+b;')
	res = driver(iiss)
	assert res == 0 # There were no (0) errors

# Example of a test that fails:
def test_b():
	""" Docstring goes here """
	iiss = InputStream('a+')
	res = driver(iiss)
	assert res == 0 # There were no (0) errors

