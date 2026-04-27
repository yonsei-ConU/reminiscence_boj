e = str(input())
a = 0
b = 0
for c in range(len(e)):
    if e[c] == '(':
               a += 1
    elif e[c] == ')':
               b += 1
    if a < b:
            print('ROCK1')
            break
else:
    if a != b:
        print('ROCK2')
    else:
        if '(+' in e or '(-' in e or '(*' in e or '(/' in e or '()' in e or ')(' in e or '++' in e or '+-' in e or '+*' in e or '+/' in e or '+)' in e or '-+' in e or '--' in e or '-*' in e or '-/' in e or '-)' in e or '*+' in e or '*-' in e or '**' in e or '*/' in e or '*)' in e or '/+' in e or '/-' in e or '/*' in e or '//' in e or '/)' in e or '0(' in e or '1(' in e or '2(' in e or '3(' in e or '4(' in e or '5(' in e or '6(' in e or '7(' in e or '8(' in e or '9(' in e or ')0' in e or ')1' in e or ')2' in e or ')3' in e or ')4' in e or ')5' in e or ')6' in e or ')7' in e or ')8' in e or ')9' in e:
            print('ROCK3')
        elif e[0] in ['+', '-', '*', '/']:
            print('ROCK4')
        else:
            try:
                print(eval(e.replace('/', '//')))
            except:
                print('ROCK5')
