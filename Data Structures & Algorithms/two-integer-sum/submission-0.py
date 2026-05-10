class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in complement:
                return [complement[comp], index,]
            complement[num] = index
        