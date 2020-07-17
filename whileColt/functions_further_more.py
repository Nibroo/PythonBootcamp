import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
#*----------------------------------------------------------------------

def is_all_strings(smthng):
    return all([type(i) == str for i in smthng])

print(is_all_strings(['n','i','b', 0 ,'r']))
print(is_all_strings(['n','i','b','i','r']))
#*----------------------------------------------------------------------

def max_magnitude(nums):
    return max([abs(n) for n in nums])

print(max_magnitude([300,10,-999]))
#*----------------------------------------------------------------------

def sum_even_values(*args):
    total = [n for n in args if n%2==0]
    return sum(total)

print(sum_even_values(1,6,9,44,99))
#*----------------------------------------------------------------------

def sum_floats(*args):
    return sum(n for n in args if type(n)==float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1))
#*----------------------------------------------------------------------

def interleave(string1, string2):
    string = list(zip(string1, string2))
    string = (''.join(s) for s in string)
    string = "".join(string)
    return string

print(interleave('Nbr','ii '))
#*----------------------------------------------------------------------

def triple_and_filter(nums):
    new_nums = list(filter(lambda n: n%4==0, nums))
    return [n*3 for n in new_nums]

print(triple_and_filter([-4,0,6,8,10,12,36]))
#*----------------------------------------------------------------------

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}, {'first': 'Iftekhar', 'last': 'Nibir'}]

def extract_full_name(dics):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), dics))

print(extract_full_name(names))