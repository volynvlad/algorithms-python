from substring.substring import kmp


def test_string():
    string = "abbbbc"
    sub_string1 = "bbc"
    sub_string2 = "abb"
    assert kmp(string, sub_string2) == 0
    assert kmp(string, sub_string1) == 3
