class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        ans = 0

        for j in range(n - 1):
            left = [0] * 27
            seen = set()

            # Count distinct characters in s[i..j]
            for i in range(j, -1, -1):
                seen.add(s[i])
                left[len(seen)] += 1

            right = [0] * 27
            seen.clear()

            # Count distinct characters in s[j+1..k]
            for k in range(j + 1, n):
                seen.add(s[k])
                right[len(seen)] += 1

            # Pair substrings having equal distinct counts
            for d in range(1, 27):
                ans += left[d] * right[d]

        return ans
