class Solution(object):
    def twoSum(self, nums, target):
      nums1 = []
      for i in range(0,len(nums)) :
        k = nums[i]
        nums1.append(k)
    
      nums.sort()
        
      i=0
      j=len(nums)-1
      z = []
      z1 = []
      for x in range(0,len(nums)) :
         if nums[i] + nums[j] > target :
            j=j-1
         elif nums[i] + nums[j] < target :
            i=i+1
         else :
            z.append(nums[i])
            z.append(nums[j])
            break
      for k in range (0,len(nums1)) :
        if z[0] == nums1[k] :
         s=k
         z1.append(k)
         break
      for k in range (0,len(nums1)) :
        if z[1] == nums1[k] and s!=k:
         z1.append(k)
         break
        
      return z1