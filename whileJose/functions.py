def even_check(num_list):           #* Return all the Even Numbers from the list

    even_n = []                     #? Placeholder list

    for n in num_list:
        if n%2==0:
            even_n.append(n)
        else:
            pass
    
    return even_n

result = even_check([1,2,3,5,7,9,10])
print('The Even list: ' + str(result))
#----------------------------------------------------------------------------------------

work_hours = [('Nibir',500),('Nihan',300),('Tihan',100),('No One',700)]

def eom(work_hours):                #* Finding the most work-hour Employee

    c_max = 0                           #? PLaceholder
    c_eom = ''                          #? PLaceholder

    for em,h in work_hours:
        if h > c_max:
            c_max = h
            c_eom = em
        else:
            pass

    return (c_eom,c_max)

name,hours = eom(work_hours)

print(name + ' has worked for ' + str(hours) + ' long Hours')
#-----------------------------------------------------------------------------------------

def myfunc(st):                                         #! UPPERCASE ALL EVEN NUMBER LETTERS
    
    res = []

    for i in range(len(st)):
        if i % 2 == 0:
            res.append(st[i].upper())
        else:
            res.append(st[i].lower())
    
    return ''.join(res)

print(myfunc('fLoccInauCinihiliPilificAtioN'))