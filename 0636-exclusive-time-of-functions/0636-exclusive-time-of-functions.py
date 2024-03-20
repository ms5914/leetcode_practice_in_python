class Solution:
    def exclusiveTime(self, n, logs):
        ans, stack = [0]*n, []
        for log in logs:
            f_id, event, time = log.split(':') 
            f_id, time = int(f_id), int(time)
            if event=='start':
                if stack:
                    ans[stack[-1][0]] += time-stack[-1][1]
                stack.append([f_id, time])
            else:
                popped = stack.pop()
                ans[popped[0]] += time-popped[1]+1
                if stack:
                    stack[-1][1] = time+1
        return ans