'''
python beginner math
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')
    
def km_miles():
    km = int(input('Enter distance in Kilometers:'))
    miles =  km / 1.609
    print('Distance in miles:{0}'.format(miles))

def miles_km():
    miles = int(input('Enter distance in Miles:'))
    km = miles * 1.609
    print('Distance in Kilometesrs:{0}'.format(km))

def F_toC():
   Fah =  int(input('Enter Celsius:'))
   Cel = (Fah - 32) * 5 / 9
   print('Celsius:{0}'.format(Fah))

def C_toF():
    Cel =  int(input('Enter Celsius:'))
    Fah = Cel * (9 / 5) + 32
    print('Fahrenheit:{0}'.format(Fah))




if __name__ == '__main__':
    while True:
        print_menu()
        choice = input('SELECT CONVERSION:')
        if choice == '1':
            km_miles()
        if choice == '2':
            miles_km()
        if choice == '3':
            F_toC()
        if choice == '4':
            C_toF()

        ans = input('Want u Break? y/n')
        if ans == 'y':
            break
