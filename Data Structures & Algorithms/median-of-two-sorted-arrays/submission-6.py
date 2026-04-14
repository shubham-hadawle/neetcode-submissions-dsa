class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary Search
        # Swap if nums2 is smaller than nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        TOTAL = len(nums1) + len(nums2)
        LEFT_HALF = (TOTAL + 1) // 2
        low, high = 0, len(nums1)

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = LEFT_HALF - mid1
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")

            if mid1 < len(nums1):
                r1 = nums1[mid1]
            if mid2 < len(nums2):
                r2 = nums2[mid2]
            if mid1 > 0:
                l1 = nums1[mid1 - 1]
            if mid2 > 0:
                l2 = nums2[mid2 - 1]

            if  l1 <= r2 and l2 <= r1:
                # Condition met, now check if TOTAL is Even or Odd
                if TOTAL%2 == 0:
                    # Even
                    median = (max(l1, l2) + min(r1, r2)) / 2
                    return median
                else:
                    median = max(l1, l2)
                    return median

            if l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1