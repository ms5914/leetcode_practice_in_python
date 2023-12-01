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
                
                #We create a star like structure for every account like all the emails in an account are connected to the first email in that account (bidirectionally) and eventually each account which has even 1 common email will become a part of a single connected components. The problem thus reduces to just finding the number of connected components in the graph and adding the name label to them. 
        
        def dfs(first_email,merged_emails):
            visited.add(first_email)
            merged_emails.append(first_email)
            for email in adj_list[first_email]:
                if not email in visited:
                    dfs(email, merged_emails)
            
            
        for account in accounts:
            name = account[0]
            if not account[1] in visited: #We traverse all the firstemails in an account if they haven't been visited before. That means they are a new component. 
                merged_emails = []
                dfs(account[1], merged_emails)
                merged_emails.sort()
                account_details = [name]+merged_emails
                result.append(account_details)
        
        return result
        
            
                
        