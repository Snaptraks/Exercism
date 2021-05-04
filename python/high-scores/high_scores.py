def latest(scores: list):
    return scores[-1]


def personal_best(scores: list):
    return max(scores)


def personal_top_three(scores: list):
    sorted_scores = sorted(scores, reverse=True)
    # prevent IndexError
    return sorted_scores[:min(len(sorted_scores), 3)]
