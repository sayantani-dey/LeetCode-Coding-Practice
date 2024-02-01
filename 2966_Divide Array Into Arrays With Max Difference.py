class Solution(object):
    def divideArray(self, nums, k):
sort() #to sort the input array
        op = []# to store the output
        for i in range(0,len(nums),3): #increment by 3
            if nums[i+2]-nums[i]> k: #if doesn't satisfy k
                return[]
            op.append(nums[i:i+3])   #if k is satisfied
        return op

"""
Approach:
1. Sort the array: Taking a closer look to the approach, 
it seems best to sort the numbers based on their values so that the difference between the elements in a array is not greater than the value of k.
2. Initialize an empty array op in this case to store the output.
3. A for loop that runs through the length of the array, incrementing by 3 every time. Within this loop, we check for the condition where the 
difference between the elements in the array are greater than k, to reduce the complexity instead of performing condition <= k.
"""
