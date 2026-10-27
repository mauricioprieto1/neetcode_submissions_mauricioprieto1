class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        highestSequence = 0

        for num in nums:
            if (num - 1) not in numSet: # start of a sequence?
                length = 1

                while (num + length) in numSet: # while the sequence exists 
                    length += 1

                highestSequence = max(length, highestSequence)
        return highestSequence 

    # O (n) space and time complexity 