class Solution:
    @staticmethod
    def nextGreatestLetter(letters: list[str], target: str) -> str:
        res = ""
        min_comp = 100
        for i in letters:
            comp = (ord(i) - ord(target))
            if 0 < comp < min_comp:
                min_comp = comp
                res = i
        return res if res == "" else letters[0]


if __name__ == '__main__':
    print(Solution.nextGreatestLetter(["c","f","j"], "c"))
    print(Solution.nextGreatestLetter(["x","x","y","y"], "z"))

