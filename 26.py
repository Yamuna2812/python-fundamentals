def word_break(s, word_dict):
    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in range(1, len(s)+1):
        for word in word_dict:
            if i >= len(word) and dp[i-len(word)]:
                if s[i-len(word):i] == word:
                    dp[i] = True
                    break
    return dp[len(s)]


s = "leetcode"
word_dict = ["leet", "code"]

print("Can break:", word_break(s, word_dict))
