string = input()
k = int(input())

for i in range(0,len(string),k):
    temp = ''
    for character in string[i:i+k]:
        if character not in temp:
            temp += character

    print(temp)
