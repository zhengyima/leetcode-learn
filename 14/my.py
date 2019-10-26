class Solution:
    def find_min_strs(self, strs):
        min_i = 0
        min_len= len(strs[0]) 
        for i,s in enumerate(strs):
            if len(s)<min_len:
                min_i = i
                min_len = len(s)
        tmp = strs[0]
        strs[0] = strs[min_i]
        strs[min_i] = tmp
        return strs
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs = self.find_min_strs(strs)
        s1 = strs[0]
        sprefix = ""
        find = True
        for i,c in enumerate(s1):
            sprefix += c
            find = True
            for j,str_j in enumerate(strs[1:]):
                # print([sprefix,str_j[:len(sprefix)]])
                if sprefix != str_j[:len(sprefix)]:
                    find = False
            
            if not find:
                break
        
        if find:
            return sprefix
        else:
            return sprefix[:-1]
        # return sprefix
                