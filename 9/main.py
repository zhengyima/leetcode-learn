class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = 0
        x_src = x
        while x>0:
            y = y * 10 + x % 10 
            x = int(x/10)
        return y == x_src
            
            
