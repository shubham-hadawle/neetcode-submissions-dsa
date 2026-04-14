class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMaps
        hashmap =  {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            num2 = target - nums[i]

            if num2 in hashmap and hashmap[num2] != i:
                    return [i, hashmap[num2]]
        
        # Brute Force
        # pos = []
        # flag = False
        # for i in range(len(nums)):     
        #     for j in range(len(nums)):
        #         if nums[j] == target - nums[i] and i != j:
        #             pos.append(i)
        #             pos.append(j)
        #             flag = True

        #     if flag == True:
        #         break
                
        # pos.sort()
        # return pos