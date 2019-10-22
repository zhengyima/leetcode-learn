class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,n in enumerate(nums):
        #     n2 = target - n
        #     if n2 in nums[i+1:]:
        #         return [i,nums[i+1:].index(n2)+i+1]
        #     else:
        #         continue
        
        # inv_dict = {}
        # for i,n in enumerate(nums):
        #     if n in inv_dict:
        #         inv_dict[n].append(i)
        #     else:
        #         inv_dict[n] = []
        #         inv_dict[n].append(i)
        
        # for i,n in enumerate(nums):
        #     m = target - n
        #     # if m in inv_dict:
        #     if m == n:
        #         if len(inv_dict[m])<=1:
        #             continue
        #         else:
        #             return [i,inv_dict[m][1]]
        #     else:
        #         if m in inv_dict:
        #             return [i,inv_dict[m][0]]

        dic = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in dic:
                return [dic[m],i]
            
            dic[n] = i
                
                