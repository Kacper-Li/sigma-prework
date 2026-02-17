def test_value(input, correct_answer):
    calculated_answer = min_and_max(input)
    correct = (calculated_answer == correct_answer)
    print(f"Correct:  {correct}, Input: {input}")
    print(f"Expected: {correct_answer}")
    print(f"Gotten:   {calculated_answer}")

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
answer1 = [-1,4]
test2 = [20, 50, 12, 6, 14, 8]
answer2 = [6,50]
test3 = [100, -100]
answer3 = [-100,100]

test_value(test1, answer1)
test_value(test2, answer2)
test_value(test3, answer3)