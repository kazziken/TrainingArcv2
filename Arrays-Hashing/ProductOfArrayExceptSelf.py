'''
Given an integer array(nums), return an array (ans) such that (ans[i]) is == to the product of all the element of
nums except nums[i]

The product of any prefixfix or suffix of nums in guaranteed to fit in a 32-bit int

Must write an algo that run O(n) without division operation

'''

'''
based on ans = [1,2,3,4]
If you think about it logically if product of array except self

self should just be 1 since anything multiply by 1 is self

ans is an array of all 1s
we'll take a prefix and store them in ans
ans[0] prefix doesn't exist so move to ans[1] which stores the prefix which is ans[0]
ans[2] == ans[1] * ans[0] and so on.

ans = [1,1,2,6]

then using the postfix, we start from the end
multiply postfix * prefix(which is in the ans)
starting from the end
ans[i] *= postfix
then update postfix to be postfix *= nums[i]

ans = [24,12,8,6]

'''

def product_of_array_except_self(nums):

    ans = [1] * len(nums)

    prefix = 1 #index 1

    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix # 1 * last element of ans
        postfix *= nums[i]
    return ans



