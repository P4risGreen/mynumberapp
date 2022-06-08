import random

print(random.randint(1000,9999))
l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for c in range(16):
    print(l[random.randint(0, len(l))],end='')
print('')