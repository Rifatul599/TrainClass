class Train:
    def __init__(self,train_number):
        self.train_number=train_number
        self.route=[]
        self.current_station_index=0

    def add_station(self,station):
        self.route.append(station)
        print(f"Station {station} added to the route.")

    def remove_station(self,station):
        if self.route:
            self.route.remove(station)
            print(f"Station {station} removed from the route.")
        else:
            print(f"Station {station} not found in the route.")

    def depart(self):
        if self.current_station_index<len(self.route):
            print(f"Train {self.train_number} has departed from {self.route[self.current_station_index]}")
        else:
            print("No more stations to depart from.")

    def arrive(self):
        if self.current_station_index<len(self.route)-1:
            self.current_station_index+=1
            print(f"Train {self.train_number} has arrived at {self.route[self.current_station_index]}")
        else:
            print("Train has reached the final station. No more arrivals.")

    def get_current_station(self):
        if self.current_station_index<len(self.route):
            return self.route[self.current_station_index]
        else:
            return "No current station (train has completed its route)."

    def show_route(self):
        if not self.route:
            print("No stations on the route.")
        else:
            print("Current route.")
            for station in self.route:
                print(f"- {station}")

train=Train("Express-101")
train.add_station("Station A")
train.add_station("Station B")
train.add_station("Station C")
train.show_route()
train.depart()
train.arrive()
print(f"Current station: {train.get_current_station()}")
train.arrive()
train.arrive()
train.remove_station("Station B")
train.show_route()
