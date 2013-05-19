def merge_sort(the_list):
  print "Splitting ", the_list
  if len(the_list) > 1:
    mid = len(the_list) // 2
    left_half = the_list[:mid]
    right_half = the_list[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        the_list[k] = left_half[i]
        i = i + 1
      else:
        the_list[k] = right_half[j]
        j = j + 1

      k = k + 1

    while i < len(left_half):
      the_list[k] = left_half[i]
      i = i + 1
      k = k + 1

    while j < len(right_half):
      the_list[k] = right_half[j]
      j = j + 1
      k = k + 1

    print "Merging ", the_list
    return the_list

if __name__ == '__main__':
  merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])