import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=int(num1)
        print(num1)
        num2=int(num2)
        print(num2)
        num3=num1+num2
        return str(num3)