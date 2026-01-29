def merge_the_tools(s, k):
    result = []

    for i in range(0, len(s), k):
        chunk = s[i:i+k]
        seen = ""
        for char in chunk:
            if char not in seen:
                seen += char
        result.append(seen)

    return result
