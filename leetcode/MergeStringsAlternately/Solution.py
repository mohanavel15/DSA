class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = list(word1)
        l2 = list(word2)
        l1l = len(l1)
        l2l = len(l2)
        if l1l > l2l:
            for i in range(l1l-l2l):
                l2.append("")
        elif l2l > l1l:
            for i in range(l2l-l1l):
                l1.append("")
        return "".join([a+b for (a, b) in zip(l1, l2)])