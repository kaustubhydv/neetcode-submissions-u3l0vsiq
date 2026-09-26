class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k == 0:
            return len(arr)
        avg = 0
        L = 0
        count = 0
        summ = 0
        for i in range(k):
            summ += arr[i]
        avg = summ/k
        if avg >= threshold:
            count += 1
        for R in range(k, len(arr)):
            avg = (avg*k - arr[L] + arr[R])/k
            if avg >= threshold:
                count += 1
            L += 1
        return count


        