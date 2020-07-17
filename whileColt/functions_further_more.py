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

