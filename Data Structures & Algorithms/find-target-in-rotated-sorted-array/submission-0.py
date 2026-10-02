class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        pivot = 0
        while L <= R:
            if nums[L] <= nums[R]:
                pivot = L if nums[L] <= nums[pivot] else pivot
                break
            mid = (L+R)//2
            pivot = mid if nums[mid] <= nums[pivot] else pivot
            if nums[L] <= nums[mid]:
                L = mid+1
            else:
                R = mid-1
        if target < nums[pivot] or target > nums[pivot-1]:
            return -1
        if target <= nums[len(nums)-1]:
            L, R = pivot, len(nums)-1
        else:
            L, R = 0, pivot-1
        while L <= R:
            mid = (L+R)//2
            if nums[mid] > target:
                R = mid-1
            elif nums[mid] < target:
                L = mid+1
            else:
                return mid
        return -1
        