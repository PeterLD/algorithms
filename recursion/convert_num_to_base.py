def convert_num_to_base(num, base):
  conversion_string = '0123456789ABCDEF'

  if num < base:
    return conversion_string[num]
  else:
    return convert_num_to_base(num // base, base) + conversion_string[num % base]

if __name__ == '__main__':
  num = 1453
  base = 16

  print '{num} in base {base}: {result}'.format(num=num, base=base, result=convert_num_to_base(num, base))