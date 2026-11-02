class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        existingNumbers = set(nums)

        for num in nums:
            currentStreak = 0
            currentNumber = num
            while currentNumber in existingNumbers:
                currentStreak += 1
                currentNumber += 1
            res = max(res, currentStreak)
        return res