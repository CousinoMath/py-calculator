from token import *

class LexerError(Exception):
    def __init__(self, message):
        self.message = message

class Lexer:
    def __init__(self, string):
        self.source = string
        self.start = 0
        self.current = 0
        self.tokens = []
        self.length = len(string)

    def skipWhitespace(self):
        while self.source[self.start].isspace() and self.start < self.length:
            self.current += 1
            self.start = self.current

    def lex(self):
        while self.start < self.length:
            self.skipWhitespace()
            start = self.source[self.start]
            if start == '+':
                self.current += 1
                self.tokens.append(TokenPlus())
            elif start == '-':
                self.current += 1
                self.tokens.append(TokenMinus())
            elif start == '*':
                self.current += 1
                self.tokens.append(TokenStar())
            elif start == '/':
                self.current += 1
                self.tokens.append(TokenSlash())
            elif start == '^':
                self.current += 1
                self.tokens.append(TokenCaret())
            elif start == '=':
                self.current += 1
                self.tokens.append(TokenEquals())
            elif start == '(':
                self.current += 1
                self.tokens.append(TokenLParen())
            elif start == ')':
                self.current += 1
                self.tokens.append(TokenRParen())
            elif start.isdigit() or start == '.':
                self.current += 1
                self.tokens.append(TokenNumber(self.parseNumber()))
            elif start.isalpha():
                self.current += 1
                self.tokens.append(classifyIdentifier(self.parseIdentifier()))
            else:
                self.current += 1
                raise LexerError("Unrecognized token " + start)
            self.start = self.current
        self.tokens.append(TokenEOF())
        return self.tokens

    def parseNumber(self):
        if self.current < self.length:
            current = self.source[self.current]
            while self.current < self.length and (current.isdigit()
              or current == '.'):
                self.current += 1
                if self.current < self.length:
                    current = self.source[self.current]
        return float(self.source[self.start:self.current])

    def parseIdentifier(self):
        if self.current < self.length:
            current = self.source[self.current]
            while self.current < self.length and current.isalnum():
                self.current += 1
                if self.current < self.length:
                    current = self.source[self.current] 
        return self.source[self.start:self.current]
