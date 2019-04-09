from abc import ABC, abstractmethod

class Option(ABC):
  @abstractmethod
  def isSome(self):
    pass
  @abstractmethod
  def isNothing(self):
    pass
  @abstractmethod
  def map(self, f):
    pass
  @abstractmethod
  def flatMap(self, f):
    pass
  @abstractmethod
  def option(self, null, f):
    pass
  @abstractmethod
  def getValue(self):
    pass
  @abstractmethod
  def getValueOr(self, null):
    pass


class Nothing(Option):
  def __init__(self):
    pass
  def isSome(self):
    return False
  def isNothing(self):
    return True
  def map(self, f):
    return Nothing()
  def flatMap(self, f):
    return Nothing()
  def option(self, null, f):
    return null
  def getValue(self):
    raise OptionError('Tried to get a value from Nothing.')
  def getValueOr(self, null):
    return null

class Some(Option):
  def __init__(self, value):
    self.value = value
  def isSome(self):
    return True
  def isNothing(self):
    return False
  def map(self, f):
    return Some(f(self.value))
  def flatMap(self, f):
    return f(self.value)
  def option(self, null, f):
    return f(self.value)
  def getValue(self):
    return self.value
  def getValueOr(self, null):
    return self.value
