def decrement_list(l):
    return list(map(lambda n: n-1, l))

print(decrement_list([10,20,30,40,50,60]))
#*----------------------------------------------------------------------

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))
print(inactive_users)

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]
print(inactive_users2)

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))
print(usernames)

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(usernames2)
#*----------------------------------------------------------------------

def remove_negatives(nums):
    return list(filter(lambda n: n>=0, nums))

print(remove_negatives([-100,-99,-1,0,1,99,100]))