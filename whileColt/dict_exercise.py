list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer1 = {list1[i]:list2[i] for i in range(3)}
print(answer1)
#----------------------------------------------------------------------
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#answer2 = dict(person)
answer2 = {i[0]:i[1] for i in person}
print(answer2)
#----------------------------------------------------------------------
answer3 = {}.fromkeys(['a','e','i','o','u'],0)
print(answer3)
#----------------------------------------------------------------------
answer4 = {count: chr(count) for count in range(65,91)}
print(answer4)