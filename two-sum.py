class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        """ One pass through array using hashmap, time: O(n) + space: O(n) """ 

        prevMap = {} # value : index 

        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in prevMap: 
                return [prevMap[diff], i] 
            prevMap[n] = i # add value : index pair 


test = Solution() 
print(test.twoSum([3,4,5,6], 7))
