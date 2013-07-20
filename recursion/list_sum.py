def list_sum(number_list):
  if len(number_list) == 1:
    return number_list[0]
  else:
    return number_list[0] + list_sum(number_list[1:])

if __name__ == '__main__':
  number_list = [1, 3, 5, 7, 9]

  print 'Numbers: {}'.format(number_list)
  print 'Sum: {}'.format(list_sum(number_list))
