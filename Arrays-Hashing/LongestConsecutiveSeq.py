'''
Given an unsorted array of integers 'nums', return the length of the longest consecutive
elements seq

nums = [100,4,200,1,3,2]
output: 4
'''

'''
Explanation:

Create a hashset for nums first, and a counter so its easy to return the max seq

then iterate through nums. If (n-1) means thats the start of a sequence, length = 0
while there is an n + length in the set, length += 1
then return counter = max(counter,length)

'''

def longest_consecutive_sequence(nums):

    num_set = set(nums)
    counter = 0

    for n in nums:
        #if the n is the start of a sequence (n-1) set length to be 0 then add 1 every time theres a (n + length)
        if (n-1) not in num_set:
            length = 0
            #loop to find consecutive nums in the set
            while (n + length) in num_set:
                length +=1 
            counter = max(counter, length)
    return counter