from src.main import add

def test_add():
    # ✅ 正常系
    assert add(2, 3) == 5
    assert add(1, 2, 3) == 6
    assert add(0, 0) == 0
    assert add(5, 5) == 10
    assert add(0, 0, 0) == 0
    assert add(10, 0) == 10
    assert add(3.5, 2.5) == 6.0

    # ✅ 境界値（端の値）
    assert add(0, 10) == 10
    assert add(10, 10) == 20
    assert add(0, 0, 10) == 10
    assert add(10, 10, 10) == 30

    # ❌ 型エラー（-1）
    assert add("a", 1) == -1
    assert add(1, "b") == -1
    assert add("a", "b") == -1
    assert add(None, 1) == -1

    # ❌ 範囲外（-2）
    assert add(-1, 1) == -2
    assert add(1, -1) == -2
    assert add(11, 1) == -2
    assert add(1, 11) == -2
    assert add(0, 0, 11) == -2
