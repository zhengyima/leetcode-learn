class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        s1 = strs[0]
        sprefix = ""
        find = True
        for i,c in enumerate(s1):
            sprefix += c
            find = True
            for j,str_j in enumerate(strs[1:]):
                if (len(str_j) <= i) or (len(str_j) > i and  str_j[i] != c):
                    find = False
            if not find:
                break
        if find:
            return sprefix
        else:
            return sprefix[:-1]
        # return sprefix
                