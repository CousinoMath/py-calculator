from token import *
from ast import *

class ParserError(Exception):
    def __init__(self, message):
        self.message = message

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.length = len(tokens)

    def peek(self, num):
        idx = self.current + num
        if idx < self.length:
            return self.tokens[idx]
        else:
            return self.tokens[-1]

    def assignment(self):
        if self.length > 1:
            if (isinstance(self.peek(0), TokenVariable) and
              isinstance(self.peek(1), TokenEquals)):
                name = self.tokens[0].name
                self.current += 2
                expr = self.expression()
                return AstAssign(name, expr)
        return self.expression()

    def expression(self):
        args = [self.factor()]
        while self.current < self.length:
            currToken = self.peek(0)
            if isinstance(currToken, TokenEOF) or isinstance(currToken, TokenRParen):
                break
            elif isinstance(currToken, TokenPlus):
                self.current += 1
                args.append(self.factor())
            elif isinstance(currToken, TokenMinus):
                self.current += 1
                args.append(AstTimes(AstNumber(-1), self.factor()))
            else:
                self.current += 1
                raise ParserError('Expected a +/- instead of ' + str(currToken))
        if len(args) == 1:
            return args[0]
        else:
            return AstPlus(*args)

    def factor(self):
        args = [self.exponential()]
        while self.current < self.length:
            currToken = self.peek(0)
            if isinstance(currToken, TokenPlus) or isinstance(currToken, TokenMinus) or isinstance(currToken, TokenEOF) or isinstance(currToken, TokenRParen):
                break
            elif isinstance(currToken, TokenStar):
                self.current += 1
                args.append(self.exponential())
            elif isinstance(currToken, TokenSlash):
                self.current += 1
                args.append(AstPower(self.exponential(), AstNumber(-1)))
            else:
                self.current += 1
                raise ParserError('Expexted a * or / instead of ' + str(currToken))
        if len(args) == 1:
            return args[0]
        else:
            return AstTimes(*args)

    def exponential(self):
        args = []
        currToken = self.peek(0)
        if isinstance(currToken, TokenMinus):
          self.current += 1
          args.append(AstTimes(AstNumber(-1), self.exponential()))
        else:
          args.append(self.atom())
        while self.current < self.length:
            currToken = self.peek(0)
            if isinstance(currToken, TokenPlus) or isinstance(currToken, TokenMinus) or isinstance(currToken, TokenStar) or isinstance(currToken, TokenSlash) or isinstance(currToken, TokenEOF) or isinstance(currToken, TokenRParen):
                break
            elif isinstance(currToken, TokenCaret):
                self.current += 1
                currToken = self.peek(0)
                if isinstance(currToken, TokenMinus):
                    self.current += 1
                    args.append(AstTimes(AstNumber(-1), self.exponential()))
                else:
                    args.append(self.atom())
            else:
                self.current += 1
                raise ParserError('Expected a ^ instead of ' + str(currToken))
        if len(args) == 1:
            return args[0]
        else:
            args.reverse()
            result = AstNumber(1)
            for arg in args:
                result = AstPower(arg, result)
            return result

    def atom(self):
        currToken = self.peek(0)
        self.current += 1
        if isinstance(currToken, TokenNumber):
            return AstNumber(currToken.value)
        elif isinstance(currToken, TokenVariable):
            return AstVariable(currToken.name)
        elif isinstance(currToken, TokenConstant):
            return AstConstant(currToken.name)
        elif isinstance(currToken, TokenLParen):
            result = self.expression()
            currToken = self.peek(0)
            self.current += 1
            if not isinstance(currToken, TokenRParen):
                raise ParserError('Unbalanced parenthesis')
            return result
        elif isinstance(currToken, TokenFunction):
            arg = self.atom()
            return AstFunction(currToken.func, arg)
        else:
            raise ParserError('Unexpected token ' + str(currToken))
