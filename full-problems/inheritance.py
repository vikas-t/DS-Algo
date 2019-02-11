#!/usr/bin/python


class Vehicle():
    def __init__(self, type, seating):
        self.type = type
        self.seating = seating
    
    def __str__(self):
        return self.type + " " + self.seating
    
    def __info__(self):
        print """
        1. 4 wheeler
        2. Motor operated
        """

class Car(Vehicle):
    def __info__(self, rating):
        print """
        1. Luxury
        2. Rating
        """
      
bus = Vehicle("passenger_carry", "75")
print bus
bus.__info__()
car = Car("personal_vehicle", "4")
print car
car.__info__(5)

