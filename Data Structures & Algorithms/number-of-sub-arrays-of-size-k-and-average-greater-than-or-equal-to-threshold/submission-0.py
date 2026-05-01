class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        total = sum(arr[L:k-1])
        count = 0
        for R in range(k-1, len(arr)):
            total += arr[R]
            if total/k >= threshold:
                count += 1
            total -= arr[L]
            L += 1
        return count
        