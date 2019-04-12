import sys
from antlr4 import *
from nintLexer import nintLexer
from nintParser import nintParser
from myListener import nintListener


if len(sys.argv) < 2:
	print("Usage: python driver.py <test_input_file.txt>")
	sys.exit()

def main(argv):
	input_stream = FileStream(argv[1])
	lexer = nintLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = nintParser(stream)
	tree = parser.prog()
	# listen = nintListener()
	# walker = ParseTreeWalker()
	# test = walker.walk(listen, tree)
	# print(tree.s.gen())
	tree.s.gen()
	# print(len(tree.s))

if __name__ == '__main__':
	main(sys.argv)
