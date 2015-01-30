import random
from random import randint
from bicycles import Bicycle, Bike_Shop, Customer, Wheel, Frame, Manufacturer

speedy = Wheel('Speedy', 4, 10)
zippy = Wheel('Zippy', 3, 20)
zoom = Wheel('Zoom', 2, 80)

aluminum = Frame("aluminum", 20, 300)
carbon = Frame("carbon", 10, 600)
steel = Frame("steel", 30, 100)

good_gears = Manufacturer("Good Gears", .1)
best_bikes = Manufacturer("Best Bikes", .15)
sweet_spokes = Manufacturer("Sweet Spokes", .2)

red_racer = Bicycle("Red Racer", speedy, steel, sweet_spokes)
blue_baron = Bicycle("Blue Baron", zippy, steel, sweet_spokes)
green_goblin = Bicycle("Green Goblin", speedy, aluminum, sweet_spokes)
purple_pony = Bicycle("Purple Pony", zippy, aluminum, best_bikes)
silver_star = Bicycle("Silver Star", zippy, carbon, best_bikes)
golden_goose = Bicycle("Golden Goose", zoom, carbon, best_bikes)
pink_porcupine = Bicycle("Pink Porcupine", zoom, aluminum, good_gears)
yellow_yak = Bicycle("Yellow Yak", speedy, carbon, good_gears)
orange_ocelot = Bicycle("Orange Ocelot", zoom, steel, good_gears)

good_gears.models = [pink_porcupine, yellow_yak, orange_ocelot]
best_bikes.models = [golden_goose, silver_star, purple_pony]
sweet_spokes.models = [red_racer, blue_baron, green_goblin]

 
def make_inventory():
  inventory = {}
  for model in good_gears.models:
    inventory[model] = randint(0, 1)
  for model in best_bikes.models:
    inventory[model] = randint(0, 1)
  for model in sweet_spokes.models:
    inventory[model] = randint(0, 1)
  return inventory
    

hot_wheels = Bike_Shop("Hot Wheels", make_inventory(), .10, 0)

arlo = Customer("Arlo", 200, "none")
beatrice = Customer("Beatrice", 500, "none")
ida = Customer("Ida", 1000, "none")

print "Welcome to {}!!".format(hot_wheels.shop_name)
for key in hot_wheels.inventory:
  print "We have {} {} bikes in stock.  A {} costs ${}.".format((hot_wheels.inventory[key]),key.model_name, key.model_name, (key.cost + (key.cost * hot_wheels.margin)))
print "\n"
  
customer_list = [arlo, beatrice, ida]
#retail_price = (bike.cost + (bike.cost * shop.margin))

def can_afford(bike_list, shop, customer):
  affordable_bikes = []  
  for bike in bike_list:
    if (bike.cost + (bike.cost * shop.margin)) < customer.bike_funds:
      affordable_bikes.append(bike)
#  print affordable_bikes  
  return affordable_bikes

def bike_in_stock(inventory):
  bike_on_order = []
  bike_stock = []
  for bike in inventory:
    if inventory[bike] == 0:
      bike_on_order.append(bike)
      print "We need to order more {}.  They will be in stock for the next customer.".format(bike.model_name)
    elif inventory[bike] > 0:
      bike_stock.append(bike)
  return (bike_on_order, bike_stock)

for customer in customer_list:
  can_afford(hot_wheels.inventory, hot_wheels, customer)  
  
  print "We have a customer named {}.  They have ${} to spend.  Their current bike is {}.".format(customer.customer_name, str(customer.bike_funds), customer.bike_owned)
   

  (bike_on_order, bike_stock) = bike_in_stock(hot_wheels.inventory)
  bike_options = can_afford(bike_stock, hot_wheels, customer)
  print "Of the bikes we have in stock, they can afford: "
  if bike_options == []:
    print "We don't have anything in stock in your price range.  Please come back tomorrow."
    customer_list.append(customer)
  else:
    for bike in bike_options:
      print bike.model_name
#    if hot_wheels.inventory[bike] == 0:
#      bike_options.remove(bike)
#      print "We are out of {}".format(bike.model_name)

  
  
#  for bike in bike_options:
#    if hot_wheels.inventory[bike] == 0:
#      print "We need to order more {}".format(bike.model_name)
#      bike_options.remove(bike)
#      bike_on_order.append(bike)

      bike_choice = random.choice(bike_options)
    print "They want to buy a {}.".format(bike_choice.model_name)
    customer.bike_owned = bike_choice
    retail_price = (bike_choice.cost + (bike_choice.cost * hot_wheels.margin))
    print "It costs ${}.".format(retail_price)
    hot_wheels.inventory[bike_choice] -= 1
    print "We now have {} {} in stock.".format(hot_wheels.inventory[bike_choice], bike_choice.model_name,)
    bike_profit = bike_choice.cost * hot_wheels.margin
    print "We made ${} on this bike sale.".format(bike_profit)
    hot_wheels.profit += bike_profit
    print "Our profit so far is ${}.".format(hot_wheels.profit)
    customer.bike_funds -= retail_price
    print "{} has ${} left to spend, and a new {} bike!".format(customer.customer_name, customer.bike_funds, bike_choice.model_name)
  for bike in bike_on_order:
    order_amount = randint(1,2)
    hot_wheels.inventory[bike] = order_amount
    print "We have ordered {} more {} from {}.  They will be in stock for the next customer.".format(order_amount,bike.model_name, bike.manufacturer.name)
  print "\n"  
  