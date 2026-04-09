class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_0 = 0
        stud_1 = 0
        for val in students:
            if val == 0:
                stud_0 += 1
            else:
                stud_1 += 1
        for val in sandwiches[:]:
            if val == 0:
                if stud_0>0:
                    stud_0 -= 1
                    sandwiches.pop(0)
                else:
                    break
            else:
                if stud_1>0:
                    stud_1 -= 1
                    sandwiches.pop(0)
                else:
                    break
        return len(sandwiches)
        


        