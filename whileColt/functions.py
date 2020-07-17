def product(a,b):
    return a*b

print(product(5,6))
#*-------------------------------------------

days = ['None','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def return_day(num):
    if 1 <= num <= 7:
        return days[num]
    return None

print(return_day(5))
print(return_day(10))
#*-------------------------------------------

nums = [1,2,3,4,5,6,7]

def last_element(which):
    if which:
        return which[-1]
    return None

print(last_element(nums))
#*-------------------------------------------

def number_compare(a,b):
    if a > b:
        return 'First is Greater'
    elif a < b:
        return 'Second is Greater'
    return 'Numbers are equal'

print(number_compare(10,1))
print(number_compare(199,199))
#*-------------------------------------------

def single_letter_count(string, ltr):
    if ltr.lower() in string.lower():
        return string.lower().count(ltr.lower())
    return 0

print(single_letter_count('Python Bootcamp', 'p'))
print(single_letter_count('Iftekhar Nibir', 'p'))
#*-------------------------------------------

def multiple_letter_count(string):
    return {l:string.count(l) for l in string}

print(multiple_letter_count('awesome'))
#*-------------------------------------------

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))
#*-------------------------------------------

def is_palindrome(string):
    string = string.replace(' ','').lower()
    if string == string [::-1]:
        return True
    return False

print(is_palindrome('a man a plan a canal Panama'))
print(is_palindrome('Nibir'))
#*-------------------------------------------

def frequency(lis, search):
    if search in lis:
        return lis.count(search)
    return 'Not Found'

print(frequency([1,2,3,3,'True','False','True'], 'True'))
#*-------------------------------------------

def multiply_even_numbers(nums):
    total = 1
    for n in nums:
        if n%2==0:
            total = total * n
    return total

print(multiply_even_numbers([1,2,3,4,5,6,7,8,9]))
#*-------------------------------------------

def capitalize(string):
    cap = string[0].upper()
    low = string[1:]
    return cap+low

print(capitalize('iftekhar'))
#*-------------------------------------------

def compact(lis):
    return [v for v in lis if v]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))
#*-------------------------------------------

def intersection(l1, l2):
    return [val for val in l1 if val in l2]

print(intersection([1,4,6,9],[2,5,8,9]))
#*-------------------------------------------

def isEven(num):
    return num % 2 == 0
    
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

print(partition([1,2,3,4], isEven))