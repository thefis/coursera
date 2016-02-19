import re

def count():

    filedir = r'C:\Users\ethefis\Downloads\regex_sum_247380.txt'

    fhandle = file(filedir, 'r')
    lines = fhandle.readlines()
    #print lines[29]

    total = 0

    for aline in lines:
        result = re.findall(r'[0-9]+', aline)
        result = [int(i) for i in result]
        print result
        line_total = sum(result)
        print line_total
        total = total + line_total

    print total
count()

