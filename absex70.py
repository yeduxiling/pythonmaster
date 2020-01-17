def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum


with open('result.txt', 'w') as reslut:
    with open('englishwordslist.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                reslut.write(word)
