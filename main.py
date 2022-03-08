import math
class Rat:
    def __init__(self,a,b):
      self.a=a
      self.b=b
      self.reduce()
    def __repr__(self):
      return str(self.a)+"/"+str(self.b)
    def __truediv__(self,other):
      if type(other) == int:
        other = Rat(other,1)
      return Rat((self.a*other.b),(self.b*other.a))
    def __add__(self, other):
      if type(other) == int:
        other = Rat(other,1)
      temp = self.a*other.b
      temp2 = other.a*self.b
      return Rat(temp+temp2,(self.b*other.b))
    def __sub__(self, other):
      if type(other) == int:
        other = Rat(other,1)
      temp = self.a*other.b
      temp2 = other.a*self.b
      return Rat(temp-temp2,(self.b*other.b))
    def __mul__(self, other):
      if type(other) == int:
        other = Rat(other,1)
      return Rat((self.a*other.a),(self.b*other.b))
    def reduce(self):
      reduction_factor = math.gcd(self.a, self.b)
      self.a = self.a//reduction_factor
      self.b = self.b//reduction_factor
      if self.b < 0:
        self.b = abs(self.b)
        self.a = self.a*-1
    def invert(self):
      return Rat(self.b,self.a)
    def __neg__(self):
      return Rat(-1*self.a,self.b)
    def __radd__(self, other):
      return self+other
    def __rsub__(self, other):
      return -self + other
    def __rmul__(self, other):
      return self*other
    def __rtruediv__(self,other):
      return self.invert() * other
    def __float__(self):
      return self.a/self.b
    def __int__(self):
      return self.a//self.b
    def __pow__(self, other):
      return Rat(self.a**other, self.b**other)
def shadowrealm(jimbo):
  t=Rat(jimbo.pop(),1)
  jimbo.reverse()
  for i in jimbo:
    t= (i+(1/t))
  return(t)
def grat():
  t=Rat(1,2)
  n=1000
  for i in range(1,n):
    t = 1+1/t
  return(t)
def main():
  phi = (1 + math.sqrt(5))/2
  print(float(shadowrealm([1]*100))-phi)

  tp2 = Rat(1,2)

if __name__ == "__main__":
  main()