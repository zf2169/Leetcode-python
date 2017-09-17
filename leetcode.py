class Solution:
    #1.Two Sum
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    print([i,j])
                    
    def twoSum2(self, nums, target):
        dict={}
        for idx1,n1 in enumerate(nums):
            dict[n1]= idx1
            n2= target-n1
            if n2 in dict:
                print(sorted([idx1, dict[n2]]))
            
ans=Solution()
ans.twoSum(nums=[2,7,11,15], target=9)
ans.twoSum2(nums=[2,7,11,15], target=9)

#2. Add Two Numbers
def addTwoNumbers(l1, l2):
    n=max(len(l1), len(l2))
    a=[0]*(n-len(l1))+l1
    b=[0]*(n-len(l2))+l2
    add=0; sums=[0]*n
    for idx in range(1,n+1):
        sum= a[-idx]+b[-idx]+add
        if sum>=10:
            sum=sum-10
            add=1
        else: add=0
        sums[-idx]=sum
    if add==1:
        sums=[1]+sums
    print(sums)
 
addTwoNumbers(l1=[2,4,3],l2=[5,6,4])
addTwoNumbers(l1=[5,0,0], l2=[1,5,0,0])

3. Longest Substring Without Repeating Characters


































