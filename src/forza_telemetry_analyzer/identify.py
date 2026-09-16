import numpy as np

data = np.genfromtxt('telemetry_data.csv', delimiter=',', skip_header=1)

print(data)

def identify_vehicle_model(data):
    # Extract vehicle model from data
    radius = fit_tire_radius(data)






