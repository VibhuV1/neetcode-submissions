class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force:
        """
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """

        # hashmap:
        """
        hash_map = {ele: index for index, ele in enumerate(nums)}
        for i in range(0, len(nums)):
            ele = target - nums[i]
            if hash_map.get(ele):
                if hash_map.get(ele) != i:
                    return [i,hash_map.get(ele)]
        """

        #clever hashmap:
        hash_map = {} # ele: idx
        for (i, num) in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                print(target, num, (target - num) in hash_map, hash_map)
                return [hash_map.get(diff),i]
            else:
                hash_map[num]= i
