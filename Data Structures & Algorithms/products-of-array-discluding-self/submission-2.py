class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            temp = 1
            for j, val in enumerate(nums):
                if i != j:
                    temp *= val
            res.append(temp)
        return res
                    
                    


        

        





        

        