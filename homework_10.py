#Homework 10
#1. Find an article about python. Save it to a file called Python.txt
#If you cannot find one, use this
#https://en.wikipedia.org/wiki/History_of_Python
#Copy everything under Version 3 to a file called Python.txt

#2. Use filehandle to read this file Python.txt


fileh = open("python.txt", "r")
word_list = []
with open("python.txt") as fh:
    lines = fh.readlines()
    print("Lines: {}".format(lines))
    #3. Split it into a list of words separated by spaces. Do not include punctuation
    for i in lines:
        words = i.split()
        print("words: {}".format(words))
        for i in words:
            if '"' in i:
                new_i = i.strip('"')
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif "," in i:
                new_i = i.strip(",")
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif "." in i:
                new_i = i.strip(".")
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif "-" in i:
                new_i = i.strip("-")
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif '".' in i:
                new_i = i.strip('".')
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif "(" in i:
                new_i = i.strip("(")
                print("{}\n".format(new_i))
                word_list.append(new_i)
            elif ")" in i:
                new_i = i.strip(")")
                print("{}\n".format(new_i))
                word_list.append(new_i)
            else:
                print("{}\n".format(i))
                word_list.append(i)
            print("Word List: {}".format(word_list))

#4. Use filter to filter out words with exactly 5 letters
            result = filter(lambda x: len(x) == 5, word_list)
            print("Five Letter Words: {}".format(result))

#5. Now use map to map the list of words with exactly 5 letters into the upper case version
            mapped_result = map(lambda x: x.upper(), result)
            print("Upper Case List: {}".format(mapped_result))


#6. Use filter to filter out words that are more than 5 letters long and save to a list called
#plus5_letters
            plus5_letters = filter(lambda x: len(x) > 5, word_list)
            print("Letters Longer Than 5 Letters: {}".format(plus5_letters))


#7. Create a dictionary called word_count. Word_count keeps track of the number of times
#each word appears in the list plus5_letters
            word_dict = {}
            for i in range(0, len(plus5_letters)):
                if plus5_letters[i] not in word_dict.keys():
                    word_dict[plus5_letters[i]] = 1
                else:
                    word_dict[plus5_letters[i]] += 1

            print("Word Dictionary: {}".format(word_dict))
                    

#8. Use reduce to count the total number of letters in the list plus5_letters
            letter_count = reduce(lambda x, y: x + y, plus5_letters)
            print("Letter Count: {}".format(letter_count))
            letter_count_length = len(letter_count)
            print("Letter Count Length: {}".format(letter_count_length))