

with open("test.txt", "w") as f:
    print('whether the file is open:', f.closed)
    f.write("Hello World!")

print('whether the file is open:', f.closed)