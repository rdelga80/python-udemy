# jabber = open('C:\\Users\\Ric\\code\\python-udemy\\sample.txt', 'r')
# EXAMPLE 1
# jabber = open('sample.txt', 'r')

# for line in jabber:
#   if "jabberwock" in line.lower():
#     print(line, end='')

# jabber.close()

# EXAMPLE 2

# with open('sample.txt', 'r') as jabber:
#   for line in jabber:
#     if "JAB" in line.upper():
#       print(line, end='')

# EXAMPLE 3
# to remove extra line

# with open('sample.txt', 'r') as jabber:
#   line = jabber.readline()
#   while line:
#     print(line, end='')
#     line = jabber.readline()

# EXAMPLE 4

# with open('sample.txt', 'r') as jabber:
#   lines = jabber.readlines()
# print(lines)

# for line in lines:
#   print(line, end='')

# EXAMPLE 5

# with open('sample.txt', 'r') as jabber:
#   lines = jabber.readlines()
# print(lines)

# for line in lines[::-1]:
#   print(line, end='')

# EXAMPLE 6

with open('sample.txt', 'r') as jabber:
  lines = jabber.read()
print(lines)

for line in lines[::-1]:
  print(line, end='')