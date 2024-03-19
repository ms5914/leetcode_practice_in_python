class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        s = sum(ribbons)             
        
        # impossible case: when total length sum of all ribbons are less than `k`
        if s < k: return 0
        n = len(ribbons)
        
        
        def ok(mid):                 # is it `ok` to form `k` ribbon with length `mid`?
            cnt = 0
            for r in ribbons:
                cnt += r // mid
            return cnt >= k    
        l, r = 1, max(ribbons)
        
        
        while l <= r:                # binary search
            mid = (l+r) // 2
            if ok(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r         
        