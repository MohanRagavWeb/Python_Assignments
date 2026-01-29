def mutate_string(string, position, character):
    list_a = list(string)
    list_a[position] = character
    return "".join(list_a)
