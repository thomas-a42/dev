from math import sqrt


class Equation:

  def __init__(self):
    self.a = 0
    self.b = 0
    self.c = 0
    self.delta = 0
    self.possibleXValues = 0
    self.x1 = 0
    self.x2 = 0

  def findDelta(self):
    self.delta = (self.b**2) - (4 * self.a * self.c)
    print(self.delta)

  def validateNumberOfPossibilities(self):
    if self.delta < 0:
      return 0
    elif self.delta == 0:
      return 1
    return 2

  def findX1(self):
    self.x1 = (-self.b + sqrt(self.delta)) / (2 * self.a)
    return self.x1

  def findX2(self):
    self.x2 = (-self.b - sqrt(self.delta)) / (2 * self.a)
    return self.x2


equation1 = Equation()

equation1.a = float(input('Digite o valor do primeiro termo (a): '))
equation1.b = float(input('Digite o valor do segundo termo (b): '))
equation1.c = float(input('Digite o valor do terceiro termo (c): '))

equation1.findDelta()

equation1.possibleXValues = equation1.validateNumberOfPossibilities()

if equation1.possibleXValues == 0:
  print('Não há raízes reais para essa equação.')
elif equation1.possibleXValues == 1:
  print(f'A única raíz para essa equação é {equation1.findX1()}')
elif equation1.possibleXValues == 2:
  print(f'As raízes possíveis para essa equação são {equation1.findX1()} e {equation1.findX2()}')