class Solution(object):
    def reverseWords(self, s):
        break_down = s.split()
        huha = []
        for i in range(len(break_down)):
           inverse = break_down[i][::-1]
           huha.append(inverse)
        b = " ".join(huha)
        return b