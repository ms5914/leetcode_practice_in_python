class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        #Solution 1
#         result = []
#         adj_list = defaultdict(list)
#         visited = set()
#         for account in accounts:
#             firstemail = account[1]
            
#             for email in account[2:]:
#                 adj_list[firstemail].append(email)
#                 adj_list[email].append(firstemail)
                
#                 #We create a star like structure for every account like all the emails in an account are connected to the first email in that account (bidirectionally) and eventually each account which has even 1 common email will become a part of a single connected components. The problem thus reduces to just finding the number of connected components in the graph and adding the name label to them. 
        
#         def dfs(first_email,merged_emails):
#             visited.add(first_email)
#             merged_emails.append(first_email)
#             for email in adj_list[first_email]:
#                 if not email in visited:
#                     dfs(email, merged_emails)
            
            
#         for account in accounts:
#             name = account[0]
#             if not account[1] in visited: #We traverse all the firstemails in an account if they haven't been visited before. That means they are a new component. 
#                 merged_emails = []
#                 dfs(account[1], merged_emails)
#                 merged_emails.sort()
#                 account_details = [name]+merged_emails
#                 result.append(account_details)
        
#         return result
    
    #Solution 2
    #Using disjoint sets
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        disjoint_set = DU(n)
        email_to_group = defaultdict(int)
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_group:
                    email_to_group[email] = i
                else:
                    disjoint_set.union_by_rank(i, email_to_group[email])
        
        root_component_map = defaultdict(list)
        for email in email_to_group.keys():
            group = email_to_group[email]
            root = disjoint_set.find(group)
            root_component_map[root].append(email)
        
        result = []
        for root in root_component_map:
            row = [accounts[root][0]]
            emails = sorted([email for email in root_component_map[root]])
            row = row+emails
            result.append(row)
        
        return result
            
            
                    
                    
                    
                
                
                
    
class DU:
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]
    
    def find(self,x):
        if x == self.parents[x]:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union_by_rank(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x == parent_y:
            return
        elif self.ranks[parent_x] <= self.ranks[parent_y]:
            self.ranks[parent_y]+=self.ranks[parent_x]
            self.parents[parent_x] = parent_y
        else:
            self.ranks[parent_x]+=self.ranks[parent_y]
            self.parents[parent_y] = parent_x

            


            
            
            
        
    
        
        
            
                
        