def intersection(arrays):
    # Not super satisfied with this answer, I'll think it over. It works, though.
    num_arrays = len(arrays)
    counting_dict = {0 : {}}

    for number in arrays[0]:
        counting_dict[0].update({number: True}) 

    for n in range(1, num_arrays):
        counting_dict[n] = {}
        for number in arrays[n]:
            try:
                if counting_dict[n-1][number]:
                    counting_dict[n].update({number: True})
            except KeyError:
                continue

    result = list(counting_dict[num_arrays-1].keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
