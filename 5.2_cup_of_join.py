def join(*lists, sep='-'):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)  # adding a list to the end of the result list
        # when i list is finished we'll add the sep at the end of it
        if i < len(lists) - 1:
            result.append(sep)
    return result


# Example 1
print(join([1, 2], [8], [9, 5, 6], sep='@'))

# Example 2
print(join([1, 2], [8], [9, 5, 6]))

# Example 3
print(join([1]))

# Example 4
print(join())
