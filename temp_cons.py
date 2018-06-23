import json

n = 28
m = 28

data = [["blank" for i in range(m)] for j in range(n)]
data[1][1] = "wall-corner-ul"
data[1][m-1] = "wall-corner-ur"

for i in range(2 , m-1):
    data[1][i] = "wall-straight-horiz"
data[1][m//2] = "wall-t-top"

for i in range(2 , 10):
    data[i][1] = "wall-straight-vert"
data[10][1] = "wall-corner-ll"

for i in range(2 , 6):
    data[10][i] = "wall-straight-horiz"
data[10][6] = "wall-corner-ur"
data[11][6] = "wall-straight-vert"
data[12][6] = "wall-corner-lr"
for i in range(1 , 6):
    data[12][i] = "wall-straight-horiz"

for i in range(1 , 6):
    data[14][i] = "wall-straight-horiz"
data[14][6] = "wall-corner-ur"
data[15][6] = "wall-straight-vert"
data[16][6] = "wall-corner-lr"

for i in range(2 , 6):
    data[16][i] = "wall-straight-horiz"
data[16][1] = "wall-corner-ul"

for i in range(17 , n-1):
    data[i][1] = "wall-straight-vert"
data[n-1][1] = "wall-corner-ll"





data[n-1][m-1] = "wall-corner-lr"

for i in range(2 , m-1):
    data[n-1][i] = "wall-straight-horiz"
data[n-1][m//2] = "wall-straight-horiz"

for i in range(2 , 10):
    data[i][m-1] = "wall-straight-vert"

data[10][m-1] = "wall-corner-lr"

for i in range(m-5 , m-1):
    data[10][i] = "wall-straight-horiz"
data[10][m-6] = "wall-corner-ul"
data[11][m-6] = "wall-straight-vert"
data[12][m-6] = "wall-corner-ll"
for i in range(1 , 6):
    data[12][m-i] = "wall-straight-horiz"

for i in range(1 , 6):
    data[14][m-i] = "wall-straight-horiz"
data[14][m-6] = "wall-corner-ul"
data[15][m-6] = "wall-straight-vert"
data[16][m-6] = "wall-corner-ll"

for i in range(2 , 6):
    data[16][m-i] = "wall-straight-horiz"
data[16][m-1] = "wall-corner-ur"

for i in range(17 , n-1):
    data[i][m-1] = "wall-straight-vert"


data[13][17] = "wall-straight-vert"
data[13][11] = "wall-straight-vert"
data[11][17] = "wall-end-t"
data[11][11] = "wall-end-t"
data[15][11] = "wall-corner-ll"
data[14][11] = "wall-straight-vert"
data[12][11] = "wall-straight-vert"
data[15][17] = "wall-corner-lr"
data[14][17] = "wall-straight-vert"
data[12][17] = "wall-straight-vert"

for i in range(12 , 17):
    data[11][i] = "ghost-door"
    data[15][i] = "wall-straight-horiz"

data[17][11] = "wall-end-l"
data[17][17] = "wall-end-r"
for i in range(12 , 17):
    data[17][i] = "wall-straight-horiz"
data[17][14] = "wall-t-top"
data[18][14] = "wall-straight-vert"
data[19][14] = "wall-straight-vert"
data[20][14] = "wall-end-b"

data[22][11] = "wall-end-l"
data[22][17] = "wall-end-r"
for i in range(12 , 17):
    data[22][i] = "wall-straight-horiz"
data[22][14] = "wall-t-top"
data[23][14] = "wall-straight-vert"
data[24][14] = "wall-straight-vert"
data[25][14] = "wall-end-b"


data[6][11] = "wall-end-l"
data[6][17] = "wall-end-r"
for i in range(12 , 17):
    data[6][i] = "wall-straight-horiz"
data[6][14] = "wall-t-top"
data[7][14] = "wall-straight-vert"
data[8][14] = "wall-straight-vert"
data[9][14] = "wall-end-b"

data[4][14] = "wall-end-b"
data[3][14] = "wall-straight-vert"
data[2][14] = "wall-straight-vert"

with open(".\\res\\levels\\1.json" , "w") as output_file:
    json.dump(data , output_file)