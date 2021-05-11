class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            result2 = "".join(reversed(str(x)))
            if int(result2) > (2**31-1):
                return 0
            return int(result2)*-1
        
        result2 = "".join(reversed(str(x)))
        if int(result2) > (2**31-1):
                return 0
        return int(result2)
