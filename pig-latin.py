# take a sentence from user
while 1==1:
    input_string = input('this is a pig-latin conversation system, please type a sentence: ').strip()
# split the words
    words = input_string.split();

# loop each word and ad `ay`
    converted_word = []
    for item in words:
        item = item[::-1] +'ay'
        converted_word.append(item)
# join the words to make sentence

    output_string = ' '.join(converted_word);

# output to user

    print('here is your response',output_string)
