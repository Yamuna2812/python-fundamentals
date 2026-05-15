from collections import deque

def word_ladder(begin, end, word_list):
    word_set = set(word_list)
    queue = deque([(begin, 1)])

    while queue:
        word, length = queue.popleft()

        if word == end:
            return length

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append((new_word, length + 1))
    return 0


begin = "hit"
end = "cog"
words = ["hot","dot","dog","lot","log","cog"]

print("Steps:", word_ladder(begin, end, words))
