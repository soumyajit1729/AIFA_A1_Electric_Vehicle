import numpy as np
import copy

# the extended electric vehicle class having 3 extra data
class ElectricVehicle:
  def __init__(self, start, end, battery_charge, charging_rate, discharging_rate,max_battery_capacity,speed):
    self.start = start
    self.end = end
    self.battery_charge = battery_charge
    self.charging_rate = charging_rate
    self.discharging_rate = discharging_rate
    self.max_battery_capacity = max_battery_capacity
    self.speed = speed

    # these 3 data will be required state generation
    self.last_town = start
    self.next_town = start
    self.dist_left = 0
    
    # status of the car
    self.is_charging = False
    self.is_waiting = False
    self.is_on_road = False
  def __str__(self): 
    return "[next town is % s, dist is % s ]" % (self.next_town, self.dist_left) 

# The class for a town's EV Charging station : will be required to see if an EV is already engaged, so that we can see if an EV has to wait or it can directly start charging,
# It will also has cars waiting in-line (for case: A charging, B just came to town, B getting charged and leaving before A-could be optimal)
class CityStation:
  def _init_(self):
    self.charging_status = False
    self.wait_list = []             # There can/cannot be a function to arrange these cars for consideration optimally

# the state class
class State:
  def __init__(self, electric_vehicles_info, towns, time_stamp):
    self.electric_vehicles_info = electric_vehicles_info  # array of cars
    self.time_stamp = time_stamp
    self.city_info = towns

n = 10
car1 = ElectricVehicle(0,3,70, 2, 1, 100, 20)
car2 = ElectricVehicle(1,7,70, 2, 1, 100, 20)
car3 = ElectricVehicle(2,5,70, 2, 1, 100, 20)

cars = [car1, car2, car3]
print(car2)

cities = np.ones(n*n)*100
cities = cities.reshape(n,n)

town = CityStation()
towns = [town]*10

initial_state = State(cars,towns,0)

def get_next_car_choices(car1):
  # if the car is in the middle
  car = copy.deepcopy(car1)
  if car.dist_left != 0:
    print("on way")
    car.dist_left = car.dist_left - car.speed
    if car.dist_left<=0:
      car.dist_left = 0
      car.last_town = car.next_town
    return [car]
  next_states = []
  for i in range(n):
    print("adding")
    if car.battery_charge*car.discharging_rate >= cities[car.next_town][i] and cities[car.next_town][i]>0:
      temp_car = copy.deepcopy(car)
      temp_car.next_town = i
      temp_car.dist_left = cities[car.next_town][i] - temp_car.speed
      temp_car.battery_charge = temp_car.battery_charge - (temp_car.speed/temp_car.discharging_rate)
      temp_car.is_charging = False
      temp_car.is_waiting = False
      temp_car.is_on_road = True
      next_states.append(temp_car.__dict__)
      #print(temp_car.__dict__)
  return next_states

  
car2 = ElectricVehicle(1,7,120, 2, 1, 100, 20)

print(car2)
print(car2.discharging_rate*car2.battery_charge)
next_states = get_next_car_choices(car2)
print(car2.__dict__)
print("----------------")
for i in next_states:
  print(i)