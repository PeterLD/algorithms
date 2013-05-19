def quick_sort(the_list):
  quick_sort_helper(the_list, 0, len(the_list) - 1)

  return the_list


def quick_sort_helper(the_list, first, last):
  if first < last:
    split_point = partition(the_list, first, last)

    quick_sort_helper(the_list, first, split_point - 1)
    quick_sort_helper(the_list, split_point + 1, last)


def partition(the_list, first, last):
  pivot_value = the_list[first]

  left_mark = first + 1
  right_mark = last
  done = False

  while not done:
    while left_mark <= right_mark and the_list[left_mark] <= pivot_value:
      left_mark = left_mark + 1

    while the_list[right_mark] >= pivot_value and right_mark >= left_mark:
      right_mark = right_mark - 1

    if right_mark < left_mark:
      done = True
    else:
      the_list[left_mark], the_list[right_mark] = the_list[right_mark], the_list[left_mark]

  the_list[first], the_list[right_mark] = the_list[right_mark], the_list[first]

  return right_mark

if __name__ == '__main__':
  print quick_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])