def kmp(string, sub_string):
    fail = _kmp_create_array(sub_string)
    str_index = 0
    sub_index = 0
    while str_index < len(string):
        if string[str_index] == sub_string[sub_index] \
                and sub_index == len(sub_string) - 1:
            return str_index - len(sub_string) + 1
        elif string[str_index] == sub_string[sub_index]:
            str_index += 1
            sub_index += 1
        elif string[str_index] != sub_string[sub_index] and sub_index == 0:
            str_index += 1
        else:
            sub_index = fail[sub_index - 1]
    return -1


def _kmp_create_array(sub_string):
    fail = [0]
    i = 1
    j = 0
    while i < len(sub_string):
        if sub_string[i] == sub_string[j]:
            fail.append(j + 1)
            i += 1
            j += 1
        elif sub_string[i] != sub_string[j] and j == 0:
            fail.append(0)
            i += 1
        else:
            j = fail[j - 1]
    print(fail)
    return fail


def boyer_moore(string, substring):
    slide = _boyer_moore_bad_char(substring)

    s = 0
    n = len(string)
    m = len(substring)
    while s <= n - m:
        j = m - 1

        while j >= 0 and substring[j] == string[s + j]:
            j -= 1

        if j < 0:
            s += m - slide[string[s + m]] if s + m < n else 1
        else:
            s += max(1, j - slide[string[s + j] if string[s + j] in slide else 0])

    return -1


def _boyer_moore_bad_char(sub_string):
    slide = {}
    for i, x in enumerate(sub_string):
        slide[x] = i + 1
    return slide


if __name__ == "__main__":
    string_ = "abbbbc"
    sub_string1 = "bbc"
    sub_string2 = "abb"
    print(kmp(string_, sub_string2))
    print(kmp(string_, sub_string1))
    with open("book.txt") as f:
        sub_string_ = "function"
        text = f.read()
        start_index = kmp(text, sub_string_)
        print(start_index)
        print(text[start_index: start_index + len(sub_string_)])
    # print(_boyer_moore_create_array("data"))
