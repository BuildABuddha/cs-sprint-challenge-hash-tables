def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    for i in range(length):
        weight_dict[weights[i]] = i

    for i_1 in range(length):
        try:
            i_2 = weight_dict[limit - weights[i_1]]

            if i_1 < i_2:
                return (i_2, i_1)
            else:
                return (i_1, i_2)

        except KeyError:
            pass

    return None


if __name__ == "__main__":
    weights_1 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_1 = get_indices_of_item_weights(weights_1, 9, 7)
    print(answer_1)