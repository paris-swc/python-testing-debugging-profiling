import numpy
def find_first(data, element):
    """
    Return the index of the first appearance of ``element`` in
    ``data`` (or -1 if ``data`` does not contain ``element``).
    """
    counter = 0
    while counter <= len(data):
        if data[counter] == element:
            return counter
        counter += 1
    return -1

def check_data(target):
    test_data = [3, 2, 8, 9, 3, 4, 7, 5]
    # We look for a zero in the data
    index = find_first(test_data, target)
    if index != -1:
        print('Data until first occurrence of', target, ':', test_data[:index])
    else:
        print('No occurrence of', target, 'in the data')
