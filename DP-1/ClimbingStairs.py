'''
You're climbing a staircase. It takes n steps to reach the top

Each time you can either climb 1 or 2 steps. How many distinct ways you can climb to the top?

Input n=2
Output: 2

1+1 or 2

Input n=3
Output: 3
1+1+1
or 1+2
or 2+1

'''

#Solution One
def climbing_stairs(self, n):
    if n <= 3:
        return n
    
    n1, n2 = 2,3

    for _ in range(4, n+1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2
'''for climbing_stars(5)
    the loop runs 3 times and by the end of it return n2 and thats how many distinct ways
    to climb 5 steps.
    n1 
'''


# DP solution 

def climb(n):

    if n <= 2:
        return n
    
    #to account for 0 steps
    dp = [0] * (n + 1) 
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


'''
Explanation:
for DP it helps store previous amount of distinct ways to climb n steps
so we create a DP array to store that information

dp[1] and dp[2] is 1 and 2 since those are set in stone

in range (3 to n+1) accounts for the array since dp[0] is added

dp[i] = dp[i-1] + dp[i-2] fibinacci seq to help us get the answer

'''