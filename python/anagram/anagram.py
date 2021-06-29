from collections import Counter


def find_anagrams(word, candidates):
    word_lower = word.lower()
    counter_word = Counter(word_lower)
    anagrams = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if word_lower == candidate_lower:
            continue

        if Counter(candidate_lower) == counter_word:
            anagrams.append(candidate)

    return anagrams
