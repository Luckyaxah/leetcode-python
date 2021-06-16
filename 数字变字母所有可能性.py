from typing import Set
def combinations(number: int) -> Set[str]:
    numbers = list(str(number))
    d = {}
    for i in range(26):
      d[str(i+1)] = chr(ord('a')+i)
    # print(d)
    # print(numbers)
      
    def help(numbers):
      if not numbers:
        return ''
      if len(numbers) == 1:
        return [ d[numbers[0]] ]


      ret1 = []
      r1 = help(numbers[1:])

      if r1:
        ret1 = [d[numbers[0]] + i for i in r1]
      
      ret2 = []
      if numbers[0] + numbers[1] in d:
        r2 = help(numbers[2:])
        if r2:
          ret2 = [d[numbers[0] + numbers[1]] + i for i in r2]
        else:
          ret2 = [ d[numbers[0] + numbers[1]] ]
      return ret1 + ret2
    return set(help(numbers))
      
print(combinations(141))
      