import math

def prepare_connected_cities(distance_dict):
    connected_cities = {}
    for k in distance_dict:
        cities = tuple(k)
        connected_cities.setdefault(cities[0], set())
        connected_cities.setdefault(cities[1], set())
        connected_cities[cities[0]].add(cities[1])
        connected_cities[cities[1]].add(cities[0])
    return connected_cities

def prepare_shortest_path(start_city, end_city, distance_and_previous_city_table):
    current_city = end_city
    shortest_path = end_city  # Reverse path
    while True:
        previous_city = distance_and_previous_city_table[current_city]['previous_city']
        if previous_city == start_city:
            break
        shortest_path += previous_city
        current_city = previous_city
    return start_city + shortest_path[::-1]  # Actual path

def get_city_with_minimum_distance(current_city, connected_cities, visited_cities, table):
    minimum_distance = math.inf
    for connected_city in connected_cities[current_city]:
        if connected_city in visited_cities:
            continue
        if table[connected_city]['shortest_distance'] < minimum_distance:
            minimum_distance = table[connected_city]['shortest_distance']
            current_city = connected_city
    return current_city

def update_shortest_distance_and_previous_city(current_city, connected_cities, table, distance_dict, visited_cities):
    for connected_city in connected_cities[current_city]:
        if connected_city in visited_cities:
            continue
        current_distance = table[current_city]['shortest_distance'] + distance_dict[frozenset([current_city, connected_city])]
        if current_distance < table[connected_city]['shortest_distance']:
            table[connected_city]['shortest_distance'] = current_distance
            table[connected_city]['previous_city'] = current_city

def get_shortest_path(start_city, end_city, distance_dict):
    all_cities = frozenset().union(*[k for k in distance_dict.keys()])
    connected_cities = prepare_connected_cities(distance_dict)
    table = {city: {"shortest_distance": math.inf, "previous_city": None} for city in all_cities}
    table[start_city]['shortest_distance'] = 0
    visited_cities = []
    unvisited_cities = list(all_cities)
    current_city = start_city
    while True:
        # For every connected city of current city, calculate the shortest distance & previous node
        update_shortest_distance_and_previous_city(current_city, connected_cities, table, distance_dict, visited_cities)
        visited_cities.append(current_city)
        unvisited_cities.remove(current_city)
        if not unvisited_cities:
            break
        # Get the next city from unvisited connected cities which has shorter distance from the current city
        # and then mark it as current city
        current_city = get_city_with_minimum_distance(current_city, connected_cities, visited_cities, table)

    shortest_path = prepare_shortest_path(start_city, end_city, table)

    print(f"Shortest distance from {start_city} to {end_city} is {table[end_city]['shortest_distance']}")
    print(f"Shortest path: {shortest_path}")


# Test
# distance_dict = {
#     frozenset(["A", "B"]): 2,
#     frozenset(["A", "D"]): 8,
#     frozenset(["B", "E"]): 6,
#     frozenset(["B", "D"]): 5,
#     frozenset(["D", "E"]): 3,
#     frozenset(["D", "F"]): 2,
#     frozenset(["F", "C"]): 3,
#     frozenset(["E", "C"]): 9,
#     frozenset(["E", "F"]): 1
# }
#
# get_shortest_path("A", "C", distance_dict)
