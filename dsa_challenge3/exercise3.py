def valid_parentheses(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{" }

    for char in text:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
symbol = "{[()]}"
symbols = "([)]"
sym = "((()))"
syms = "{[}"
print(valid_parentheses(symbol))
print(valid_parentheses(symbols))
print(valid_parentheses(sym))
print(valid_parentheses(syms))