for n in range(0,10,2):
    print(n)

for n in range(1,10,2):
    print(n)

word = 'PYTHON'

for num,let in enumerate(word):
    print(num,let)
    #print(let)

lst1 = ['a','b','c','d','e','f','g']
lst2 = [1,2,3,4,5]
lst3 = ['Y','E','S','N','O']

for item in zip(lst1,lst2,lst3):
    print(item)