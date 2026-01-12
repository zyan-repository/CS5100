def CoinGame(N: int, S: list[int]) -> list[int]:
    status = [False] * (N + 1)
    for i in range(1, (N + 1)):
        for s in S:
            # check if there is a move that leads to a losing position for the opponent
            if i - s >= 0 and not status[i - s]:
                status[i] = True
                break
    res = []
    for i, s in enumerate(status):
        # collect all losing positions for the first player, excluding position N
        if s == False and i != N:
            res.append(i)
    return res
print(CoinGame(5, [1, 2, 3, 4, 5]))
print(CoinGame(17, [1,2]))
print(CoinGame(27, [1, 3, 6]))
