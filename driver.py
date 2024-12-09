import sys
from antlr4 import *
from D1Lexer import D1Lexer
from D1Parser import D1Parser

def main(argv):
    if len(sys.argv) > 1:
        inp = FileStream(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <filename>")
        return
    counter = 0
    lexer = D1Lexer(inp)
    tokens = CommonTokenStream(lexer)
    parser = D1Parser(tokens)
    tree = parser.start()
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"Parse error on line {counter}")
        print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)