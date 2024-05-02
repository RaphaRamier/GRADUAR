'''

Esse problema no site parecia algo estranho, pois havia várias soluções mas ele aceita algumas poucas, a que eu consegui chegar mesmo não gostando de usar o while para isso foi essa.

tentei:


ListComprehension como, por exemplo:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = [i for i in nums if i != val]

        return n

Lambda:


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = list(filter(lambda x: x != val, nums)

        return n


Mas o que funcionou foi o código abaixo.
'''





class Solution(object):
    def removeElement(self, nums, val):

        while val in nums:
           nums.remove(val)