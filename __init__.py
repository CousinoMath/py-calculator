from lexer import Lexer
from parser import Parser
import ast

if __name__ == '__main__':
    cont = True
    memory = dict()
    while cont:
        source = input('> ').strip()
        cont = source != ''
        if cont:
            tokens = Lexer(source).lex()
            print(list(map(str, tokens)))
            ast = Parser(tokens).assignment()
            print(str(ast))
            value = ast.evaluate(memory)
            print(str(value))

