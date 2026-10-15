class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        use a hashmap to keep track of the numbers seen and their indices
        iterate over the list of numbers and if theyre not already in the dict, add them with dict[num] = key
        on each iteration, check if the number needed to reach the sum is already in the dict
        """

        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return False
        