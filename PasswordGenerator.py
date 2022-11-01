import random

lower = "qwertyuopasdfghjklizxcvbnm"
upper = lower.upper()
number = "0123456789"
mark = "!^+%&/()=*-"

#total = lower + upper + number + mark

print("""
WELCOME TO PASSWORD GENERATOR
  Password contains lower
  upper, number and mark
""")


lowerCount = int(input("lower character count: "))
upperCount = int(input("upper character count: "))
numberCount = int(input("number character count: "))
markCount = int(input("mark character count: "))

p1 = random.choices(lower,k=lowerCount)
p2 = random.choices(upper,k=upperCount)
p3 = random.choices(number,k=numberCount)
p4 = random.choices(mark,k=markCount)

tempPass = p1+p2+p3+p4

random.shuffle(tempPass)

password = "".join(tempPass)

print(password)
input()

