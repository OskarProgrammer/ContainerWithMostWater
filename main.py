class Solution:
    def maxArea(self, height: List[int]) -> int:
        lista=[0]
        for x in range(len(height)):
            for j in range(len(height)):
                if height[x] < height[j]:
                    pole = height[x] * abs(x-j)
                else:
                    pole = height[j] * abs(x-j)
                if pole > lista[0]:
                    lista[0]=pole
                else:
                    continue
        return max(lista)