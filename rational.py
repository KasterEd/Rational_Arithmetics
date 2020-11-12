def gcd(n1,n2):
    if n1==0 and n2==0 :
        raise ArithmeticError("gcd(0,0) does not exist")
    while n2:
        n1,n2 = n2,n1%n2
    return n1

from numbers import *

class Rational(Number):

    def __init__( self, num, denom ) :
        if not isinstance( num, Integral ) :
            raise TypeError( "Rational: numerator {} must be Integral".format( num ))
        if not isinstance( denom, Integral ) :
            raise TypeError( "Rational: denominator {} must be Integral".format( denom ))
        self. num = num
        self. denom = denom
        self. normalize()

    def normalize(self):
        gcdNum = gcd(self.num,self.denom)
        self.num = self.num//gcdNum
        self.denom = self.denom//gcdNum
        if self.denom < 0:
            self.denom = -1*self.denom

    def __repr__(self):
        return "Rational({},{})".format(self.num,self.denom)

    def __str__(self):
        if self.denom ==1:
            return "Rational({})".format(self.num)
        else:
            return "Rational({},{})".format(self.num,self.denom)

    def __neg__(self):
        return Rational(-1*self.num,self.denom)

    def __add__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator = self.num+other.num*self.denom
            return Rational(numenator,self.denom)
        elif isinstance(other,str):
            raise NotImplementedError
        else: 
            numenator = self.num*other.denom+other.num*self.denom
            denominator = self.denom*other.denom
            return Rational(numenator,denominator)

    def __sub__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator = self.num-other.num*self.denom
            return Rational(numenator,self.denom)
        elif isinstance(other,str):
            raise NotImplementedError
        else: 
            numenator = self.num*other.denom-other.num*self.denom
            denominator = self.denom*other.denom
            return Rational(numenator,denominator)

    def __radd__(self,other):
        other = Rational(other,1)
        numenator = self.num+other.num*self.denom
        return Rational(numenator,self.denom)
    
    def __rsub__(self,other):
        other = Rational(other,1)
        numenator = other.num*self.denom-self.num
        return Rational(numenator,self.denom)
    
    def __mul__(self,other):
        if not isinstance(other,Rational):
            return Rational(other*self.num,self.denom)
        elif isinstance(other,str):
            raise NotImplementedError
        else: 
            return Rational(self.num*other.num,self.denom*other.denom)

    def __truediv__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator = self.num * other.denom
            denominator = self.denom * other.num
            return Rational(numenator,denominator)
        elif isinstance(other,str):
            raise NotImplementedError
        else: 
            numenator = self.num * other.denom
            denominator = self.denom * other.num
            return Rational(numenator,denominator)

    def __rmul__(self,other):
         return Rational(other*self.num,self.denom)

    def __rtruediv__(self,other):
        other = Rational(other,1)
        numenator = self.denom * other.num 
        denominator = self.num * other.denom
        return Rational(numenator,denominator)

    def __eq__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            return self.num == other.num and self.denom == other.denom
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            return self.num == other.num and self.denom == other.denom

    def __ne__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            return self.num != other.num or self.denom != other.denom
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            return self.num != other.num or self.denom != other.denom
    
    def __lt__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator =self.denom*other.num
            return numenator > self.num
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            numenator1 = self.denom*other.num
            numenator2 = self.num * other.denom
            return numenator1 > numenator2

    def __gt__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator =self.denom*other.num
            return numenator < self.num
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            numenator1 = self.denom*other.num
            numenator2 = self.num * other.denom
            return numenator1 < numenator2
    
    def __le__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator =self.denom*other.num
            return numenator >= self.num
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            numenator1 = self.denom*other.num
            numenator2 = self.num * other.denom
            return numenator1 >= numenator2

    def __ge__(self,other):
        if not isinstance(other,Rational):
            other = Rational(other,1)
            numenator =self.denom*other.num
            return numenator <= self.num
        elif isinstance(other,str):
            raise NotImplementedError
        else:
            numenator1 = self.denom*other.num
            numenator2 = self.num * other.denom
            return numenator1 <= numenator2

    def getfloat(self):
        return self.num/self.denom
