class Person:
    def __init__(self,name):
        self.name = name
    
    
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers (self, person):

        if not isinstance(person, Person):
            print("Solo se pueden subir objetos de tipo Person.")
            return
        
        if person in self.passengers:
            print(f"{person.name} ya está en el bus.")
            return
        
        if self.max_passengers > len(self.passengers) :
            self.passengers.append(person)
            print ( f"Pasajero {person.name} ya ingreso al autobus")
        else:
            print("El bus esta a su capacidad màxima, debe esperar el siguiente bus")

    
    def remove_passenger (self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print (f"el pasajero {person.name} se ha retirado del autobus.")
        
        else:
            print( f"El pasajero {person.name} no se encuentra en el autobus")


if __name__ == "__main__":

    bus_1 = Bus(max_passengers=5)  

    first_person = Person("juan")
    second_person = Person("Javier")
    third_person = Person("Jose")
    fourth_person = Person("Eva")
    fifth_person = Person("Felipe")
    sixth_person = Person("Fabian")


    bus_1.add_passengers(first_person)
    bus_1.add_passengers(second_person)
    bus_1.add_passengers(third_person)
    bus_1.add_passengers(fourth_person)
    bus_1.add_passengers(fifth_person)
    bus_1.add_passengers(sixth_person)

    bus_1.remove_passenger(second_person)
    bus_1.remove_passenger(fifth_person)

    bus_1.add_passengers(sixth_person)
