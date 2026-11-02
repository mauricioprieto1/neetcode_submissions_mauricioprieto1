class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers approach:
        # sort number array
        # choose one number anchor, then look for the other  2 numbers in the rest of the array 
        # make sure anchor is not repeated (nums[i] != nums[i-1])
        # check the 3sum, if < 0, l++ ; if > 0 r--
        # one 3sum == 0, append triplets to res
        # skip repeated left pointers 
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            