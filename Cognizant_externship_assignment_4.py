# Working with data structures
## task 1 - working with lists
fav_fruits = ['apple', 'banana', 'orange', 'cherry', 'blueberry', 'pineapple'] ## original list
print("Original List: ", fav_fruits)

fav_fruits.append('watermelon') ## adding a item to the list
print("New List after adding a fruit: ", fav_fruits)

fav_fruits.remove('orange') ## remove a item from the list
print("List after removing a fruit: ", fav_fruits)

print("The list in reverse order: ", fav_fruits[::-1]) ## reversing the list using slicing

## task 2 exploring dictionaries
my_demographics = {
    'name' : 'Mason',
    'age' : '25',
    'city' : 'Manasquan'
} ## creating a dictionary
print('The initial dictionary: ', my_demographics)

my_demographics['favorite color'] = 'purple' ## adding an item to the dictionary
print('The dictionary with an addition: ', my_demographics)

my_demographics['city'] = 'Boulder' ## changing the city demographic
print('The dictionary with a change: ', my_demographics)

for x in my_demographics.keys(): ## print dict keys
  print('Keys: ', x)

for x in my_demographics.values(): ## print dict values
  print('Values: ', x)

## Task 3 using tuples
my_tuple = ('V for Vendetta', 'Losing Days', 'The Great Gatsby') ## create tuple
print('Favorite things: ', my_tuple)

print('Tuple length: ', len(my_tuple)) ## print length of tuple