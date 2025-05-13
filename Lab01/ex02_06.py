input_str = input("nhập X, Y: ")
dimensinons = [int(x) for x in input_str.split(',')]
rowNum = dimensinons[0]
colNum = dimensinons[1]
multilist = [[0 for col in range(colNum)]for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)