#Exercise 4
#Setting up variables
#Joel Sheppard


cars = 100  																		#anytime cars us called the value 100 will be used
space_in_a_car = 4.0  																#four people can fix in a car, set an a long int
drivers = 30																		#number of drivers who can drive
passengers = 90																		#number of passengers needing rides
cars_not_driven = cars - drivers
#cars_not_driven evaluates to cars minus drivers
													
#cars_driven variable is the same as the drivers variable
cars_driven = drivers

#carpool capacity is cars_driven multiplied by the value of space_in_a_car 
carpool_capacity = cars_driven * space_in_a_car

#evaluates to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
