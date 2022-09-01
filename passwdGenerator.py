import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digests = "0123456789"
symbols = "()[]{},;:.-/\\?+*#$+ "

upper,lower,nums,syms = True, True, True, False

all = ""

if upper:
    all+= uppercase_letters
if lower:
    all+= lowercase_letters
if nums:
    all+= digests
if syms:
    all+= symbols
# password length
length = 20
# how many password 
amount = 10

for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)