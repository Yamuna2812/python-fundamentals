def is_palindrome(s):
    return s == s[::-1]


def partition(s, path, result):
    if not s:
        result.append(path)
        return

    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            partition(s[i:], path + [s[:i]], result)


string = input("Enter string: ")
result = []

partition(string, [], result)

for r in result:
    print(r)
