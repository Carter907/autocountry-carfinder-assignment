AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

PROMPT = """
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. Exit
"""

decision = input(PROMPT)

if (decision == '1'):
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicle in AllowedVehiclesList:
        print(vehicle)
elif (decision == '2'):
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')


