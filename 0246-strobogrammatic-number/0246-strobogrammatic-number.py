class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapp = dict()
        mapp['8'] = '8'
        mapp['9'] = '6'
        mapp['6'] = '9'
        mapp['0'] = '0'
        mapp['1'] = '1'
        
        for n in num:
            if n not in mapp:
                return False
        
        for index,value in enumerate(num):
            complement = num[len(num)-1-index]
            if value != mapp[complement]:
                return False
        return True
        