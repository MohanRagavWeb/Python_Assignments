def find_runner_up(arr):
    unique_scores = list(set(arr))
    unique_scores.sort()
    return unique_scores[-2]
