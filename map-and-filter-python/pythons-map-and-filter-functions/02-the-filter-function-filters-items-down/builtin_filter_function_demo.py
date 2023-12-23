#! /usr/bin/python3.12

def is_odd( number : int ) -> bool:
  return True if number % 2 == 1 else False

if __name__ == '__main__':
  numbers : list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
  ]
  odd_numbers : filter = filter( is_odd , numbers )
  print( type( odd_numbers ) )
  for odd_number in list( odd_numbers ):
    print( F'Number: \'{odd_number}\'' )
