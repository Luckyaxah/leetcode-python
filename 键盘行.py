class Solution:
    def findWords(self, words):
        """
        给定一个单词列表，返回可以用同一行字母打印的单词
        """
        l= ['qwertyuiop','asdfghjkl','zxcvbnm']
        ret=[]
        for word in words:
            for line in l:
                found = True
                for c in word.lower():
                    if c not in line:
                        found = False
                        break
                if found == True:
                    ret.append(word)
                    break
        return ret

if __name__ == "__main__":
    print(Solution().findWords(['Hello','Alska','Dad','Peace']))
                