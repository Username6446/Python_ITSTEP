import re
# # # Завдання 1

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur! Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

result = re.findall(r"[!\.\?]", line)
print(len(result))

# # # # # # Завдання 2

line = input("Enter line ::")

result = re.findall(r"\w", line)

reversed = list(result)
reversed.reverse()

print("Polindrom" if reversed==result else "Not Polindrom")

# # # # # Завдання 3

line = input("Enter line : ")

keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

words = re.findall(r"\w+", line)
for i in words:
    for j in keywords:
        if i==j:
            line = line.replace(i, i.upper())
print(line)



# # # # # Завдання 4

line = "word $ dsf gsdfg # word"
symb1 = input("Enter symbol1 :: ")
symb2 = input("Enter symbol2 :: ")

parts = re.split(re.escape(symb1) + r'.*?' + re.escape(symb2), line)

result = ''.join(parts)

print(result)

# # # # Завдання 5

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent semper feugiat odio, non hendrerit tellus bibendum quis. Nam id varius augue. Etiam suscipit facilisis libero, eu venenatis lorem pellentesque a. Donec lectus leo, congue non nulla et, hendrerit condimentum lectus. Nulla consectetur eros in dictum euismod. Morbi at nibh vel est ornare rutrum ac vel turpis. Sed nec blandit eros, quis auctor leo. Etiam pulvinar nisi nec neque efficitur, ut vulputate diam mattis. Nullam vitae volutpat risus. Praesent at nisi accumsan, placerat urna eget, aliquam orci. Curabitur posuere pellentesque nibh, sit amet faucibus nulla ornare et."
symbol = "stlp"

words = re.findall("[ ]*\w+[.,! ]*", text)
print(words)

for word in words:
    for s in symbol:
       if word.lower().find(s.lower()) !=1:
            text = text.replace(word, "")
print(text)


# # Завдання 6

line = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

result = re.findall("\w+", line)
print(result.reverse())

print(' '.join(result))