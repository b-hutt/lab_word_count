# put your code here.
import sys

def get_word_count(file_name):
    """Will return word count of a given text file.
        
        user will enter python3 wordcount.py 'anytextfilehere' on the command
        line to run the code

    """

    text_file = open(sys.argv[1])
    
    word_count = {}
    special_characters = [',', '?', '.', '/', ':', '(',')', '!']

    for line in text_file:
        line = line.strip()
        words = line.split(' ')

        for word in words:
            # for letter in word:
            #     if letter in special_characters:
            #         new_word = [word]
            #         new_word = word.remove([-1])
                    
            #         word = new_word
            word_count[word] = word_count.get(word,0) + 1

    return word_count

print(get_word_count(sys.argv))