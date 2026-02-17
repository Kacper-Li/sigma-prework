def min_and_max(array):
    lowest = array[0]
    highest = array[0]
    for item in array:
        if item > highest:
            highest = item
        elif item < lowest:
            lowest = item
    return [lowest, highest]

test1 = [2, 4, 1, 0, 2, -1]
test2 = [20, 50, 12, 6, 14, 8]
test3 = [100, -100]

def test_value(input, correct_answer):
    