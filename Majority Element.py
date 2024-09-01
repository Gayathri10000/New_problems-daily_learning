class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                di[i]+=1
        max_ele=0
        ele = None
        for key, val in di.items():
            if val> max_ele:
                max_ele = val
                ele = key

        return ele
