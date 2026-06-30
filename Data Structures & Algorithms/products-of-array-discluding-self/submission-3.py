class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre , suff, res = [0]*n, [0]*n, [0]*n
        pre[0] = suff[n-1] = 1
        for i in range(1, n):
            pre[i] = nums[i-1]*pre[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1]*suff[i+1]
        for i in range(n):
            res[i] = suff[i]*pre[i]
        return res

                    
                    


        

        





        

        