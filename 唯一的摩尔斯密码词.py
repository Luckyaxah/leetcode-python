class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        def word2morse(word):
            characters = [chr(ord('a')+i) for i in range(26)]
            morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            d = dict(zip(characters, morses))
            s = ''
            for c in word:
                s += d[c]
            return s
        ret = []
        for word in words:
            m = word2morse(word)
            if m in ret:
                continue
            ret.append(m)
        return len(ret)