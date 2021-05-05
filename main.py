
import random
import string
import os
from serial import generate_number
import check


winstreak = 0
win = 0
lose = 0
colors = {  1: 'red',
            2: 'blue',
            3: 'white',
            4: 'yellow',
            5: 'black'  }



while True:

    serial_number = generate_number()
    wires = random.randint(3, 6)
    current_combination = []

    for i in range(wires):
        color = colors[random.randint(1, 5)]
        current_combination.append(color)
    print("Serial number: ", serial_number)
    print(*current_combination, sep=' ')
    
    if wires == 3:
        right_wire = check.wires3(current_combination, serial_number)
    elif wires == 4:
        right_wire = check.wires4(current_combination, serial_number)
    elif wires == 5:
        right_wire = check.wires5(current_combination, serial_number)
    else:
        right_wire = check.wires6(current_combination, serial_number)
    print('Please, choose wire to cut: ', end='')    
    
    while True:
        users_choice = input()
        if users_choice == '?':
            print('Correct wire is ', right_wire + 1)
            break
        elif users_choice == 'stats':
            print('Current winstreak: ', winstreak)
            print('Win percent: ', win / (win + lose) * 100, '%')
            break
        else:
            try:
                if int(users_choice) <= 0 or int(users_choice) > wires:
                    raise ValueError
                if int(users_choice) - 1 == right_wire:
                    print('WIN')
                    winstreak += 1
                    win += 1
                    break
                else:
                    print('LOSE')
                    print(right_wire + 1, ' was correct')
                    lose += 1
                    break
            except:
                print('The answer is not correct. Try again. ', end='')
    
    os.system("pause")
    os.system('cls')



