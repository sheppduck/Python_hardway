#Exercise 5
#More with variables
#Joel Sheppard

# -*- coding: utf-8 -*-

# Begin setting up variables
name = 'Joel F. Sheppard'
age = 47 #not a lie
height = 73.0 #inches
weight = 187 #lbs
eyes = 'Brown'
teeth = 'white'
hair = 'Brown'
metric_conversion = 2.74

# Print statements using variables set up above
print "Let's talk about %s." % name
#print "He's %d centimeters tall." % (height * metric_conversion)
print "He's %f centimeters tall." % (height * metric_conversion)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
#print "He's got %r eyes and %r hair." % (eyes, hair)
print "his teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d  I get %d." % (age, height, weight, age + height + weight)
