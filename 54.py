from collections import defaultdict

def find_ladders(begin, end, word_list):
    word_set = set(word_list)
    layer = {begin: [[begin]]}

    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == end:
                return layer[word]

        for word in layer:
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]

        word_set -= set(new_layer.keys())
        layer = new_layer

    return []
