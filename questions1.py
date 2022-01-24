def twoSum(nums, target):
        lst=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    lst.extend([x,y])
                    
        lst=list(set(lst))
        return lst

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
