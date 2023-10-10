class Solution:
    @staticmethod
    def asteroidCollision(asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            flag = True
            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()

                flag = False
                break
            if flag:
                stack.append(asteroid)
        return stack


def main():
    print(Solution.asteroidCollision([5, 10, -5]))
    print(Solution.asteroidCollision([8, -8]))
    print(Solution.asteroidCollision([10, 2, -5]))


if __name__ == "__main__":
    main()
