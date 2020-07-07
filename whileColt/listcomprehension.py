answer = ['answer'+ str(n) for n in range(1,10)]
print(answer)
#?------------------------------------------------------------------------------

answer1 = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(answer1)
print(answer2)
#?------------------------------------------------------------------------------

answer3 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
answer4 = [w[::-1].lower() for w in ['Elie','Tim','Matt']]
print(answer3)
print(answer4)
#?------------------------------------------------------------------------------

answer5 = [val for val in range(1,101) if val % 12 == 0]
print(answer5)
#?------------------------------------------------------------------------------

answer6 = [w for w in 'amazing' if w not in 'aeiou']
print(answer6)
#?------------------------------------------------------------------------------

#* NESTED LIST COMPREHENSION
answer7 = [['X' if num%2!=0 else 'O' for num in range(1,5)] for i in range(1,4)]
print(answer7)
#?------------------------------------------------------------------------------

answer8 = [[n for n in range(3)] for i in range(3)]
print(answer8)
#?------------------------------------------------------------------------------

answer9 = [[n for n in range(5)] for i in range(5)]
print(answer9)
