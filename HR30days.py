# Day 2: Travel Around the World

def make_city_dict(num_cities, refuel, fuel_needed):
    city_dict = {}
    
    for i in range(num_cities):
        city_dict[i] = {'refuel': refuel[i], 'fuel': fuel_needed[i]}
        
    return city_dict

def count_around_the_world_cities(num_cities, capacity, refuel, fuel_needed):
   
    movable = False
    count = 0
    
    city_dict = make_city_dict(num_cities, refuel, fuel_needed)
    
    for i in range(num_cities):
        curr_fuel = 0
        for j in range(i, num_cities + i):
            k = j % num_cities
            if min(city_dict[k]['refuel'], capacity) + curr_fuel >= city_dict[k]['fuel']:
                movable = True
                curr_fuel = curr_fuel + min(city_dict[k]['refuel'], capacity) - (city_dict[k]['fuel'])  
            else:
                movable = False
                break
                
        if movable:
            count += 1
        
    return count
 
    
line = raw_input().split(' ')
num_cities = int(line[0])
capacity = int(line[1])
refuel = map(int, raw_input().split(' '))
fuel_needed = map(int, raw_input().split(' ')) 
print count_around_the_world_cities(num_cities, capacity, refuel, fuel_needed)