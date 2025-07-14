nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i,num in enumerate(nums):
            complement = target- num
            if complement in hash_map:
                return [hash_map[complement],i]
            hash_map[num]=i
            
print(twoSum(nums, target))
                

        
