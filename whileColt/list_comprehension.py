answer = ['answer'+ str(n) for n in range(1,10)]
#?------------------------------------------------------------------------------

answer1 = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
#?------------------------------------------------------------------------------

answer3 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
answer4 = [w[::-1].lower() for w in ['Elie','Tim','Matt']]
#?------------------------------------------------------------------------------

answer5 = [val for val in range(1,101) if val % 12 == 0]
#?------------------------------------------------------------------------------

answer6 = [w for w in 'amazing' if w not in 'aeiou']
#?------------------------------------------------------------------------------

#* NESTED LIST COMPREHENSION
answer7 = [['X' if num%2!=0 else 'O' for num in range(1,5)] for i in range(1,4)]
#?------------------------------------------------------------------------------

answer8 = [[n for n in range(3)] for i in range(3)]
#?------------------------------------------------------------------------------

answer9 = [[n for n in range(5)] for i in range(5)]
#?------------------------------------------------------------------------------

print(str(answer) +'\n'+ str(answer1) +'\n'+ str(answer2) +'\n'+ str(answer3) +'\n'+ str(answer4) +'\n'+ str(answer5) +'\n'+ str(answer6) +'\n'+ str(answer7) +'\n'+ str(answer8) +'\n'+ str(answer9))
