# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id: int) -> int:
        def helper(employees, _id):
            for e in employees:
                if e.id == _id:
                    ret = e.importance
                    for i in e.subordinates:
                        score = helper(employees, i)
                        ret += score
                    return ret
        return helper(employees, id)