from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides = []
    
    def add_rider(self,rider):
        self.riders.append(rider)
        
    def add_driver(self,driver):
        self.drivers.append(driver)
        
    def __repr__(self) -> str:
        # print(f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}')
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'
class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        #todo set user id dynamically
        self.__id = 0
        self.__nid=nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_ride = None
        self.wallet=0
        self.current_location=current_location
        super().__init__(name, email, nid)
        
    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')
        
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
    
    def update_location(self,current_location):
        self.current_location=current_location
        
    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            #todo: set ride properly
            #todo: set current ride via ride match
            ride_request = Ride_request(self,destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            if ride:
                self.current_ride = ride

    def show_current_ride(self):
        if self.current_ride:
            print(self.current_ride)
        
        
class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet=0
            
    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')
        
    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare= None
        
    def set_driver(self,driver):
        self.driver=driver
        
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self,rider,ammount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    
    def __repr__(self) -> str:
        return f'Ride details Started: {self.start_location} to {self.end_location}'
        
class Ride_request:
    def __init__(self,rider,end_location) -> None:
        self.ride = rider
        self.end_location = end_location
        
class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.available_drivers=drivers
    
    def find_driver(self,ride_request):
         if len(self.available_drivers)>0:
             #todo: find the closet driver of the rider
             driver = self.available_drivers[0]
             ride = Ride(ride_request.rider.current_location, ride_request.end_location)
             driver.accept_ride(ride)
             return ride

class Vehicle(ABC):
    
    speed ={
        'Car':50,
        'bike':60,
        'cng': 15       
    }
    
    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        self.status= 'available'
        super().__init__()
    
    @abstractmethod
    def start_drive(self):
        pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    def start_drive(self):
        self.status = 'unavailable'
        



#check the class integration

niya_jao= Ride_Sharing('Niya Jao')
sakib = Rider("Sakib khan",'sakib@kan.com',1254,'Mohakhali')
niya_jao.add_rider(sakib)

kala_paki = Driver('kala pakhi', 'kala@pakhi.com',5698, 'gulshan 1')
niya_jao.add_driver(kala_paki)
print(niya_jao)
sakib.request_ride(niya_jao,'Uttora')
sakib.show_current_ride()