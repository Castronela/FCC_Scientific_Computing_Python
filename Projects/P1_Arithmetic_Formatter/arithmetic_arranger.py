#!/bin/python3.11

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return ('Error: Too many problems.')
    lines = [[], [], [], []]
    for problem in problems:
        first_num, sign, second_num = problem.split()

        error_str = error_check(first_num, sign, second_num)
        if error_str != "":
            return error_str

        buffer = max(len(first_num), len(second_num))
        lines[0].append(' ' * 2 + (buffer - len(first_num)) * ' ' + first_num)
        lines[1].append(sign + ' ' + (buffer - len(second_num)) * ' ' + second_num)
        lines[2].append((buffer + 2) * '-')

        if sign == '+':
            result = str(int(first_num) + int(second_num))
        else:
            result = str(int(first_num) - int(second_num))
        lines[3].append((buffer + 2 - len(result)) * ' ' + result)
    lines_joined = [(" " * 4).join(line) for line in lines]
    output = "\n".join(lines_joined[:3])
    if show_answers:
        output += "\n" + lines_joined[3]
    return output

def error_check(first_num, sign, second_num):
    if not first_num.isdigit() or not second_num.isdigit():
        return ('Error: Numbers must only contain digits.')
    if len(first_num) > 4 or len(second_num) > 4:
        return ('Error: Numbers cannot be more than four digits.')
    if sign not in ["-", "+"]:
        return ("Error: Operator must be '+' or '-'.")
    return ""


print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

