print('----------------')
print('zadanie 1')
num_str = input("podaj pierwsza liczbe ")
num = int(num_str) 
if num % 2 == 0 :
    if num % 4 == 0:
        print('ta liczba jest wielokrotnocią 4')
    else:
        print('liczba jest parzysta')
else:
    print('liczba jest nieparzysta')

print('----------------')
print('zadanie 2')
num_1 = input('podaj tu pierwsza liczbe ')
num_2 = input('podaj tu drugą liczbe ')
num1 = int(num_1)
num2 = int(num_2)
if num1 % num2 == 0:
    print('liczba pierwsza dzieli sie bez reszty przez drugą liczbe')
else:
    print('liczba pierwsza NIE dzieli sie przez drugą liczbe bez reszty')


print('---------------')
input('nacisnij dolwony przycisk by zakończyć')
