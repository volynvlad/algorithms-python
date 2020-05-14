def knuth_morris_pratt(string, sub_string):
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
    return fail


def boyer_moore(string, substring):
    shifts = _boyer_moore_create_shifts(substring)

    i = 0
    text_len = len(string)
    pattern_len = len(substring)
    while i <= text_len - pattern_len:
        num_of_skips = 0
        j = pattern_len - 1
        while j >= 0:
            if substring[j] != string[i + j]:
                num_of_skips = shifts[string[i + j]] if string[i + j] in shifts else pattern_len
                break
            j -= 1
        if num_of_skips == 0:
            return i
        i += num_of_skips
    return -1


def _boyer_moore_create_shifts(sub_string):
    shift = {}
    for i, x in enumerate(sub_string):
        shift[x] = max(1, len(sub_string) - i - 1)
    return shift


def rabin_karp(string, sub_string):
    pass


if __name__ == "__main__":
    def test(string_search):
        string_ = "abbbbc"
        sub_string1 = "bbc"
        sub_string2 = "abb"
        print(string_search(string_, sub_string2))
        print(string_search(string_, sub_string1))
        with open("book.txt") as f:
            sub_string_ = "function"
            text = f.read()
            start_index = string_search(text, sub_string_)
            print(start_index)
            print(text[start_index: start_index + len(sub_string_)])

    test(knuth_morris_pratt)
    print('-' * 20)
    test(boyer_moore)
    print('-' * 20)
    test()
