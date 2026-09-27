class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        M = 0
        L = 0
        great = lambda x, y: x > y
        less = lambda x, y: x < y
        length = 1
        nextV = None
        maxL = 1

        for R in range(1, len(arr)):
            if not nextV:
                if arr[R] > arr[M]:
                    nextV = less
                    length += 1
                    maxL = max(maxL, length) 
                    M += 1
                    continue
                if arr[R] < arr[M]:
                    nextV = great
                    length += 1
                    maxL = max(maxL, length)
                    M += 1
                    continue

            if arr[R] == arr[M]:
                M = R
                nextV = None
                length = 1
                continue
            
            if nextV(arr[R], arr[M]):
                length += 1
                maxL = max(maxL, length)
                nextV = great if nextV == less else less
                M += 1
            else:
                # arr[R] and arr[M] are still unequal, so they form a new valid pair of length 2
                length = 2
                nextV = less if arr[R] > arr[M] else great
                M = R
        return maxL


        