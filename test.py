def multiple_of_index(arr):
    result = []
    index = 1
    for value in arr:
        if value[index] % index == 0:
            result.append(value)
        index += 1
    return result
