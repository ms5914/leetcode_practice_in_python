class Solution:
    def __init__(self):
        self.cheapest = float('inf')
        self.intermediate_cheapest = dict()
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k = k+1
        
        if src == dst:
            return 0
        
        
        adj_list = defaultdict(list)
        prices = defaultdict(int)
        
        
        #For every start platform adding all the platforms that we can visited from that platform and related prices. Directed graph. It may contain cycles. 
        for (fr, to, price) in flights:
            adj_list[fr].append(to)
            prices[(fr, to)] = price
            
        q = deque() 
        q.append((src, 0, 0))
        visited = set()
        
        
        while q:
            for i in range(len(q)):
                current_vacation_spot, stops, cost = q.popleft() 
                if stops>k:
                    continue
                if current_vacation_spot == dst:
                    self.cheapest = min(self.cheapest, cost)
                    continue
                if self.cheapest!=float('inf') and self.cheapest < cost:
                    continue
                else:
                    for n in adj_list[current_vacation_spot]:
                        if n in self.intermediate_cheapest and self.intermediate_cheapest[n]<= cost+prices[(current_vacation_spot,n)]:
                            continue
                        self.intermediate_cheapest[n] = cost+ prices[(current_vacation_spot,n)]
                        q.append((n, stops+1, cost+ prices[(current_vacation_spot,n)]))  
                        
        
        # Base conditions after computation
        if self.cheapest == float('inf'):
            return -1
        else:
            return self.cheapest
                
            
            
            
            
            
            
        
        
        