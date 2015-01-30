class Bicycle(object):
  def __init__(self, model_name, wheels, frame, manufacturer):
    self.model_name = model_name
    self.weight = 2*wheels.weight + frame.weight
    self.cost = (2*wheels.cost + frame.cost) + ((2*wheels.cost + frame.cost) * manufacturer.margin)
    self.wheels = wheels #expected to be a list of wheel objects
    self.frame = frame
    self.manufacturer = manufacturer
    
class Bike_Shop(object):
  def __init__(self, shop_name, inventory, margin, profit):
    self.shop_name = shop_name
    self.inventory = inventory
    self.margin = margin
    self.profit = profit
    
class Customer(object):
  def __init__(self, customer_name, bike_funds, bike_owned):
    self.customer_name = customer_name
    self.bike_funds = bike_funds
    self.bike_owned = bike_owned

class Wheel(object):
  def __init__(self, model_name, weight, cost):
    self.model_name = model_name
    self.weight = weight
    self.cost = cost
    
class Frame(object):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    self.cost = cost
    
class Manufacturer(object):
  def __init__(self, name, margin):
    self.name = name
    self.models = []
    self.margin = margin
  
  
