class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = []
        flag = False
        for i in range(len(nums)):     
            for j in range(len(nums)):
                if nums[j] == target - nums[i] and i != j:
                    pos.append(i)
                    pos.append(j)
                    flag = True

            if flag == True:
                break
                
        pos.sort()
        return pos