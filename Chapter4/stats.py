import random

num = random.randrange(10, 100)

numList = list(range(num))

mxNum = max(numList)
mnNum = min(numList)
smNum = sum(numList)
lnNum = len(numList)
avgNum = smNum/lnNum

print(f'The list of numbers: \n {numList}')
print(f'The largest number: {mxNum}')
print(f'The smallest number: {mnNum}')
print(f'The total of all numbers: {smNum}')
print(f'The average number{avgNum}')