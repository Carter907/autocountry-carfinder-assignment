AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

PROMPT = """********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicles
3. ADD Authorized Vehicle
4. Exit
"""
VEHICLE_SEARCH_PROMPT = """********************************
Please enter the full vehicle name:"""
while (True):
    decision = input(PROMPT)

    if (decision == '1'):
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicle in AllowedVehiclesList:
            print(vehicle)
    elif (decision == '2'):
        vehicle_name = input(VEHICLE_SEARCH_PROMPT)
        if (vehicle_name in AllowedVehiclesList):
            print(f'{vehicle_name} is an authorized vehicle')
        else:
            print(f'{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    elif (decision == '3'):
        vehicle_name = input(f'Please Enter the full Vehicle name you would like to add:')
        AllowedVehiclesList.append(vehicle_name);
        print(f'You have added "{vehicle_name}" as an authorized vehicle')

    elif (decision == '4'):
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break;


