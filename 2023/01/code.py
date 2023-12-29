#Part 1: First and last numerical digit

total = 0
with open('2023/01/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        for c in line:
            if ord(c) >= 48 and ord(c) <= 57:
                xx = c
                break
        for c in reversed(line):
            if ord(c) >= 48 and ord(c) <= 57:
                x = c
                break
        total = total + int(xx + x)
        #print('input: ' + line + ' first: ' + xx + ' last: ' + x + ' result: ' + xx + x)
        #print(int(xx + x))

print('Part 1:' + str(total))

#Part 2: First and last digit but some are written out in text, eg one, two
def replace_numbers(input):
    input = input.replace('one', '1')
    input = input.replace('two', '2')
    input = input.replace('three', '3')
    input = input.replace('four', '4')
    input = input.replace('five', '5')
    input = input.replace('six', '6')
    input = input.replace('seven', '7')
    input = input.replace('eight', '8')
    input = input.replace('nine', '9')
    return input

def replace_numbers_rev(input):
    input = input.replace('eno', '1')
    input = input.replace('owt', '2')
    input = input.replace('eerht', '3')
    input = input.replace('ruof', '4')
    input = input.replace('evif', '5')
    input = input.replace('xis', '6')
    input = input.replace('neves', '7')
    input = input.replace('thgie', '8')
    input = input.replace('enin', '9')
    return input

total = 0
with open('2023/01/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        orig = line
        for c in replace_numbers(line):
            if ord(c) >= 48 and ord(c) <= 57:
                xx = c
                break
        rev = line[::-1]
        for c in replace_numbers_rev(rev):
            if ord(c) >= 48 and ord(c) <= 57:
                x = c
                break
        total = total + int(xx + x)
        print('input: ' + orig + ' first: ' + xx + ' last: ' + x + ' result: ' + xx + x)
        #print(int(xx + x))

print('Part 2: ' + str(total))