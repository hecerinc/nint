import sys
from antlr4 import *
from grammar.nintLexer import nintLexer
from grammar.nintParser import nintParser
# from myListener import nintListener


if len(sys.argv) < 2:
	print("Usage: python driver.py <test_input_file.txt>")
	sys.exit()

def main(argv):
	input_stream = FileStream(argv[1])
	lexer = nintLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = nintParser(stream)
	result = parser.prog()
	# listen = nintListener()
	# walker = ParseTreeWalker()
	# test = walker.walk(listen, tree)
	# print(tree.s.gen())
	result.s.intercode()
	# print(len(tree.s))

if __name__ == '__main__':
	main(sys.argv)
