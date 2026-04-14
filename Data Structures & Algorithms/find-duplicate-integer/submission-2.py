class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1st Point of Intersection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]           # 1X Speed
            fast = nums[nums[fast]]     # 2X Speed, index of index in the array
            if slow == fast:
                break

        # 2nd Point of Intersection
        slow2 = 0
        while True:
             slow = nums[slow]
             slow2 = nums[slow2]
             if slow == slow2:
                return slow