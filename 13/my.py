class Solution:
    def romanToInt(self, s: str) -> int:
        # s  ="MCMXCIV"
        char2num = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        special_str = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        sum = 0
        jump = False
        for i in range(len(s)):
            if jump:
                jump = False
                continue
                
            if i == len(s) - 1:
                sum += char2num[s[i]]
            else:
                j = i + 1
                s2 = s[i:j+1]
                if s[i:j+1] in special_str:
                    sum += special_str[s2]
                    # i += 1
                    jump = True
                else:
                    sum += char2num[s[i]]
            # print(sum)
        
        # print(sum)
        return sum
            