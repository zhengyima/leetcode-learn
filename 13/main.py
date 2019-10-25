class Solution:
    def romanToInt(self, s: str) -> int:
        char2num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                sum += char2num[s[i]]
            else:
                if char2num[s[i]] < char2num[s[i+1]]:
                    sum -= char2num[s[i]]
                else:
                    sum += char2num[s[i]]
        return sum