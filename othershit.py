states = [
    'Oregon' : 'OR',
    'Florida' : 'FL', 
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
]
cities = [
    'CA' : 'San Francisco',
    'MI': 'Detroit',
    'FL' : 'Jacksonville'
]
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('_' * 10)
print('NY State has: ', cities['NY']) 
print('OR State has: ', cities['OR'])

print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('_' * 10)
print("Michigan's has: ", cities[states['Michigan']])
print("Florida's has: ", cities[statets['Florida']])

print('_' * 10)
for state, abbrev in states.items():
    print(' {} is abbreviated {}' (state, abbrev))

print('_' * 10)
for state, abbrev in states.items():
    print("{state} state is abbreviated {abbrev} and has city {cities[abbrev
    ]}")