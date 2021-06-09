

def my_count_word(text):
    length = len(text)
    count = 0
    for x in range (length):
        # 빈칸일 경우 단어로 카운드!
        if text[x] == ' ':
            if x != 0:
                count = count + 1
        # 마지막 단어 카운드!
        elif x == length - 1:
            count = count + 1
    return count

input_txt = input("문장을 입력하세요")
print("단어의 수는?")
cnt = input(my_count_word(input_txt))