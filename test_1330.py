"""

문제

두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
입력

첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
출력

첫째 줄에 다음 세 가지 중 하나를 출력한다.

    A가 B보다 큰 경우에는 '>'를 출력한다.
    A가 B보다 작은 경우에는 '<'를 출력한다.
    A와 B가 같은 경우에는 '=='를 출력한다.

제한

    -10,000 ≤ A, B ≤ 10,000
"""

def _input():
    a, b = map(int, input().split())
    return a, b

def main(a:int, b:int):
    if -10000 >= a or a >= 10000 or -10000 >= b or b >= 10000:
        raise ValueError

    if a == b:
        result = '=='
    elif a > b:
        result = '>'
    else:
        result = '<'
    return result


def test_001_compare():
    assert main(1, 2) == '<'
    assert main(10, 2) == '>'
    assert main(5, 5) == '=='