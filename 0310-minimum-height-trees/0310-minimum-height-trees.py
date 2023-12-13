class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
#         I am sharing two of my solutions, one is based on the longest path, and the other is related to Tree DP.

# Longest Path

# It is easy to see that the root of an MHT has to be the middle point (or two middle points) of the longest path of the tree.
# Though multiple longest paths can appear in an unrooted tree, they must share the same middle point(s).

# Computing the longest path of a unrooted tree can be done, in O(n) time, by tree dp, or simply 2 tree traversals (dfs or bfs).
# The following is some thought of the latter.

# Randomly select a node x as the root, do a dfs/bfs to find the node y that has the longest distance from x.
# Then y must be one of the endpoints on some longest path.
# Let y the new root, and do another dfs/bfs. Find the node z that has the longest distance from y.

# Now, the path from y to z is the longest one, and thus its middle point(s) is the answer. Java Solution

# Tree DP

# Alternatively, one can solve this problem directly by tree dp.
# Let dp[i] be the height of the tree when the tree root is i.
# We compute dp[0] ... dp[n - 1] by tree dp in a dfs manner.

# Arbitrarily pick a node, say node 0, as the root, and do a dfs.
# When we reach a node u, and let T be the subtree by removing all u's descendant (see the right figure below).
# We maintain a variable acc that keeps track of the length of the longest path in T with one endpoint being u.
# Then dp[u] = max(height[u], acc)
# Note, acc is 0 for the root of the tree.

#              |                 |
#              .                 .
#             /|\               /|\
#            * u *             * u *
#             /|\
#            / | \
#           *  v  *
# . denotes a single node, and * denotes a subtree (possibly empty).

# Now it remains to calculate the new acc for any of u's child, v.
# It is easy to see that the new acc is the max of the following

# acc + 1 --- extend the previous path by edge uv;

# max(height[v'] + 2), where v != v' --- see below for an example.

#          u
#         /|
#        / |
#       v' v
#       |
#       .
#       .
#       .
#       |
#       .
# In fact, the second case can be computed in O(1) time instead of spending a time proportional to the degree of u.
# Otherwise, the runtime can be quadratic when the degree of some node is Omega(n).
# The trick here is to maintain two heights of each node, the largest height (the conventional height), and the second largest height
# (the height of the node after removing the branch w.r.t. the largest height).

# Therefore, after the dfs, all dp[i]'s are computed, and the problem can be answered trivially.
# The total runtime is still O(n). Java Solution


#https://leetcode.com/problems/minimum-height-trees/discuss/76052/Two-O(n)-solutions
        
        
        
        adjList = defaultdict(list)
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        def dfs(start, visited):
            visited.add(start)
            max_len = 0
            max_path = []
            has_child = False
            for child in adjList[start]:
                if child not in visited:
                    has_child = True
                    l,p=dfs(child,visited)
                    if l > max_len:
                        max_len = l
                        max_path = p
            if not has_child:
                return (1, [start])
            
            #The path is stored in reverse order
            max_path.append(start)
            return (max_len+1, max_path)
        
        
        # Find the path from an arbritary root here 0 to a max possible vertex
        l_max, path = dfs(0, set())
        #The path is stored in reverse order
        
        #Take the vertex you found which was at max distance from the arbritary start node and find a vertex farther from that node. That path is the diameter of the tree. The mid points of the diameter of the tree will form the root of the MHT.
        #Read diameter of a tree here https://cses.fi/book/book.pdf
        l_max, path = dfs(path[0], set())
    
        m = len(path)
        return path[(m-1)//2:(m//2)+1]
    
    
    #This can also be done using tree dp
                        
                        
                    
                    
                    
        
        
            
            
        