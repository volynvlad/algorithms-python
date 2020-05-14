def knuth_morris_pratt(text, pattern):
    fail = _kmp_create_array(pattern)
    str_index = 0
    sub_index = 0
    while str_index < len(text):
        if text[str_index] == pattern[sub_index] \
                and sub_index == len(pattern) - 1:
            return str_index - len(pattern) + 1
        elif text[str_index] == pattern[sub_index]:
            str_index += 1
            sub_index += 1
        elif text[str_index] != pattern[sub_index] and sub_index == 0:
            str_index += 1
        else:
            sub_index = fail[sub_index - 1]
    return -1


def _kmp_create_array(pattern):
    fail = [0]
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            fail.append(j + 1)
            i += 1
            j += 1
        elif pattern[i] != pattern[j] and j == 0:
            fail.append(0)
            i += 1
        else:
            j = fail[j - 1]
    return fail


def boyer_moore(text, pattern):
    shifts = _boyer_moore_create_shifts(pattern)

    i = 0
    text_len = len(text)
    pattern_len = len(pattern)
    while i <= text_len - pattern_len:
        num_of_skips = 0
        j = pattern_len - 1
        while j >= 0:
            if pattern[j] != text[i + j]:
                num_of_skips = shifts[text[i + j]] if text[i + j] in shifts else pattern_len
                break
            j -= 1
        if num_of_skips == 0:
            return i
        i += num_of_skips
    return -1


def _boyer_moore_create_shifts(pattern):
    shift = {}
    for i, x in enumerate(pattern):
        shift[x] = max(1, len(pattern) - i - 1)
    return shift


def rabin_karp(text, pattern):
    def char_to_int(char):
        return ord(char) - ord('a') + 1

    r = 53
    m = 997
    pattern_hash = 0
    current_substring_hash = 0
    degree = 1  # current power of r

    text_len = len(text)
    pattern_len = len(pattern)

    i = 0
    # h(s) = sum_0_n-1(s_i * r ** i) % m
    # calculate hash value for the pattern
    while i < pattern_len:
        print(f"degree = {degree}")
        pattern_hash += char_to_int(pattern[i]) * degree
        pattern_hash %= m

        current_substring_hash += char_to_int(text[text_len - pattern_len + i]) * degree
        current_substring_hash %= m

        if i != pattern_len - 1:
            degree = degree * r % m
        i += 1

    occurrences = []

    i = text_len
    while i >= pattern_len:
        if pattern_hash == current_substring_hash:
            is_pattern_found = True

            j = 0
            while j < pattern_len:
                if text[i - pattern_len + j] != pattern[j]:
                    is_pattern_found = False
                    break
                j += 1

            if is_pattern_found:
                occurrences.append(i - pattern_len)

        if i > pattern_len:
            current_substring_hash = (current_substring_hash - char_to_int(text[i - 1]) * degree % m + m) * r % m
            current_substring_hash = (current_substring_hash + char_to_int(text[i - pattern_len - 1])) % m

        i -= 1

    # print(occurrences)
    return occurrences[-1]


if __name__ == "__main__":
    def test(string_search):
        # string_ = "abbbbc"
        # sub_string1 = "bbc"
        # sub_string2 = "abb"
        # print(string_search(string_, sub_string2))
        # print(string_search(string_, sub_string1))
        with open("book.txt") as f:
            pattern = "Python"
            text = f.read()
            start_index = string_search(text, pattern)
            print(start_index)
            print(text[start_index: start_index + len(pattern)])

    test(knuth_morris_pratt)
    print('-' * 20)
    test(boyer_moore)
    print('-' * 20)
    test(rabin_karp)
