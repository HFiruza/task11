# name = input('ВВедите ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# else:
#     print("Привет", name)

# number = int(input("Введите число: "))  # Fizz, Buzz, FizzBuzz
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print("Число не подходит")
# or - не строгий оператор, and - строгий оператор (это если нужно проверить 2 условия в одном)

first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second and first != third and second != third: #if not x == y and not y == z: print("")
    print(0)
#else:
    #print(0)






