def word_count(filename): 
""" Function that returns word count within a file.
"""

    text_file = open(filename)
    #opening file and assigns it to a variable

    word_count_dict = {}
    #creating an empty dictionary

    for line in text_file:
    #iterates through each line of the file
        line = line.rstrip()
        #removes the white space of the file, and rebinding to line variable
        line = line.lower()
        #makes all characters lowercase letters
        split_line = line.split(' ')
        #splitting each line into a list where each word is an item in a list

        for word in split_line:
            word = word.replace('"',"")
            word = word.replace('.',"")
            word = word.replace(';',"")
            word = word.replace('!',"")
            word = word.replace(':',"")
            word = word.replace('?',"")
            word = word.replace('--'," ")
            word = word.rstrip(",")            
            word = word.replace('_',"")
            word = word.replace(')',"")
            word = word.replace('(',"")

        for word in split_line:
        #iterates through each word in the list
            word_count_dict[word] = word_count_dict.get(word,0) + 1
            #if the word exists in word_count_dict increase value by 1, otherwise
            #add word as a key with a count of 1

    for word, count in word_count_dict.iteritems():
        #iterating over tuples that are in the word_count_dict which is now a 
        #list of tuples
        print word, count 
        #for each tuple, print the word and count


# word_count('test.txt')
word_count('twain.txt')