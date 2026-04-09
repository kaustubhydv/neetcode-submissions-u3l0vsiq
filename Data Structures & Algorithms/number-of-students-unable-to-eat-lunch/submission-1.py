class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for val in sandwiches[:]:
            if val == 0:
                if cnt[0]>0:
                    cnt[0] -= 1
                    sandwiches.pop(0)
                else:
                    break
            else:
                if cnt[1]>0:
                    cnt[1] -= 1
                    sandwiches.pop(0)
                else:
                    break
        return len(sandwiches)
        


        