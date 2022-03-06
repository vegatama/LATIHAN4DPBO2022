from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

from Person import Person
from Job import Job
from Driver import Driver

# object instantiation
Vehicles = [Vehicle("avgas", 150), Vehicle("Jet Fuel", 400), Vehicle("avgas", 600), Vehicle("Diesel", 1500), Vehicle("petroleum", 3000)]

Airplanes = [Airplane("AIRBUS A318", 2, 34.1), Airplane("AIRBUS A320", 1, 35.8), Airplane("AIRBUS A330-200", 4, 60.3), 
            Airplane("BOEING 757-300", 3, 38.1), Airplane("BOEING 777F", 5, 64.8)]

Airplanes[0].setfuelType("avgas")
Airplanes[0].setmaxPassengers(150)
Airplanes[1].setfuelType("avgas")
Airplanes[1].setmaxPassengers(150)
Airplanes[2].setfuelType("Jet Fuel")
Airplanes[2].setmaxPassengers(400)
Airplanes[3].setfuelType("avgas")
Airplanes[3].setmaxPassengers(150)
Airplanes[4].setfuelType("avgas")
Airplanes[4].setmaxPassengers(400)

Ships = [Ship(4, "frigate", "Japan"), Ship(3, "helicopter destroyer", "Japan"), Ship(5, "Submarine", "Japan"), 
        Ship(7, "Destroyer", "USA"), Ship(2, "landing platform dock", "USA")]

Ships[0].setfuelType("Diesel")
Ships[0].setmaxPassengers(1500)
Ships[1].setfuelType("petroleum")
Ships[1].setmaxPassengers(3000)
Ships[2].setfuelType("Diesel")
Ships[2].setmaxPassengers(1500)
Ships[3].setfuelType("Diesel")
Ships[3].setmaxPassengers(1500)
Ships[4].setfuelType("petroleum")
Ships[4].setmaxPassengers(3000)

jobs = [Job(438192831937 , "Lion Air", "Pilot"), Job(438392231234 , "Airbus", "Project Lead"), Job(2311952339991 , "Boeing", "Software Engineer"),
       Job(4421943335981 , "Evergreen", "ship captain"), Job(4421252339992 , "Mitsubishi", "Engineer")]

Drivers = [Driver(12230211000111 , "23/01/2025", "Small Ship"), Driver(12230211000112 , "21/12/2026", "Medium Ship"), Driver(12230211000113 , "13/09/2024", "Small Aircraft"),
          Driver(12230211000114 , "16/02/2030", "Medium Aircraft"), Driver(12230211000115 , "11/06/2029", "Large Aircraft")]

for x in range(2):
    Drivers[x].setNIP(4421943335981)
    Drivers[x].setcompanyName("Evergreen")
    Drivers[x].setposition("ship captain")

for x in range(3):
    Drivers[x+2].setNIP(438192831937)
    Drivers[x+2].setcompanyName("Lion Air")
    Drivers[x+2].setposition("Pilot")

Persons = [Person(5819000738918671 , "Andi Hermawan", "M"), Person(5819002758958642 , "Yudi Herlambang", "M"), Person(4119022753955645 , "Nichole Adams", "F"),
          Person(5319082728968445 , "Rei Yasuda", "F"), Person(7419432256978832 , "Naki Hajime", "M")]

# output
print("class Vehicle:")
for x in range(5):
    Vehicles[x].printVehicle()
    if x == 2:
        Vehicles[x].Move()
    print("")

print("class Airplane:")
for x in range(5):
    Airplanes[x].printAirplane()
    Airplanes[x].printVehicle()
    print("")

print("class Ship:")
for x in range(5):
    Ships[x].printShip()
    Ships[x].printVehicle()
    print("")

print("class job:")
for x in range(5):
    jobs[x].printJob()
    print("")

print("class Driver:")
for x in range(5):
    Drivers[x].printJob()
    Drivers[x].printDriver()
    print("")

print("class Person:")
for x in range(5):
    Persons[x].printPerson()
    if x == 2:
        Persons[x].sleep()
    print("")