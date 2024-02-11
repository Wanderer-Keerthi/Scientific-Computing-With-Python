def arithmetic_arranger(problems, display_solutions=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_line = ""
    bottom_line = ""
    dash_line = ""
    result_line = ""
    
    for problem in problems:
        operand1, operator, operand2 = problem.split()
    
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
    
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
    
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
    
        width = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(width) + '    '
        bottom_line += operator + operand2.rjust(width - 1) + '    '
        dash_line += '-' * width + '    '
    
        if display_solutions:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
    
            result_line += result.rjust(width) + '    '
    
    arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()
    
    if display_solutions:
        arranged_problems += '\n' + result_line.rstrip()
    
    return arranged_problems
