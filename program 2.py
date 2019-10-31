import random 
x = random.randrange(1,11)
y = True
i = 1
while y:
    print('-----------------------------------------')
    anss = input('podaj liczbe ')
    if anss == 'exit' or anss == 'Exit':
       y = False
       print('zakonczyłes gre')
    else:
        ans = int(anss) 
        if ans == x:
            print('zgadłes w %d próbie, gratulacje' %i)
            y = False
        if ans > x:
            print('liczba której szukasz jest mniejsza niż podana orzez ciebie')
        if ans < x:
            print('liczba której szukasz jest wieksza niz ta podana przez ciebie')
        
    i += 1
input("")