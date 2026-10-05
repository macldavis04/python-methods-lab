def max_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def max_of_three(num1, num2, num3):
    return max_of_two_numbers(max_of_two_numbers(num1, num2), num3)


def is_character_a_vowel(char):
    return len(char) == 1 and char.lower() in "aeiou"


def count_arguments(*args):
    return len(args)


def reverse_string(text):
    return text[::-1]


def find_longest_word(word_list):
    longest = 0
    for word in word_list:
        if len(word) > longest:
            longest = len(word)
    return longest


def filter_long_words(word_list, min_length):
    return [word for word in word_list if len(word) > min_length]


if __name__ == "__main__":
    print("Testing max_of_two_numbers:")
    print(f"max_of_two_numbers(5, 3) = {max_of_two_numbers(5, 3)}")
    print(f"max_of_two_numbers(2, 8) = {max_of_two_numbers(2, 8)}")

    print("\nTesting max_of_three:")
    print(f"max_of_three(5, 3, 8) = {max_of_three(5, 3, 8)}")
    print(f"max_of_three(1, 9, 4) = {max_of_three(1, 9, 4)}")

    print("\nTesting is_character_a_vowel:")
    print(f"is_character_a_vowel('a') = {is_character_a_vowel('a')}")
    print(f"is_character_a_vowel('B') = {is_character_a_vowel('B')}")
    print(f"is_character_a_vowel('E') = {is_character_a_vowel('E')}")

    print("\nTesting count_arguments:")
    print(f"count_arguments(1, 2, 3) = {count_arguments(1, 2, 3)}")
    print(f"count_arguments('hello', 'world') = {count_arguments('hello', 'world')}")

    print("\nTesting reverse_string:")
    print(f"reverse_string('hello world') = '{reverse_string('hello world')}'")
    print(f"reverse_string('python') = '{reverse_string('python')}'")

    print("\nTesting find_longest_word:")
    words = ['python', 'java', 'javascript']
    print(f"find_longest_word({words}) = {find_longest_word(words)}")

    print("\nTesting filter_long_words:")
    words = ['python', 'java', 'go', 'javascript']
    print(f"filter_long_words({words}, 4) = {filter_long_words(words, 4)}")