from abc import ABC, abstractmethod
import math

class Token(ABC):
    pass

class TokenPlus(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '+'

class TokenMinus(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '-'

class TokenStar(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '*'

class TokenSlash(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '/'

class TokenCaret(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '^'

class TokenLParen(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '('

class TokenRParen(Token):
    def __init__(self):
        pass

    def __str__(self):
        return ')'

class TokenEquals(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '='

class TokenNumber(Token):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class TokenIdentifier(Token):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class TokenVariable(TokenIdentifier):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class TokenFunction(TokenIdentifier):
    def __init__(self, name):
        super().__init__(name)
        if name == 'acos':
            self.func = math.acos
        elif name == 'asin':
            self.func = math.asin
        elif name == 'atan':
            self.func = math.atan
        elif name == 'cos':
            self.func = math.cos
        elif name == 'sin':
            self.func = math.sin
        elif name == 'tan':
            self.func = math.tan
        else:
            self.func = None

class TokenConstant(TokenIdentifier):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class TokenEOF(Token):
    def __init__(self):
        pass

    def __str__(self):
        return '♣'

def classifyIdentifier(name):
    if name in ('pi', 'e'):
        return TokenConstant(name)
    elif name in ('acos', 'asin', 'atan', 'cos', 'sin', 'tan'):
        return TokenFunction(name)
    else:
        return TokenVariable(name)

