class Solution:
    '''
    [0,1,2,3,4,5,6,7]
    [1,7,2,5,4,7,3,6]
     ^             ^

     7 * 1 = 7


    '''
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = -1
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            curr_area = length * width
            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area