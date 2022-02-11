arrayy = [1, 2]
amountt = 5

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount] * (amount+1)
        dp[0] = 0
        
        for a in range(1, amount-1):
            print(a, "aaaaa")
            
            for c in coins:
                print(c, "c")
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    print(dp[a], "---->dp[a] ||||", 1 + dp[a - c], "---->1 + dp[a - c] |||",a - c, "---->a-cc")
                
            print(dp[a], "dp[a]dp[a]dp[a]")
            print("")
        print(dp, "dppppppppppp")
        return dp[amount] if dp[amount] != amount + 1 else -1


f = Solution
gg = f.coinChange(f, arrayy, amountt)
print(gg)
#if dp[amount] != amount + 1 else -1
