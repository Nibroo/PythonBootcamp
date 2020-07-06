def even_check(num_list):
    return num_list%2 == 0

nums = [1,2,3,4,5]

resm = list(map(even_check,nums))
resf = list(filter(even_check,nums))

print('Output using Map Func: ' + str(resm))
print('Output using Filter Func: ' + str(resf))
#----------------------------------------------------------------

names = ['Nibir', 'Nihan', 'Tihan']

reslm = list(map(lambda x: x[::-1], names))
reslf = list(filter(lambda x: x[0], names))

print('Output using Map & Lamda Func: ' + str(reslm))
print('Output using Filter & Lamda Func: ' + str(reslf))