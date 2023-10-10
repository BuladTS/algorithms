class Solution:
    @staticmethod
    def findPrimePairs(n: int) -> list[list[int]]:
        primes = _sieveEratosthenes(n + 1)
        result = []
        for i in range(2, (n // 2) + 1):
            if primes[i] and primes[n - i]:
                result.append([i, n - i])

        return result
        # result = []
        #
        # def isPrime(num: int) -> bool:
        #     for i in range(2, round(num ** 0.5) + 1):
        #         if num % i == 0:
        #             return False
        #     return True
        #
        # for i in range(2, (n // 2) + 1):
        #     if isPrime(i) and isPrime(n - i):
        #         result.append([i, n - i])
        # return result


def _sieveEratosthenes(n: int) -> list[bool]:
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return primes


def main():
    print(Solution.findPrimePairs(10))
    print(Solution.findPrimePairs(2))


if __name__ == '__main__':
    main()
