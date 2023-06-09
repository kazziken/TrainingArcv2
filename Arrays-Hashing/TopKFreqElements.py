'''

Given an integer array (nums) and integer (k), return the k most freq elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''

'''
Explanation, 

Create a hashmap to count ocurrence of each element
then create a frequency bucket sort.

what a bucket sort looks like
freq = [[] for i in range(len(nums) + 1)]
for len(nums + 1) = 6, we do (+1) because thats the maximum amount of times an element can occur
this creates [[],[],[],[],[],[]]
then we append the element to the index(which we'll correlate the amount of times it occurred)

while counting backwards (because the higher the index, the higher the ocucurence)
when len(res) == k, return res

'''

def top_k_frequent_elements(nums, k):

    count_elements = {}
    #this is a bucket sort
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count_elements[num] = count_elements.get(num, 0) + 1
    
    # count_elements = {
    #     1: 3,
    #     2: 2,
    #     3: 1,
    # }

    #we're only adding value to bucket sort
    for key,value in count_elements.items():
        freq[value].append(key)
        print(freq)
    
    res = []
    
    #higher the index, the more occurences so we count from the end of res
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


arr = [1,1,1,2,2,3]
k = 2

print(top_k_frequent_elements(arr,k))

    