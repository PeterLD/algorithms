def move_tower(height, pole1, pole2, pole3):
  if height >= 1:
    move_tower(height - 1, pole1, pole3, pole2)
    move_disk(pole1, pole3)
    move_tower(height - 1, pole2, pole1, pole3)


def move_disk(from_pole, to_pole):
  print 'Moving disk from {from_pole} to {to_pole}'.format(from_pole=from_pole, to_pole=to_pole)


if __name__ == '__main__':
  move_tower(3, 'A', 'B', 'C')
