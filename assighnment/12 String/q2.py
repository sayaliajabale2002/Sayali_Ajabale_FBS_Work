s = 'Helloworldprogram'
n = int(input('enter nth index:'))

if(n<=len(s)):
    first_half = s[:n]
    second_half = s[n+1:]

    new_s = first_half + second_half
    print(new_s)
else:
    print(f'lenght of string is {len(s)}.\nout of range')
