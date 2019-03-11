list = [1, 2, 3, 4, 5, 6, 8, 9, 10]

def find_missing_number(list):
    for index, item in enumerate(list):
        prev_item = list[index-1]
        if index != 0 and prev_item + 1 != item:
            print('{} is missing from the list'.format(prev_item + 1))

find_missing_number(list)