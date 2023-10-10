class Solution:
    @staticmethod
    def smallestSufficientTeam(req_skills: list[str], people: list[list[str]]) -> list[int]:
        n = len(req_skills)
        N = 1 << n
        dp = [0] + [float('inf')] * N
        team = [[] for _ in range(N)]
        skillToId = {skill: i for i, skill in enumerate(req_skills)}
        for j in range(len(people)):
            person = 0
            for skill in people[j]:
                if skill in skillToId:
                    person |= (1 << skillToId[skill])
            for skillset in range(N):
                new_skillset = skillset | person
                if dp[new_skillset] > dp[skillset] + 1:
                    dp[new_skillset] = dp[skillset] + 1
                    team[new_skillset] = team[skillset] + [j]
        return team[N - 1]


def main():
    print(Solution.smallestSufficientTeam(["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]))
    print(Solution.smallestSufficientTeam(["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                          [["algorithms", "math", "java"]]))


if __name__ == "__main__":
    main()
