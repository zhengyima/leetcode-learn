class Solution:
    def reverse(self, x: int) -> int:
        # x = 120
        # print(2**30-1)
        # negative = False
        # if x < 0:
        #     negative = True
        #     x = -x
        print(-123%10)
        nums = [] 
        x_src = x
        y = 0
        while x!=0:
            # x_10 = 
            # nums.append(x%10)
            y = (y * 10) + x%10
            x = int(x/10)
            
        
        # for i in range(len(nums)):
        #     y = (y * 10) + nums[i]
        if y < -2**31 or y > 2**31 -1:
            return 0
        # if negative:
        #     y = -y
        return y