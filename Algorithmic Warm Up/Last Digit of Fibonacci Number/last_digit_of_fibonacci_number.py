# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 6

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 6

    if n <= 1:
        return n
    else:
        fibonacci_list = [0] * (n + 1)
        fibonacci_list[1] = 1
        for i in range(2, n + 1):
            fibonacci_list[i] = (fibonacci_list[i - 1] + fibonacci_list[i - 2]) % 10
        return fibonacci_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
