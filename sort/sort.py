
def bubbleSort(nums):
    lenNums=len(nums)
    if lenNums==0:
        return nums
    for i in range(lenNums-1):
        if nums[i]>nums[i+1]:
            tmp=nums[i+1]
            nums[i+1]=nums[i]
            nums[i]=tmp
    lenNums -=1
    nums[0:lenNums]=bubbleSort(nums[0:lenNums])   ###???
    return nums

def selectSort(nums):
    lenNums=len(nums)
    if lenNums==0:
        return nums
    max=nums[0]
    for i in range(1,lenNums-1):
        if nums[i]>max:
            max=nums[i]
            nums.remove(max)
            nums.append(max)
    lenNums -=1
    nums[0:lenNums]=bubbleSort(nums[0:lenNums])   ###???
    return nums



nums=[]

print (selectSort(nums))


