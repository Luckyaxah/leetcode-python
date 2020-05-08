# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        earliest_wrong_version = n
        lastest_right_ver = 0
        while True:
            # print(lastest_right_ver,earliest_wrong_version)
            t = (earliest_wrong_version+lastest_right_ver)//2
            if isBadVersion(t):
                earliest_wrong_version = t
            else:
                lastest_right_ver = t
            if earliest_wrong_version-lastest_right_ver==1:
                break
        return earliest_wrong_version


def isBadVersion(t):
    return True