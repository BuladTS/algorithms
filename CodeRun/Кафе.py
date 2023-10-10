def main():
    with open("input.txt", "r") as file:
        days = int(file.readline())
        price_list = [0 for _ in range(days)]

        for i in range(days):
            price_list[i] = int(file.readline())
    coupons = 0
    dp = [(0, 0) for i in range(days)]
    dp[0] = (price_list[0], 0)
    for i in range(days):
        if coupons == 0:
            pass

        if price_list[i] >= 100:
            coupons += 1


if __name__ == "__main__":
    main()

