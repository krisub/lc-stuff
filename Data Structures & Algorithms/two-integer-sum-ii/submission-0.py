class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # target = 5
        # [1, 2, 4, 5]
        
        num_set = set(numbers)
        searching = False
        i_ret = -1
        j_ret = -1

        for i in range(0, len(numbers), 1):
            if not searching:
                diff = target - numbers[i] 
                if diff in num_set:
                    searching = True
                    i_ret = i
            else:
                if numbers[i] == target - numbers[i_ret]:
                    j_ret = i
        
        return [i_ret+1, j_ret+1]
