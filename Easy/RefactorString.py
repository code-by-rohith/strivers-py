def rever(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed = ""
    while stack:
        reversed += stack.pop()

    return reversed
n = "rohith"
reversed = rever(n)
print("Original string:", n)
print("Reversed string:", reversed)
