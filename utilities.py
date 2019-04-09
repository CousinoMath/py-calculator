class OptionError(Error):
  def __init__(self, message):
    self.message = message
    
class Option:
  def isSome(self):
    raise OptionError('Method isSome is not implemented for Option class.')
  def isNone(self):
    raise OptionError('Method isNone is not implemented for Option class.')
  def getValue(self):
    raise OptionError('Method getValue is not implemented for Option class.')
  def getValueOr(self, null):
    raise OptionError('Method getValueOr is not implemented for Option class.')
  def map(self, f):
    raise OptionError('Method map is not implemented for Option class.')
  def flatMap(self, f):
    raise OptionError('Method flatMap is not implemented for Option class.')

class Nothing(Option):
  def isSome(self):
    return False
  def isNone(self):
    return True
  def getValue(self):
    raise OptionError('Cannot get value out of nothing.')
  def getValueOr(self, null):
    return null
  def map(self, f):
    pass
  def flatMap(self, f):
    pass
