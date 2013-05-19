def insertion_sort(the_list):
    for i in range(1, len(the_list)):
        current_value = the_list[i]
        position = i

        while position > 0 and the_list[position - 1] > current_value:
            the_list[position] = the_list[position - 1]
            position = position - 1

        the_list[position] = current_value

    return the_list

if __name__ == '__main__':
    print insertion_sort([54,26,93,17,77,31,44,55,20])