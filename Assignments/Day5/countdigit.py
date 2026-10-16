class Solution:
    def digitCounts(self, n: int) -> int:
        count=0
        for digit in str(n):
            count=count+1
        return count
        pass