def bubble_sort(the_list):
  """
  Bubble sort passes through the list n - 1 times.
  On each pass, it compares each list item with the next, swapping them if the first is greater than the second.
  Time complexity of O(n^2), but average case can be improved by exiting on a pass with no swapping.
  """

  pass_number = len(the_list) - 1
  swapped = True

  while pass_number > 0 and swapped:
    swapped = False
    for i in range(pass_number):
      if the_list[i] > the_list[i + 1]:
        swapped = True
        the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]

    pass_number = pass_number - 1

  return the_list


if __name__ == '__main__':
  print bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
