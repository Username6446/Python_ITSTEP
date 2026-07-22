import re
word = "Lorem ipsum"

print(word[2])

# word[2] = 'R'

# for char in word:
#     print(char, "---")
# print(chr(9835))

# for char in word:
#     print(ord(char))

# letter = "1"
# print(chr(ord(letter) + 32))

# numbers = "123456478"
# letters = "gfhfydj"
# line = "Lorem ipsum dolor sit amet"
# word = "Fruit Apple"
# word_2 = "BANANA"
# letterDig = "dhhhf66253JHHkdkd"

# # наявність лише букв або цифр
# print("================= str.isalnum() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.isalnum())
# print("\t", letters, "\t\t\t ----> ", letters.isalnum())
# print("\t", line, "\t ----> ", line.isalnum())
# print("\t", word, "\t\t\t ----> ", word.isalnum())
# print("\t", word_2, "\t\t\t ----> ", word_2.isalnum())
# print("\t", letterDig, "\t\t ----> ", letterDig.isalnum())


# # наявність лише букв
# print("================= str.isalpha() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.isalpha())
# print("\t", letters, "\t\t\t ----> ", letters.isalpha())
# print("\t", line, "\t ----> ", line.isalpha())
# print("\t", word, "\t\t\t ----> ", word.isalpha())
# print("\t", word_2, "\t\t\t ----> ", word_2.isalpha())
# print("\t", letterDig, "\t\t ----> ", letterDig.isalpha())

# # наявність лише цифр
# print("================= str.isdigit() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.isdigit())
# print("\t", letters, "\t\t\t ----> ", letters.isdigit())
# print("\t", line, "\t ----> ", line.isdigit())
# print("\t", word, "\t\t\t ----> ", word.isdigit())
# print("\t", word_2, "\t\t\t ----> ", word_2.isdigit())
# print("\t", letterDig, "\t\t ----> ", letterDig.isdigit())

# # наявність лише пробілів
# # letters = "           "
# print("================= str.isspace() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.isspace())
# print("\t", letters, "\t\t\t ----> ", letters.isspace())
# print("\t", line, "\t ----> ", line.isspace())
# print("\t", word, "\t\t\t ----> ", word.isspace())
# print("\t", word_2, "\t\t\t ----> ", word_2.isspace())
# print("\t", letterDig, "\t\t ----> ", letterDig.isspace())

# # наявність лише букви у нижньому регістрі
# print("================= str.islower() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.islower())
# print("\t", letters, "\t\t\t ----> ", letters.islower())
# print("\t", line, "\t ----> ", line.islower())
# print("\t", word, "\t\t\t ----> ", word.islower())
# print("\t", word_2, "\t\t\t ----> ", word_2.islower())
# print("\t", letterDig, "\t\t ----> ", letterDig.islower())

# # наявність лише букви у верхньому регістрі
# print("================= str.isupper() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.isupper())
# print("\t", letters, "\t\t\t ----> ", letters.isupper())
# print("\t", line, "\t ----> ", line.isupper())
# print("\t", word, "\t\t\t ----> ", word.isupper())
# print("\t", word_2, "\t\t\t ----> ", word_2.isupper())
# print("\t", letterDig, "\t\t ----> ", letterDig.isupper())

# # кожне слово з великої букви
# print("================= str.istitle() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.istitle())
# print("\t", letters, "\t\t\t ----> ", letters.istitle())
# print("\t", line, "\t ----> ", line.istitle())
# print("\t", word, "\t\t\t ----> ", word.istitle())
# print("\t", word_2, "\t\t\t ----> ", word_2.istitle())
# print("\t", letterDig, "\t\t ----> ", letterDig.istitle())

# # перетворює рядок у нижній регістр (всі маленьки букви)
# print("================= str.lower() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.lower())
# print("\t", letters, "\t\t\t ----> ", letters.lower())
# print("\t", line, "\t ----> ", line.lower())
# print("\t", word, "\t\t\t ----> ", word.lower())
# print("\t", word_2, "\t\t\t ----> ", word_2.lower())
# print("\t", letterDig, "\t\t ----> ", letterDig.lower())

# # перетворює рядок у верхній регістр (всі великі букви)
# print("================= str.upper() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.upper())
# print("\t", letters, "\t\t\t ----> ", letters.upper())
# print("\t", line, "\t ----> ", line.upper())
# print("\t", word, "\t\t\t ----> ", word.upper())
# print("\t", word_2, "\t\t\t ----> ", word_2.upper())
# print("\t", letterDig, "\t\t ----> ", letterDig.upper())

# # перетворює слово на початку речення з великої букви
# print("================= str.capitalize() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.capitalize())
# print("\t", letters, "\t\t\t ----> ", letters.capitalize())
# print("\t", line, "\t ----> ", line.capitalize())
# print("\t", word, "\t\t\t ----> ", word.capitalize())
# print("\t", word_2, "\t\t\t ----> ", word_2.capitalize())
# print("\t", letterDig, "\t\t ----> ", letterDig.capitalize())

# # кожне слово з великої букви
# print("================= str.title() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.title())
# print("\t", letters, "\t\t\t ----> ", letters.title())
# print("\t", line, "\t ----> ", line.title())
# print("\t", word, "\t\t\t ----> ", word.title())
# print("\t", word_2, "\t\t\t ----> ", word_2.title())
# print("\t", letterDig, "\t\t ----> ", letterDig.title())

# # кожне слово з великої букви
# print("================= str.swapcase() ===================")
# print("\t", numbers, "\t\t\t ----> ", numbers.swapcase())
# print("\t", letters, "\t\t\t ----> ", letters.swapcase())
# print("\t", line, "\t ----> ", line.swapcase())
# print("\t", word, "\t\t\t ----> ", word.swapcase())
# print("\t", word_2, "\t\t\t ----> ", word_2.swapcase())
# print("\t", letterDig, "\t\t ----> ", letterDig.swapcase())

# line = "Lorem ipsum dolor sit  ipsum amet Lorem ipsum dolor sit amet ipsum"
# print("================= str.find() ===================")
# print("", line, " ----> ", line.find("ipsum"))
# print("", line, " ----> ", line.find("ipsum",7))
# print("", line, " ----> ", line.find("ipsum",24))
# print("", line, " ----> ", line.find("ipsum",41))

# index = line.find("ipsum")
# while index != -1:
#     print(line, index)
#     index = line.find("ipsum", index + 1)

# print("================= str.rfind() ===================")
# print("", line, " ----> ", line.rfind("ipsum"))
# print("", line, " ----> ", line.rfind("ipsum",0, 61))
# print("", line, " ----> ", line.rfind("ipsum",0, 40))
# print("", line, " ----> ", line.rfind("ipsum",0, 23))
# print("", line, " ----> ", line.rfind("ipsum",0, 6))

# print("================= str.index() ===================")
# print("", line, " ----> ", line.index("ipsum"))
# print("", line, " ----> ", line.index("ipsum",7))
# print("", line, " ----> ", line.index("ipsum",24))
# print("", line, " ----> ", line.index("ipsum",41))
# # print("", line, " ----> ", line.index("ipsum",62))

# print("================= str.rindex() ===================")
# print("", line, " ----> ", line.rindex("ipsum"))

# print("================= str.count() ===================")
# print("", line, " ----> ", line.count("ipsum"))

# print("================= str.replace() ===================")
# print("", line, " ----> ", line.replace("ipsum","yellow"))

# line = "Lorem ipsum dolor sit  ipsum amet Lorem ipsum dolor sit amet ipsum"

# str_1 = "1234"
# str_2 = "132ags1214"
# str_3 = "Lorem** ipsum 21 dolor sit"

# print("================= re.search('template', str) ===================")
# print(str_1, "\t\t\t\t --> ", re.search('^[0-9]{4}$', str_1))
# print(str_2, "\t\t\t --> ", re.search('^[0-9]{4}$', str_2))
# print(str_3, "\t --> ", re.search('^[0-9]{4}$', str_3))

# match = re.search('[a-zA-Z]+',str_3)
# match = re.search('[a-z]+',str_3,flags=re.IGNORECASE)
# # print(match[0])
# match = re.search('[a-z]+\*+',str_3,flags=re.IGNORECASE)
# print(match)

# match = re.search('\w+',str_3,flags=re.IGNORECASE)
# print(match)
# match_all = re.findall('\w+',str_3,flags=re.IGNORECASE)
# print(match_all)

# email = "dasha_konopelko@gmail.com"
# match = re.search('^\w+@\w{3,5}.\w{3,}$',email,flags=re.IGNORECASE)
# print(match)

# match = re.search('[^12a-z]',str_3,flags=re.IGNORECASE)
# print(match)

# line = "Lorem ipsum dolor sit  ipsum amet Lorem ipsum dolor sit amet ipsum"
# print(line)
# print(re.sub('\w{5}','red',line))

print('Lorem'.center(50))
print('Lorem'.center(50,'*'))
print('Lorem\trr'.expandtabs(10))
print('Lorem'.rjust(50,'*'))
print('Lorem'.ljust(50,'*'))
print('Lorem'.lstrip('Lo'))
print('Lorem'.rstrip('em'))
print('mLorem'.strip('m'))

import string
import random
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print("Password :: ","".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 10)))