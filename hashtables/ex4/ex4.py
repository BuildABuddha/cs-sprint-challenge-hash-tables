def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for n in a:
        cache[n] = True
        try:
            cache[n*-1]
            if n != 0:
                result.append(abs(n))

        except KeyError:
            continue

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
