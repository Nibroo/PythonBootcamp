people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"
print(people)
#?-----------------------------------------------------------------------------

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
print(result)
#?-----------------------------------------------------------------------------

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(['Colt','Blue','Lisa'])
# Run the tests to make sure you've done this correctly!
print(instructors)
#?-----------------------------------------------------------------------------

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
#?-----------------------------------------------------------------------------
