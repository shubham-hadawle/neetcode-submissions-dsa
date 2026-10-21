class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1st Intersection: Fast & Slow Pointers
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                intersection = fast
                break

        # 2nd Intersection: Two Slow Pointers
        slow1, slow2 = 0, intersection

        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        return slow2