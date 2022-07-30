vowel_list = ['a', 'e', 'i', 'o', 'u']
final_word = ''
word_input = input('Input: ')
for i in range(len(word_input)):
    if word_input[i].lower() not in vowel_list:
        final_word += word_input[i]
print('Output:',final_word)