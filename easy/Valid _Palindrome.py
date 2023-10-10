class Solution:

    @staticmethod
    def isPalindrome(s: str) -> bool:
        s = s.strip()

        def is_letter(letter: str):
            if letter.isdigit():
                return True
            return letter.upper() != letter.lower()

        i = 0
        j = len(s) - 1
        while i < j:
            while not is_letter(s[j]) and j > i:
                j -= 1

            while not is_letter(s[i]) and i < j:
                i += 1

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution.isPalindrome("race a car"))
    print(Solution.isPalindrome("0P"))

