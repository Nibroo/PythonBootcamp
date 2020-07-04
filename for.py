lst = [1,2,3,4,5]
for num in lst:
    print('It was '+ str(num))
#------------------------------------------------------------------------------------

lst1 = [1,2,3,4,5]
for even in lst1:
    if even % 2 == 0:
        print('Even: {}'.format(even))                      # TODO Checking if Even
    else:
        print('Odd: {}'.format(even))
#------------------------------------------------------------------------------------

lst_sum = 0
for num in lst:
    lst_sum = lst_sum + num                                 # TODO Finding Sum

print('Total Sum is ' + str(lst_sum))
#------------------------------------------------------------------------------------

for _ in 'Cool':                                            # TODO HOT & COOL
    print('Hot')
#------------------------------------------------------------------------------------

lst2 = [(1,2),(3,4),(5,6),(7,8)]
for a,b in lst2:
    if a%2 == 0:
        print('A: {}'.format(a) + ' is Even')             # TODO Checking which are even
    elif b%2 == 0:
        print('B: {}'.format(b) + ' is Even')
    else:
        print('All Odd')
#------------------------------------------------------------------------------------

dic = {'Best': 'Burger', 'Better': 'Fries', 'Good': 'Pizza'}
print(dic)

for key,values in dic.items():
    print(values)
#------------------------------------------------------------------------------------