h = 1100 // 1000
print(h)


import random


def guess_number(n_numbers):
        random_n = random.randint(1, n_numbers)
        array = [n for n in range(1,n_numbers+1)]
        to_guess = array[random_n]
        print(to_guess)
        c = 0
        c2 = n_numbers
        while True:
                inputt = input("ingrese number para ver si adivinó: ")
                if array[int(inputt)] < to_guess:  # 4   7
                        c2 = to_guess
                        print(-1)
                elif array[int(inputt)] > to_guess:
                        c = to_guess
                        print(1)
                else:
                        return "0"
                        
        return array



n1_numbers = 10
t = guess_number(n1_numbers)
print(t)
