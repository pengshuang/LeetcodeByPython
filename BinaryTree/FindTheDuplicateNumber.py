# -*- coding: utf-8 -*-
'''
Given an array nums containing n + 1 integers where each integer
is between 1 and n (inclusive), prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Note:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution(object):
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        '''
        这里利用了二分法的思想
        '''
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high

class Solution2(object):
    def findDuplicate(self, nums):
        start = 0
        end = len(nums)
        nums.sort()
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > mid:
                start = mid
            else:
                end = mid
        return end

class Solution3(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return slow

'''
Test:
nums:[1,2,2,3]
'''
nums = [1, 2, 3, 3, 3]
solution = Solution()
index = solution.findDuplicate(nums)
print(index)
