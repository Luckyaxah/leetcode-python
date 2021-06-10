class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        ret = letters[0]
        for letter in letters:
            if ord(letter) > ord(target):
                if ord(ret) <= ord(target):
                    ret = letter
        return ret
