from abc import ABC, abstractmethod

class ASTNode(ABC):
  @abstractmethod
  def evaluate(self, **kwargs):
    pass

class Plus(ASTNode):
  def __init__(self, *args):
    self.arguments = list(*args)
  def evaluate(self, **kwargs):
    sum = 0
    for arg in self.arguments:
      sum += arg.evaluate(**kwargs)

class Times(ASTNode):
  def __init__(self, *args):
    self.arguments = list(*args)
  def evaluate(self, **kwargs):
    product = 1
    for arg in self.arguments:
      product *= arg.evaluate(**kwargs)

class Power(ASTNode):
  def __init__(self, base, expon):
    self.base = base
    self.expon = expon
  def evaluate(self, **kwargs):
    baseValue = self.base.evaluate(**kwargs)
    expValue = self.expon.evaluate(**kwargs)
    return baseValue ** expValue

class Number(ASTNode):
  def __init__(self, value):
    self.value = value
  def evaluate(self, **kwargs):
    return self.value

class Variable(ASTNode):
  def __init__(self, name):
    self.name = name
  def evaluate(self, **kwargs):
    if self.name in kwargs:
      return kwargs[self.name]
    else:
      raise Error(f'Unbound variable {self.name}')

class Constant(ASTNode):
  def __init__(self, name):
    if name in list('pi', '\pi'):
      self.value = Math.PI
    elif name in list('e'):
      self.value = Math.E
    else:
      raise Error(f'Unknown constant {name}')
  def evaluate(self, **kwargs):
    return self.value

class Function(ASTNode):
  def __init__(self, func, arg):
    self.func = func
    self.arg = arg
  def evaluate(self, **kwargs):
    argValue = arg.evaluate(**kwargs)
    return self.func(argValue)