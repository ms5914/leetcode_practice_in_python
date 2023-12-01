class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        adj_list = defaultdict(list)
        visited = set()
        for account in accounts:
            firstemail = account[1]
            
            for email in account[2:]:
                adj_list[firstemail].append(email)
                adj_list[email].append(firstemail)
        
        def dfs(first_email,merged_emails):
            visited.add(first_email)
            merged_emails.append(first_email)
            for email in adj_list[first_email]:
                if not email in visited:
                    dfs(email, merged_emails)
            
            
        for account in accounts:
            name = account[0]
            if not account[1] in visited:
                merged_emails = []
                dfs(account[1], merged_emails)
                merged_emails.sort()
                account_details = [name]+merged_emails
                result.append(account_details)
        
        return result
        
            
                
        