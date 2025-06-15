def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")



import time

def countdown_with_sleep(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        time.sleep(1)
        n -= 1
    print("HAPPY NEW YEAR!")
