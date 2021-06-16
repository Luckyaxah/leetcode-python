def edit_distance(word_1: str, word_2: str) -> int:
    class Info:
      def __init__(self, count):
        self.count = count
    def helper(word1, word2):
      # print(word1, word2)
      if word1 == word2:
        return Info(0)
      if word1 and not word2:
        return Info(len(word1))
      if not word1 and word2:
        return Info(len(word2))

      # insert
      info1 = helper(word1, word2[1:])
      # delete
      info2 = helper(word1[1:], word2)
      # repalce
      info3 = helper(word1[1:], word2[1:])
      _min = min(info1.count, info2.count, info3.count) + 1
      
      # not doing anything
      if word1[0] == word2[0]:
        info4 = helper(word1[1:], word2[1:])
        _min = min(_min, info4.count)
      
      return Info(_min)
    return helper(word_1, word_2).count
print( edit_distance('horse','ros') )
      