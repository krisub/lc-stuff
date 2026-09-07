class Solution:
    '''
    [-1,0,1,2,-1,-4]

    sorted:

    [-4, -1, -1, 0, 1, 2]
      ^             ^  ^

    two sum where -(nums[i]) is the target
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        if len(nums_sorted) < 3:
            return []
        
        triplets = set()

        for idx in range(0, len(nums), 1):
            i = idx + 1
            j = len(nums) - 1
            target = -(nums_sorted[idx])
            while i < j:
                if nums_sorted[i] + nums_sorted[j] == target:
                    triplets.add((nums_sorted[i], nums_sorted[j], nums_sorted[idx]))
                    i += 1
                    j -= 1
                elif nums_sorted[i] + nums_sorted[j] < target:
                    i += 1
                else:
                    j -= 1

        return list(triplets)

            
