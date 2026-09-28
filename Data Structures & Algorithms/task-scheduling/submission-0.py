class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for val in tasks:
            count[ord(val) - ord("A")] += 1
        count.sort()
        maxf = count[25]
        idle = (maxf - 1)*n
        for i in range(25):
            idle -= min(count[i], maxf-1)
        return len(tasks) + max(0, idle)


        
        
        