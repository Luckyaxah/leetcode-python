class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        r = licensePlate.lower()
        def get_d(word):
            d = {}
            for c in word:
                if c.isalpha():
                    if c in d:
                        d[c] += 1
                    else:
                        d[c] = 1
            return d
        
        d = get_d(r)
        result = ''
        for word in words:
            d1 = get_d(word)
            if all( [d[key] <= d1.get(key,0) for key in d] ):
                if not result:
                    result = word
                    length = len(word)
                elif len(word) < length:
                    result = word
                    length = len(word)
        return result



