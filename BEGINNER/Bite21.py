cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    return ", ".join(cars["Jeep"]

def get_first_model_each_manufacturer(cars=cars):
    return [cars[x][0] for x in cars]


def get_all_matching_models(cars=cars, grep='trail'):
    x =  [cars for x in cars.values() for cars in x if grep.lower() in cars.lower()]
    return sorted(x)

def sort_car_models(cars=cars):
    x = {}
    
    for key, values in cars.items():
        x[key] = sorted(values)
    
    return x
