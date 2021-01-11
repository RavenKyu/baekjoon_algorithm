"""

문제

시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
입력

첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력

시험 성적을 출력한다.

"""

def _input():
    v = int(input())
    return v

def main(v:int):
    if 0 > v > 100:
        raise ValueError

    if 90 <= v >= 100:
        result = 'A'
    elif 80 <= v >= 89:
        result = 'B'
    elif 70 <= v >= 79:
        result = 'C'
    elif 60 <= v >= 69:
        result = 'D'
    else:
        result = 'F'
    return result

def test_score():
    assert 'A' == main(100)
    assert 'B' == main(91)
    assert 'C' == main(82)
    assert 'D' == main(74)
    assert 'F' == main(50)