
##bubble sort
def bubbleSort(nums):
    for i in range(len(nums),1,-1):
        for j in range(i-1):
           if nums[j] > nums[j+1] :
               nums[j],nums[j+1]=nums[j+1],nums[j]
                             
##select sort
def selectSort(nums): 
    for i in range(len(nums),1,-1):     
        for j in range(i-1):
            if nums[j] > nums[i-1] :
                nums[j],nums[i-1]=nums[i-1],nums[j]
                

def insertSort(nums):
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] < nums[j] :
                nums[0:i+1]=nums[0:j] + [nums[i]] + nums[j:i]

nums=[4,8,2,3,1,0]
insertSort(nums)
print (nums)
              




