f = open(r'C:\Users\RanWeizheng\Desktop\pyTest\scores.txt','r', encoding='UTF-8')
lines = f.readlines()
f.close()

writeLines = []
def getSum(data):
    sum = 0
    for str in data[1:]:
        if int(str) < 60:
            continue
        sum += int(str)
    return sum

for line in lines:
    data = line.split()
    sum = getSum(data)
    result = '%s\t:%d\n'%(data[0], sum)
    writeLines.append(result)

out = open(r'C:\Users\RanWeizheng\Desktop\pyTest\score-result.txt', 'w')
out.writelines(writeLines)
out.close()