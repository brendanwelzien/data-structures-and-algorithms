def insert_sort(list):
    for index in range(1, len(list)):
        index_position = index
        temporary_position = list[index]

        while index_position > 0 and temporary_position < list[index_position - 1]:
            list[index_position] = list[index_position - 1]
            index_position -= 1
        list[index_position] = temporary_position
    return list

if __name__ == "__main__":
    sortify = insert_sort([8, 4, 23, 42, 16, 15])
    print(sortify)
