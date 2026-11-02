class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            # avoid anchor duplicates
            if i > 0 and nums[i - 1] == anchor:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = anchor + nums[l] + nums[r]
                if currentSum < 0:
                    l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    # found triplet
                    res.append([anchor, nums[l], nums[r]])
                    # move pointers
                    l += 1
                    r -= 1
                    # check if l is duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res