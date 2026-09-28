vowel = 'aeiou'
count = 0
s = input('enter string: ')
new_s = s.lower()

for i in new_s:
    if(i in vowel):
        count += 1

print(f'total count of vowels in {s} is {count}')