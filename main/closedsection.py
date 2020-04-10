
class ClosedSection:
    def __init__ (self, lower : int, upper :int):
        if isinstance(lower, int) and isinstance(upper, int):
            if lower <= upper:
                self.lower = lower
                self.upper = upper
            else:
                raise InputValueError   # 入力値の上限と下限が逆転している場合
        else:
            raise InputTypeError    # 入力した型が整数型以外の場合
    
    def stringify(self):
        return "[{0},{1}]".format(self.lower,self.upper)
    
    def getLower(self):
        return self.lower
    
    def getUpper(self):
        return self.upper
    
    def is_element_of(self, num):
        if num <= self.upper and num >= self.lower:
            return True
        else:
            return False
    
    def equals(self,other):
        if not isinstance(other, ClosedSection):
            raise NotImplementedError
        else:
            return self.lower == other.lower and self.upper == other.upper        

    def includes(self,other):
        if not isinstance(other, ClosedSection):
            raise NotImplementedError
        else:        
            return self.lower <= other.lower and self.upper >= other.upper 


    
class InputTypeError(Exception):
    "整数以外が入力されました"
    pass

class InputValueError(Exception):
    "上端と下端の値が逆転しています"
    pass