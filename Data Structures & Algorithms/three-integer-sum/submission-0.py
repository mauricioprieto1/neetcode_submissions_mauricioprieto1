class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # if anchor is positive, end loop
            if a > 0:
                break
            # avoid repeating anchor number
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    # decrease sum
                    r -= 1
                elif threeSum < 0:
                    # increase sum
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # move on
                    l += 1
                    r -= 1
                    # skip repeated left pointer numbers
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res







        