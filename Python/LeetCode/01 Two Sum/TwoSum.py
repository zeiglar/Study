# Description https://leetcode.com/problems/two-sum/description/

from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        remaining = 0
        hashmap = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hashmap:
                ans.append(hashmap[remaining])
                ans.append(i)
                break
            else:
                hashmap[nums[i]] = i

        return ans