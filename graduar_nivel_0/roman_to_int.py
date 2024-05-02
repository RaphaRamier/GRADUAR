'''
O intuito do algoritmo é converter números romanos, que são strings, em números (int).
Sem o uso da biblioteca Roman.

'''


class Solution(object):
    def romanToInt(self, s=str()):
        n = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

        for i, j in zip(s, s[1:]):
            if roman[i] < roman[j]:
                n -= roman[i]
            else:
                n += roman[i]

        return n + roman[s[-1]]