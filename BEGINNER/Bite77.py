def uncommon_cities(my_cities, other_cities):
    return len(set(my_cities) ^ set(other_cities))
    
