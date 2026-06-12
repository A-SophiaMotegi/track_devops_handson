from src.main import add
import pytest

def test_add():
  assert add(2, 3) == 5
  assert add(1.2, 3.5) == 4
  assert add(1, 2, 3) == 6
  assert add(0, 0) == 0
  assert add(-1, -2) == -3
  assert add(-1, 2) == 1
  assert add(5, 0) == 5
  assert add(1.9, 1.1) == 3
  assert add(2.5, 2.5) == 5
  assert add(10, -5) == 5
  assert add(3, 3, 3) == 9
  assert add(1, 2, 0) == 3
  assert add(100, 200) == 300
  assert add(0.9, 0.9) == 1
  assert add(1.1, 1.1) == 2
  assert add(-1.5, -1.5) == -3
  assert add("a", 1) == "error"
  assert add(1, "b") == "error"
  assert add("a", "b") == "error"
  assert add(None, 1) == "error"
