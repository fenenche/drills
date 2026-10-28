def balanced_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
word = "(hello)"
words = "{[()]}"
texts = "([)]"
bracket = "((hello)"
print(balanced_brackets(word))
print(balanced_brackets(words))
print(balanced_brackets(texts))
print(balanced_brackets(bracket))
