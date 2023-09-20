f = open('data.txt','r')


read_file = f.read().lower()
words_in_file = read_file.split()
count_word = {}
for i in words_in_file:
    if i in count_word:
        count_word[i] +=1
    else:
        count_word[i] = 1
    
print(count_word)