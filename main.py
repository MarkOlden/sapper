
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
    print("----------------------------------------------------")
    print("| To see correct answer type '?'                   |")
    print("| To show stats type 'stats'                       |")
    print("| To save stats type 'save' and filename           |")
    print("| To load stats type 'load' and filename           |")
    print("| To show stats from file type 'show' and filename |")
    print("----------------------------------------------------")
    
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

    while True:
        users_choice = input('Please, choose wire to cut: ')
        if len(users_choice.split()) == 2 and users_choice.split()[0] == 'save':
            try:
                fOut = open(users_choice.split()[1], 'w')
                s = " ".join([str(i) for i in [win, lose, winstreak]])
                fOut.write(s)
            except:
                print('File is not available')
            finally:
                fOut.close()
            continue
        elif len(users_choice.split()) == 2 and users_choice.split()[0] in ['load', 'show']:
            try:
                fIn = open(users_choice.split()[1], 'r')
                line = fIn.readline()
                if users_choice.split()[0] == 'load':
                    win, lose, winstreak = [int(i) for i in line.split()]
                    print('Stats loaded')
                else:
                    print(*[int(i) for i in line.split()])
            except:
                print('File is not available')
            finally:
                fIn.close()
            continue
        elif users_choice == '?':
            print('Correct wire is ', right_wire + 1)
            break
        elif users_choice == 'stats':
            print('Current winstreak: ', winstreak)
            try:
                print('Wins: ', win)
                print('Loses: ', lose)
                print('Win percent: ', win / (win + lose) * 100, '%')
            except:
                print('You have no stats yet, start playing or load stats.')
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
