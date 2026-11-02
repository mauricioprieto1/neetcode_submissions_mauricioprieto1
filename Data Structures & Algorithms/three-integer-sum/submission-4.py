class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # so we have an array of numbers and we want to find the numbers that will sum up to 0
        # sort array
        # avoid duplicates
        res = []
        nums.sort()

        # iterate over the array, take one number (anchor)
        #   check all numbers to the left, using 2 pointers
        #    
        for i, a in enumerate(nums):
            # avoid duplicate anchors
            if i > 0 and nums[i-1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l - 1]:  
                        l += 1
                    r -= 1
                    res.append([a, nums[l], nums[r]])


        return res
            