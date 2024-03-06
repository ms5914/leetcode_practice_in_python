class SparseVector:
    def __init__(self, nums: List[int]):
        self.ind_num_dict = defaultdict(int)
        for i,n in enumerate(nums):
            if n != 0:
                self.ind_num_dict[i] = n
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # dict_to_use = vec.ind_num_dict if len(vec.ind_num_dict)<len(self.ind_num_dict)
        result = 0
        for k in self.ind_num_dict:
            if k in vec.ind_num_dict:
                result+=self.ind_num_dict[k]*vec.ind_num_dict[k]
        return result
                
                
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)