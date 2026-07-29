class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sw = deque(sandwiches)
        while sw and sw[0] in st:
            if sw[0] == st[0]:
                sw.popleft()
                st.popleft()
            else:
                st.append(st.popleft())
        return len(sw)



        