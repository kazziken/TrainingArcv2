class Solution:
    def coinChange(self, coins, amount: int) -> int:

        '''
        coins = [1,2,5]
        amount = 11
        return the least num that is required to add up to that amount
        return -1 if none of the coins add up to == amount
        
        if we start with greedy approach (start with pointer at len(coins) - 1), we technically can read the solution quicker.
        but it doesn't work b/c
        ex. [1,3,4,5] amount = 7
        greedy will return 5 + 1 + 1 which is obv not the answer

        lets use DP (backtracking) - top down memoization 
        or bottom-up memoization starting with reverse order (starting with 0)

            
        '''
        #dp needs to be always +1 to compensate for index 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        #checks to see if its not the same amount, it was originally in the dp array. If it is, that means no coin combinations hence return -1
        return dp[amount] if dp[amount] != amount + 1 else -1

        


        