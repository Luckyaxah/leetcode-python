class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
        如果被奖赏，返回True
        """
        a_flag = False
        l_flag = False
        count_a = 0
        count_l = 0
        for c in s:
            if c == 'A':
                count_a += 1
                if count_a > 1:
                    a_flag = True
                count_l = 0
            elif c == 'L':
                count_l += 1
                if count_l > 2:
                    l_flag = True
            else:
                count_l = 0
            if a_flag or l_flag:
                return False
        return True




if __name__ == "__main__":
    # P: Present
    # L: Late
    # A: Absent
    s = 'PPALLL'
    print(Solution().checkRecord(s))