for i in range (100, 1000):
    unit = i % 10
    ten_digit = (i // 10) % 10
    hundred_digit = i // 100
    if (unit ** 3) + (ten_digit ** 3) + (hundred_digit **3) == i:
        print(i)
