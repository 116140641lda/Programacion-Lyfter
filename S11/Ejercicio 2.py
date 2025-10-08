class Person:
    def __init__(self,name):
        self.name = name
    
    
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers (self, Person):
        if self.max_passengers < 12 :
            self.passengers.append(Person)
            print ( f"Pasajero {Person.name} ya ingreso al autobus")
        else:
            print("El bus esta a su capacidad màxima, debe esperar el siguiente bus")

    
    def remove_passenger (self, Person):
        if Person in self.passengers:
            self.passengers.remove(Person)
            print (f"el pasajero {Person.name} se ha retirado del autobus.")
        
        else:
            print( f"El pasajero {Person.name} no se encuentra en el autobus")


if __name__ == "__main__":

    bus_1 = Bus(max_passengers=5)  

    first_person = Person("juan")
    second_person = Person("Javier")
    third_person = Person("Jose")
    fourth_person = Person("Eva")
    fifth_person = Person("Felipe")


    bus_1.add_passengers(first_person)
    bus_1.add_passengers(second_person)
    bus_1.add_passengers(third_person)
    bus_1.add_passengers(fourth_person)
    bus_1.add_passengers(fifth_person)

    bus_1.remove_passenger(second_person)
    bus_1.remove_passenger(fifth_person)
