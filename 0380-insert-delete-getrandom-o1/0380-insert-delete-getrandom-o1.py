import random
class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.li = [0 for i in range(2*pow(10,5))]
        self.index = 0
        
        
    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.hm[val] = self.index
        self.li[self.index] = val
        self.index+=1
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.hm:
            return False
        target_index = self.hm[val]
        tmp = self.li[self.index-1]
        self.li[self.index-1] = self.li[target_index]
        self.li[target_index] = tmp
        self.hm[tmp] = target_index
        self.index=self.index-1
        del self.hm[val]
        return True
        
        

    def getRandom(self) -> int:
        rand_ind = random.randint(0, self.index-1)
        return self.li[rand_ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()