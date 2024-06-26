class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        total_number_to_represent_target = pow(2,n) #For n = 3 it's 0-7 i.e 8 numbers
        dp = [float('inf') for i in range(total_number_to_represent_target)]
        # no characters required to represent empty string
        dp[0] = 0
        
        for i in range(total_number_to_represent_target):
            # Start to explore paths from reachable states hence
            if dp[i]==float('inf'):
                # Its not reachable
                continue
            else:
                for sticker in stickers:
                    state = i
                    for ch in sticker:
                        for index,t in enumerate(target):
                            if t==ch and not ((state >> index) & 1):
                                state = state | (1<<index)
                                break
                    dp[state] = min(dp[state], dp[i]+1)
            
        return -1 if dp[total_number_to_represent_target-1]==float('inf') else dp[total_number_to_represent_target-1]
    
    """
    TC: O(2^T * S*T) T = num letters in target word, S: total num of letters in stickers
SC: O(2^T) : Space used by dp
    """