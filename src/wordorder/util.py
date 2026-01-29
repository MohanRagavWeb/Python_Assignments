def count_words(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    unique_count = len(word_count)
    counts = list(word_count.values())

    return unique_count, counts
