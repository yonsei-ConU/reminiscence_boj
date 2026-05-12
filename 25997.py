import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def get_direction(c):
    if c == 'N':
        return 0
    elif c == 'E':
        return 90
    elif c == 'S':
        return 180
    else:
        return 270


X, Y = input_().rstrip().split()
X = X
Y = Y
if len(X) == 1:
    angleX = get_direction(X)
elif X == "NE":
    angleX = 45
elif X == "SE":
    angleX = 135
elif X == "SW":
    angleX = 225
elif X == "NW":
    angleX = 315
else:
    X = X[::-1]
    if X[:2][::-1] == "NE":
        angleX = 45
    elif X[:2][::-1] == "SE":
        angleX = 135
    elif X[:2][::-1] == "SW":
        angleX = 225
    else:
        angleX = 315
    cur = 22.5
    for i in range(2, len(X)):
        if 0 < angleX < 90 and X[i] == "N" or 90 < angleX < 180 and X[i] == "E" or 180 < angleX < 270 and X[i] == "S" or 270 < angleX < 360 and X[i] == "W":
            angleX -= cur
        else:
            angleX += cur
        cur /= 2

if len(Y) == 1:
    angleY = get_direction(Y)
elif Y == "NE":
    angleY = 45
elif Y == "SE":
    angleY = 135
elif Y == "SW":
    angleY = 225
elif Y == "NW":
    angleY = 315
else:
    Y = Y[::-1]
    if Y[:2][::-1] == "NE":
        angleY = 45
    elif Y[:2][::-1] == "SE":
        angleY = 135
    elif Y[:2][::-1] == "SW":
        angleY = 225
    else:
        angleY = 315
    cur = 22.5
    for i in range(2, len(Y)):
        if 0 < angleY < 90 and Y[i] == "N" or 90 < angleY < 180 and Y[i] == "E" or 180 < angleY < 270 and Y[i] == "S" or 270 < angleY < 360 and Y[i] == "W":
            angleY -= cur
        else:
            angleY += cur
        cur /= 2

print(min(abs(angleX - angleY), angleX + 360 - angleY, angleY + 360 - angleX))
