# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return gcd(b, a_prime)


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    # a x b = LCM(a, b) * GCD(a, b)
    # LCM(a, b) = a x b / GCD(a, b)
    return a * b / gcd(a, b)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
