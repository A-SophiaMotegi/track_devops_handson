def add(a, b, c=0):
    # 型チェック
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return -1

    # 範囲チェック
    if not (0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10):
        return -2

    # 正常処理
    return a + b + c
    
