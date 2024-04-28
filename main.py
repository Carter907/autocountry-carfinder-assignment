
from typing import List


with open('allowed_vehicles.txt', 'r') as vehicles:
    allowed_vehicles: List[str] = [vehicle.strip() for vehicle in vehicles.readlines()]


PROMPT = """********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicles
3. ADD Authorized Vehicle
4. REMOVE Authorized Vehicle 
5. Exit
"""
VEHICLE_SEARCH_PROMPT = """********************************
Please enter the full vehicle name:"""

def remove_vehicle(vehicle: str):
    allowed_vehicles.remove(vehicle)
    write_vehicles();

def add_vehicle(vehicle: str):
    allowed_vehicles.append(vehicle)
    write_vehicles();

def write_vehicles():
    with open('allowed_vehicles.txt', 'w') as vehicles:
        for vehicle in allowed_vehicles:
            vehicles.write(vehicle + '\n')


while (True):
    decision = input(PROMPT)

    if (decision == '1'):
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicle in allowed_vehicles:
            print(vehicle)
    elif (decision == '2'):
        vehicle_name = input(VEHICLE_SEARCH_PROMPT)
        if (vehicle_name in allowed_vehicles):
            print(f'{vehicle_name} is an authorized vehicle')
        else:
            print(f'{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    elif (decision == '3'):
        vehicle_name = input(f'Please Enter the full Vehicle name you would like to ADD:\n')
        add_vehicle(vehicle_name);
        print(f'You have added "{vehicle_name}" as an authorized vehicle')
    elif (decision == '4'):
        vehicle_name = input(f'Please Enter the full Vehicle name you would like to REMOVE:\n')
        choice = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List?\n')
        if choice == 'yes':
            remove_vehicle(vehicle_name)
            print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle')
            
    elif (decision == '5'):
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break;


