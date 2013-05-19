def shell_sort(the_list):
  sublist_count = len(the_list) // 2

  while sublist_count > 0:
    for start_position in range(sublist_count):
      gap_insertion_sort(the_list, start_position, sublist_count)

    print "After increments of", sublist_count, "the list is", the_list

    sublist_count = sublist_count // 2

  return the_list


def gap_insertion_sort(the_list, start, gap):
  for i in range(start + gap, len(the_list), gap):
    current_value = the_list[i]
    position = i

    while position >= gap and the_list[position - gap] > current_value:
      the_list[position] = the_list[position - gap]
      position = position - gap

    the_list[position] = current_value

if __name__ == '__main__':
  print shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
