class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        hm = defaultdict(int)
        max_same = 0
        max_len = 0
        for j in range(len(s)):
            hm[s[j]]+=1
            max_same = max(max_same, hm[s[j]])
            if i<=j and j-i+1-max_same>k:
                hm[s[i]]-=1
                i+=1
            max_len = max(max_len, j-i+1)
        return max_len
        






        






# I'm confused about the solution 1. python line 46,
# max_frequency = max(max_frequency, freq_map[s[end]])
# if we move the sliding window from left to right, could the max_frequency got decreased in some cases, eg.
# AAABB, if the sliding window is [0, 3] {A: 3, B: 1} , at [1,4] {A:2, B: 2}
#  k = 0

#  AAABB
#  k = 0

#  A    same_count = 1
#  AA   same_count = 2
#  AAA  same_count = 3
#  AAAB  same_count = 3 total = 4  4-3 > k the window becomes invalid
#  AAB   same_count = 3




# How this works?

# 0
# Hide Replies
# Reply

# damian9687
# Sep 05, 2023
# Yes, it's a brain teaser. The trick is to understand that it doesn't matter, you can keep the max frequency seen so far even if it's not the max frequency of the current window. Because if a higher max_frequency hasn't made a substring valid, a lower frequency won't either. So you will keep iterating until you find a higher frequency than the max_frequency seen so far.

