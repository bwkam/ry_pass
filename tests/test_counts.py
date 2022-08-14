from main import count_ints, count_letters, count_symbols

def test_count_ints():
    assert count_ints("143242") == 6
    assert count_ints("543") == 3
    assert count_ints("5gy3") == 2

def test_count_letters():
    assert count_letters("ABC") == 3
    assert count_letters("GD42") == 2
    assert count_letters("YH543FGF") == 5

def test_count_symbols():
    assert count_symbols("?>54") == 2
    assert count_symbols("!$#") == 3
    assert count_symbols("kt#5%34#?*&") == 6