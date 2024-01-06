#Advent of Code 2023 Day 1
#Part 1: What is the first and last numerical digit in each line. Combine into a two digit number and add the results
#Part 2: Same as above, but also include digits written out in text, eg 'one'

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

print('Part 1: ' + str(total))

#Part 2: First and last digit but some are written out in text, eg one, two
def detect_numbers(input):
    for c in input:
        if ord(c) >= 48 and ord(c) <= 57:
            return int(c)
    return 0

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

total = 0
with open('2023/01/input.txt') as f:
    lines = f.readlines()
    for line in lines:

        if line[:18] == 'drkdbmv4zbjbznsqtj':
            pass

        string = ''
        xx = 0
        x = 0
        for c in line:
            string = string + c
            string = replace_numbers(string)
            xx =  detect_numbers(string)
            if xx > 0:
                break

        string = ''
        for c in line[::-1]:
            string = c + string
            string = replace_numbers(string)
            x =  detect_numbers(string)
            if x > 0:
                break               

        total = total + int(10 * xx + x)
        #print('input: ' + line + ' first: ' + str(xx) + ' last: ' + str(x) + ' result: ' + str(10 * xx + x))
        #print(int(xx + x))

print('Part 2: ' + str(total))