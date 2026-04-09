class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for val in sandwiches[:]:
            if cnt[val]>0:
                cnt[val] -= 1
                sandwiches.pop(0)
            else:
                break
        return len(sandwiches)
        


        