# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    for path in files:
        filename = path.rsplit('/',1)[1]
        try:
            cache[filename]
        except KeyError:
            cache[filename] = []
        finally:
            cache[filename].append(path)

    for query in queries:
        try:
            result.extend(cache[query])
        except KeyError:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
