'''

O intuito do código é dando um array de inteiros e um alvo, deve retornar os indices(index) dos dois números que
somados sejam igual ao algo:


Ex.: 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Ex.: 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Ex.: 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = []

        for i, tar1 in enumerate(nums):
            for j, tar2 in enumerate(nums[i + 1:]):
                if tar1 + tar2 == target:
                    l.append(i)
                    l.append(i + j + 1)
                    return l