

def getMAXNumericValue(string):
    max_begin = 0
    max_end = 0
    cur_begin = 0
    cur_end = 0
    i = 0
    while i < len(string):
        if (not isNumber(string[i])):
            cur_end = i
            if isLess(string[max_begin : max_end], string[cur_begin : cur_end]):
                max_begin, max_end = cur_begin, cur_end
            while (i < len(string) and not isNumber(string[i])):
                i += 1
        else:
            cur_begin = i
            while (i < len(string) and isNumber(string[i])):
                i += 1
    if max_begin == max_end:
        return "0"
    return string[max_begin : max_end]
         
def isLess(string1, string2):
    if len(string1) < len(string2):
        return True
    return len(string1) == len(string2) and string1 < string2

def isNumber(string):
    return string >= "0" and string <= "9"

s = "lkJ89kjHF100SLK530jh240"
print s
print getMAXNumericValue(s)
