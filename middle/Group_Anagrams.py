import collections


class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        dp = collections.defaultdict(list)
        for i in strs:
            dp[''.join(sorted(i))].append(i)
        return list(dp.values())


def main():
    print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution.groupAnagrams([""]))
    print(Solution.groupAnagrams(["a"]))


if __name__ == "__main__":
    main()
