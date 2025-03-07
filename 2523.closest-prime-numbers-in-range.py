#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = self._sieve_of_eratosthenes(right)
        all_primes = [i for i in range(left, right + 1) if sieve[i]]

        closest_primes = [-1, -1]
        if len(all_primes) < 2:  # noqa: PLR2004
            return closest_primes

        min_difference = right - left + 1
        for i in range(len(all_primes) - 1):
            n1, n2 = all_primes[i], all_primes[i + 1]
            if n2 - n1 >= min_difference:
                continue
            min_difference = n2 - n1
            closest_primes = [n1, n2]
        return closest_primes

    def _sieve_of_eratosthenes(self, n: int) -> list[bool]:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for i in range(2, int(n**0.5 + 1)):
            if not sieve[i]:
                continue
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
        return sieve


# @lc code=end
