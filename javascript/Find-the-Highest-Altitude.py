1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        max_altitude=0
4        altitude=0
5        for g in gain:
6            altitude+=g
7            max_altitude=max(max_altitude,altitude)
8        return max_altitude