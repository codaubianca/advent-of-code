with open("./inputs/day05.txt", "r") as reader:
    lines = reader.readlines()
    
lines = [line.strip().split('->') for line in lines]
#lines = [[line.split('->')] for line in lines]
#print(lines)
lines = [[list(map(int,coord.strip().split(','))) for coord in coords] for coords in lines]
#print(lines)
N, M = 1000, 1000
diagram = [[0] * N for _ in range(M)]
#print(diagram)
for line in lines:
    x1 = line[0][0]
    #print(x1)
    y1 = line[0][1]
    #print(y1)
    x2 = line[1][0]
    #print(x2)
    y2 = line[1][1]
    #print(y2)
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1,y2+1):
            diagram[x1][y] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1,x2+1):
            diagram[x][y2] += 1
    else:
        adder_x, adder_y = 1, 1
        if x1 > x2 and y1 > y2:
            adder_x = adder_y = -1
        elif x1 > x2:
            adder_x = -1
        elif y1 > y2: 
            adder_y = -1
        
        for x in range(x1, x2, adder_x):
            diagram[x][y1] += 1
            y1 += adder_y
        diagram[x2][y2] += 1        

#print(diagram)

count = 0
for x in range(N):
    for y in range(M):
        if diagram[x][y] > 1:
            count += 1
    
print(count)
       