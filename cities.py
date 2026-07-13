cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Bangalore"]

# Middle city
print("Middle city:", cities[len(cities)//2])

# First 3 cities
print("First 3 cities:", cities[:3])

# Sort cities
cities.sort()
print("Sorted cities:", cities)

# Append new city
cities.append("Kolkata")
print("After append:", cities)

# Remove first city
cities.pop(0)
print("After removing first city:", cities)

# Function to find length
def city_count(city_list):
    return len(city_list)

print("Number of cities:", city_count(cities))