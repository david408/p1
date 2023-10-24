def gcd(a: int, b: int) -> int:
    # gcd(a,b) is the largest integer that divides a and b without remainder
    # gcd(a,b) = gcd(a % b, b). why?
    # if q divides a and b then it also divides a-nb
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r


def test_gcd():
    assert gcd(1229, 17) == 1
    assert gcd(17, 1229) == 1
    assert gcd(15, 5) == 5
    assert gcd(5, 15) == 5
    assert gcd(1520273, 3378521) == 1229
    assert gcd(3378521, 1520273) == 1229
    assert gcd(57, 81) == 3
    assert gcd(81, 57) == 3


def egcd(a: int, b: int) -> tuple[int, int]:
    """
    :return: coefficients x,y s.t. ax + by = 1
    """
    x, q = [0, 1], [0, 0]
    _a, _b = a, b
    while True:
        q.append(int(a/b))
        x.append(x[-2] - x[-1]*q[-2])
        if a % b == 0:
            break
        a, b = b, a % b
    # y = (gcd(a,b) - ax)/b
    y = int((b - _a * x[-1])/_b)
    return x[-1], y


def test_egcd():
    test_cases = [(15, 26), (26, 15), (99, 100), (8, 2), (2, 8), (15, 69), (12, 42), (42823, 6409), (6409, 42823)]
    for a, b in test_cases:
        x, y = egcd(a, b)
        assert a*x + b*y == gcd(a, b)


if __name__ == "__main__":
    test_gcd()
    test_egcd()
