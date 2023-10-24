def is_valid_expression(expression):
    valid_chars = set("TF(AOT)")
    stack = []

    for char in expression:
        if char not in valid_chars:
            return False

        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False  # 括號不平衡
            stack.pop()  # 移除匹配的開括號

    # 檢查括號是否平衡
    if stack:
        return False

    # 檢查操作數和運算符的正確組合
    for i in range(len(expression) - 1):
        char = expression[i]
        next_char = expression[i + 1]
        if char in "TF" and next_char in "TF":
            return False  # 兩個操作數相鄰
        if char in "AO" and next_char in "AO":
            return False  # 兩個運算符相鄰

    return True

def evaluate_expression(expression):
    if not is_valid_expression(expression):
        return "E"

    def evaluate_subexpression(expression):
        operators = []
        values = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char == "T":
                values.append(True)
            elif char == "F":
                values.append(False)
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators and operators[-1] != "(":
                    operator = operators.pop()
                    operand2 = values.pop()
                    operand1 = values.pop()
                    if operator == "A":
                        values.append(operand1 and operand2)
                    elif operator == "O":
                        values.append(operand1 or operand2)
                operators.pop()  # 移除開括號
            elif char in "AO":
                while operators and operators[-1] in "AO":
                    operator = operators.pop()
                    operand2 = values.pop()
                    operand1 = values.pop()
                    if operator == "A":
                        values.append(operand1 and operand2)
                    elif operator == "O":
                        values.append(operand1 or operand2)
                operators.append(char)
            i += 1
        while operators:
            operator = operators.pop()
            operand2 = values.pop()
            operand1 = values.pop()
            if operator == "A":
                values.append(operand1 and operand2)
            elif operator == "O":
                values.append(operand1 or operand2)
        return values[0]

    return "T" if evaluate_subexpression(expression) else "F"

# 使用者輸入
user_input = input("請輸入布林表達式：")
result = evaluate_expression(user_input)
print("結果:", result)
