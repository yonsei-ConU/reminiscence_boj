data = open('data.txt', 'w')

data.write(f"100000 0\n")
for i in range(1, 100000):
    data.write(f"{i} {i + 1}\n")
