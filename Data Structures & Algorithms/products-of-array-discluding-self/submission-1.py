import math

# range(start, stop, step)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive
        # outputs = []
        # for i in range(len(nums)):
        #     product = math.prod(nums[0:i])
        #     product *= math.prod(nums[i+1:])
        #     outputs.append(product)
        
        # return outputs

        # [2,2,4,6]
        # solution: [48, 48, 24, 16]
        # prefix products: [1, 2, 4, 16], at each index i, stores the product of the elements before i
        # suffix products: [48, 24, 6, 1], at each index i, stores the product of the elements after i
        # prefix * suffix: [48, 48, 24, 16]

        len_nums = len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ret = [1] * len(nums)

        for i in range(1, len(nums), 1):
            prefix[i] = nums[i-1] * prefix[i-1] 
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(0, len(nums), 1):
            ret[i] = prefix[i] * suffix[i]

        return ret
        