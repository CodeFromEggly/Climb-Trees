# H Wells 08/2022
# This script will update the file 'tree_database.csv', based upon user input.

# When ran, ask for: latitude, longitude, difficulty, name
import csv





print("Okay - Let's add a tree\n")


# Lat & long:

# Initially, let's assume input is only in decimal degrees.
latitude = input("Please enter latitude [DD]:   ")

longitude = input("and enter longitude [DD]:    ")


# Difficulty will be added as a number, the code will append 'T'
difficulty = input("Please enter a numerical rank for said tree:    ")
difficulty = "".join(["T",difficulty])

print("You're adding a " + difficulty + " tree at: " + latitude + " lat, ", longitude, " long.")

name = input("Add a custom name? [y/n]  ")
if (name.lower() == 'y') :
    name = input("Enter the custom name:    ")
else :
    # A default name for now. In the future it could be named Tree X where X is its number in the database
    name = "Tree"



# Can now update the CSV file

filename = 'test_database.csv'
f = open(filename,"a")
tup1 = (latitude, longitude, name,  difficulty)
writer = csv.writer(f)
writer.writerow(tup1)

f.close()

"""
new_tree = pd.DataFrame({'Decimal Lat': [latitude],
    'Decimal Long': [longitude],
    'Name': [name],
    'Difficulty': [difficulty]})


new_tree




new_tree.to_csv(filename, mode='a', index=False, header=False)

updated_database = pd.read_csv(filename)
print(updated_database)

"""
