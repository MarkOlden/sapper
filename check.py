
def wires3(wires, serial_number):
    if 'black' in wires:
        if wires.count('yellow') >= 2:
            right_wire = len(wires) - 1 - wires[::-1].index('yellow')
        elif wires[2] == 'blue' or wires[2] == 'white':
            right_wire = 2
        else:
            right_wire = 1
    else:
        right_wire = 0
    return right_wire


def wires4(wires, serial_number):
    if wires.count('red') > 1 and (int(serial_number[5]) % 2 == 1):
        right_wire = len(wires) - 1 - wires[::-1].index('red')
    elif wires[3] == 'yellow' and not ('red' in wires):
        right_wire = 0
    elif wires.count('blue') == 1:
        right_wire = 0
    elif wires.count('yellow') > 1:
        right_wire = 3
    else:
        right_wire = 1
    return right_wire


def wires5(wires, serial_number):
    if wires[4] == 'black' and (int(serial_number[5]) % 2 == 1):
        right_wire = 3
    elif wires.count('red') == 1 and wires.count('yellow') > 1:
        right_wire = 0
    elif not ('black' in wires):
        right_wire = 1
    else:
        right_wire = 0
    return right_wire


def wires6(wires, serial_number):
    if not ('yellow' in wires) and (int(serial_number[5]) % 2 == 1):
        right_wire = 2
    elif wires.count('yellow') == 1 and wires.count('white') > 1:
        right_wire = 4
    elif not ('red' in wires):
        right_wire = 5
    else:
        right_wire = 3
    return right_wire
