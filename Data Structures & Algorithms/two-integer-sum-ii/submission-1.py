class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # target = 5
        # [1, 2, 4, 5]
        #  ^        ^
        # 6 > target
        # 

        # target = 3
        # [1, 2, 3, 4]
        
        # not O(1) space:
        # num_set = set(numbers)
        # searching = False
        # i_ret = -1
        # j_ret = -1

        # for i in range(0, len(numbers), 1):
        #     if not searching:
        #         diff = target - numbers[i] 
        #         if diff in num_set:
        #             searching = True
        #             i_ret = i
        #     else:
        #         if numbers[i] == target - numbers[i_ret]:
        #             j_ret = i
        
        # return [i_ret+1, j_ret+1]

        front = 0
        back = len(numbers) - 1

        while front < back:
            num_sum = numbers[front] + numbers[back]

            if num_sum == target:
                return [front + 1, back + 1]
            elif num_sum > target:
                back -= 1
            else:
                front += 1
            
