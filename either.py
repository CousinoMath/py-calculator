from abc import ABC, abstractmethod

class Either(ABC):
  @abstractmethod
  def isLeft(self):
    pass
  @abstractmethod
  def isRight(self):
    pass
  @abstractmethod
  def getLeft(self):
    pass
  @abstractmethod
  def getRight(self):
    pass
  @abstractmethod
  def mapLeft(self, lf):
    pass
  @abstractmethod
  def mapRight(self, rf):
    pass
  @abstractmethod
  def either(self, leftF, rightF):
    pass

class Left(Either):
  def __init__(self, lvalue):
    self.lvalue = lvalue
  def isLeft(self):
    return True
  def isRight(self):
    return False
  def getLeft(self):
    return self.lvalue
  def getRight(self):
    raise Error('Cannot get a right value out of Left.')
  def mapLeft(self, lf):
    return Left(lf(self.lvalue))
  def mapRight(self, rf):
    return Left(self.lvalue)
  def either(self, leftF, rightF):
    return leftF(self.lvalue)

class Right(Either):
  def __init__(self, rvalue):
    self.rvalue = rvalue
  def isLeft(self):
    return False
  def isRight(self):
    return True
  def getLeft(self):
    raise Error('Cannot get a left value out of Right.')
  def getRight(self):
    return self.rvalue
  def mapLeft(self, lf):
    return Right(self.rvalue)
  def mapRight(self, rf):
    return Right(rf(self.rvalue))
  def either(self, leftF, rightF):
    return rightF(self.rvalue)
