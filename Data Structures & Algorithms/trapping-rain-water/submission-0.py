class Solution:

    '''
     [0,2,0,3,1,0,1,3,2,1]

     [0,2,2,3,3,3,3,3,3,3]
     [3,3,3,3,3,3,3,3,2,1]
amt: [0,0,2,0,2,3,2,0,0,0]
         
        .
    .   .
    . . . 

    min(left, right) - curr
    '''

    def trap(self, height: List[int]) -> int:
        
        prefix_max = [-1] * len(height)
        suffix_max = [-1] * len(height)

        prefix_max[0] = height[0]
        suffix_max[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height), 1):
            prefix_max[i] = max(height[i], prefix_max[i-1])

        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(height[i], suffix_max[i+1])

        total = 0

        for i in range(0, len(height), 1):
            amount = min(prefix_max[i], suffix_max[i]) - height[i]

            if amount > 0:
                total += amount

        return total


