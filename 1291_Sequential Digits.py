class Solution(object):
    def sequentialDigits(self, low, high):
        res = []
        low_d, high_d = len(str(low)), len(str(high))       #lower bound, upper bound

        for digits in range(low_d, high_d + 1):
            for start in range(1,9):                        # upper bound 9:next sequence = 10, unsatisfies constraints
                if start + digits >10:
                    break                                   # constraint unsatisfied
                num = start
                prev = start                                #keep track of start

                for i in range(digits-1):
                    num= num*10          #multiplies the number with 10, ex.: num = 23*10=230
                    prev += 1       #adds the sequential digit in place of 0, ex.:234
                    num += prev     #sets num as 234 and repeats until bound is satisfied
                if low<= num <=high:                        #check contraints
                    res.append(num)
        return res
