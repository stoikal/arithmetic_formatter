def arithmetic_formatter(problems, show_result=False) :
    if len(problems) > 5 :
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    spaces = "    "

    for index, problem in enumerate(problems) :
        [str1, operator, str2] = problem.split()

        if not operator in ["-", "+"] :
            return "Error: Operator must be '+' or '-'."

        if len(str1) > 4 or len(str2) > 4 :
            return "Error: Numbers cannot be more than four digits."

        try :
            operand1 = int(str1)
            operand2 = int(str2)
        except :
            return "Error: Numbers must only contain digits."
        
        if operand1 >= operand2 :
            length = len(str1) + 2
        else :
            length = len(str2) + 2

        for i in range(0, length - len(str1)) :
            line1 += " "

        line1 += str1

        line2 += operator
        for i in range(0, length - 1 - len(str2)) :
            line2 += " "

        line2 += str2

        for i in range(0, length) :
            line3 += "-"
    
        if operator == "+" :
            result = str(operand1 + operand2)
        else :
            result = str(operand1 - operand2)

        for i in range(0, length - len(result)) :
            line4 += " "

        line4 += result

        if index < len(problems) - 1 :
            line1 += spaces
            line2 += spaces
            line3 += spaces
            line4 += spaces

    final_result = line1 + "\n" + line2 + "\n" + line3

    if show_result :
        final_result += "\n" + line4

    return final_result