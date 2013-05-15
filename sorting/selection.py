def selection_sort(the_list):
  """
  Selection sort is similar to bubble sort, but improves on it by only making one exchange per pass - moving the greatest item to the end.
  """

  for fill_slot in range(len(the_list) - 1, 0, -1):
    position_of_max = 0

    for location in range(1, fill_slot + 1):
      if the_list[location] > the_list[position_of_max]:
        position_of_max = location

    the_list[fill_slot], the_list[position_of_max] = the_list[position_of_max], the_list[fill_slot]

  return the_list

if __name__ == '__main__':
  print selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
