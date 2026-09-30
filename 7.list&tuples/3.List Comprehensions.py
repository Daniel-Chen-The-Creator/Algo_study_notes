squares_1 = []
for x in range(10):
    squares_1.append(x**2)

print(squares_1)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares_2 = [x**2 for x in range(10)]
#square_1 == square_2