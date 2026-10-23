# 1. Two Sum  (Easy)
# https://leetcode.com/problems/two-sum/

class Solution:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    
    @classmethod
    def two_sum(cls, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {} # empty dict initialization, no memory allocated
        for i, num in enumerate(nums): # one loop
            complement = target - num # constant operation so O(1)
            if complement in seen: # O(1): no matter size of seen, dictionary lookup is contant due to the hashing function applied to the key
                return [seen[complement], i]
            seen[num] = i # O(1): constant operation
        return []


if __name__ == "__main__":
    input = [2,7,11,15]
    target = 9
    output = [0,1]
    assert Solution.two_sum(nums=input, target=target) == output
