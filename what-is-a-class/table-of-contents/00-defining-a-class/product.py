#! /usr/bin/python3.12

class Product:
  # Initialize object state
  def __init__( self , name : str , cost : float , price : float ):
    self.name = name
    self.cost = cost
    self.price = price
  # Instance method
  def profit_margin( self ) -> float:
    return self.price - self.cost
