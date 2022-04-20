# removing all occurrences
list_1 = [5, 20, 15, 20, 25, 50, 20]


def occurrence_removal(sample_list, val):
    return [i for i in list_1 if i != val]


new_list = occurrence_removal(list_1, 20)
print(new_list)

