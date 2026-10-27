class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # except i
        prefix = [1] * n # <- i 
        postfix = [1] * n # i -> 
        result = [1] * n
        # prefix product array
        for i in range(1, n): # skip the first element "1"
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # postfix product array
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        # result array
        # print("prefix",prefix)
        # print("postfix",postfix)
        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        # print("result",result)
        return result

        #space and time O(n)



        
