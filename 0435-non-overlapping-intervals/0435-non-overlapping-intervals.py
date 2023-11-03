class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        ans = 0
        k = -inf

        #Here k is like a sweep line which is checking for overlaps
        
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                k = min(k, y) #This is the greedy trick. Keep the interval that is shorter
                ans += 1
        
        return ans

       
# The editorial just seems like a trick than actual reasoning.
# I have solved interval problems before, and the most intuitive way to solve them was to sort the intervals based on start-times and not end-times.
# I have solved it using sorting based on start-time and greedy 2 pointers.
# The idea is to first sort all intervals based on start time and then check for conflict, whenever there will be an overlap you will need to remove either one so you can add 1 to the ans but you need to set the prev pointer to the interval with shorter end-time.
# This may be a bit slow but asymptotically it is still O(nlogn) time and O(1) space.
# The intuition behind this approach is much easier to explain during interview.
        

#Imagine an interval like this:

# (1,2),(4,5)(0,6) When we are sweeping through this we should pick (1,2) on the first conflict instead of (0,6) because we'll be able to avoid a later conflict with (4,5)