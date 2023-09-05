class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numsfound = {}
        # for i in nums:
        #     if not numsfound.get(i):
        #         numsfound[i] = 1
        #     else:
        #         numsfound[i] += 1
        
        # for k in numsfound.keys():
        #     if numsfound[k] == 1:
        #         return k

        # numsfound = []
        # for i in nums:
        #     if i not in numsfound:
        #         numsfound.append(i)
        #     else:
        #         numsfound.remove(i)
        
        # return numsfound[0]

        # numsfound = {}
        # for i in nums:
        #     if numsfound.get(i):
        #         numsfound.pop(i)
        #     else:
        #         numsfound[i] = True
        # return list(numsfound.keys())[0]

        unique = 0
        for i in nums:
            unique = unique ^ i
        return unique