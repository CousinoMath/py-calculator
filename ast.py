from abc import ABC, abstractmethod
import math


class AstNode(ABC):
    @abstractmethod
    def evaluate(self, memory):
        pass

    @abstractmethod
    def __str__(self):
        pass


class AstNumber(AstNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self, memory):
        return self.value

    def __str__(self):
        return str(self.value)


class AstVariable(AstNode):
    def __init__(self, name):
        self.name = name

    def evaluate(self, memory):
        if self.name in memory:
            return memory[self.name]
        else:
            return 0

    def __str__(self):
        return self.name


class AstPlus(AstNode):
    def __init__(self, *arguments):
        self.arguments = arguments

    def evaluate(self, memory):
        total = 0
        for arg in self.arguments:
            total += arg.evaluate(memory)
        return total

    def __str__(self):
        return '(+ ' + ' '.join(map(str, self.arguments)) + ')'


class AstTimes(AstNode):
    def __init__(self, *arguments):
        self.arguments = arguments

    def evaluate(self, memory):
        product = 1
        for arg in self.arguments:
            product *= arg.evaluate(memory)
        return product

    def __str__(self):
        return '(* ' + ' '.join(map(str, self.arguments)) + ')'


class AstPower(AstNode):
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp

    def evaluate(self, memory):
        bvalue = self.base.evaluate(memory)
        evalue = self.exp.evaluate(memory)
        return bvalue**evalue

    def __str__(self):
        return '(^ ' + str(self.base) + ' ' + str(self.exp) + ')'

class AstAssign(AstNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, memory):
        memory[self.name] = self.value.evaluate(memory)
        return memory[self.name]

    def __str__(self):
        return '(= ' + self.name + ' ' + str(self.value) + ')'

class AstFunction(AstNode):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def evaluate(self, memory):
        return self.func(self.arg.evaluate(memory))

    def __str__(self):
        return '(' + str(self.func) + ' ' + str(self.arg) + ')'

class AstConstant(AstNode):
    def __init__(self, name):
        self.name = name

    def evaluate(self, memory):
        if self.name == 'pi':
            return math.pi
        elif self.name == 'e':
            return math.e
        else:
            return 0

    def __str__(self):
        return self.name
