from copy import copy
outerTable = dict()
string = "abcabc"

for c in string:
    outerTable[c] = outerTable.get(c, 0) + 1

for i in range(5):
    innerTable = copy(outerTable)
    innerTable['a'] -= 1

print outerTable
