class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, (len(h) - 1)
        m = 0 
        while l < r:
            hth = min(h[l],h[r])
            wth = r - l
            area = hth * wth
            m = max(area,m)
            if h[l] < h[r]:
                l+=1
            else:
                r-=1

        return m

