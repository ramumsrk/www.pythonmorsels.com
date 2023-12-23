#! /usr/bin/python3.12

# User-defined function
def square( number : int ) -> int:
  return number * number

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
  squared_numbers = map( square , numbers )
  print( type( squared_numbers ) )
  for squared_number in list( squared_numbers ):
    print( F'Number: \'{squared_number}\'' )
