class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start<= end:
            my_guess = (start+end)//2
            if guess(my_guess) == 1:
                start = my_guess+1
            elif guess(my_guess) == -1:
                end = my_guess -1
            elif guess(my_guess) == 0:
                return my_guess

def guess(num):
    pass
