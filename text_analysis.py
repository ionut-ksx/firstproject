# text_analysis.py
"""
Requirements
Given a piece of text( article), extract the following:
How many words are there in total
How many unique words are there
What are the top 5 words that appear in the text ? What are their number of appearances?
Print all phone numbers
input file: input.txt
file is openable
split by space
remove all the punctuation
don’t count words with less than 3 characters
what is a phone number
1:42
mobile ro number
"""

def extract_data(file_name):
    def remove_punctuations(file_line):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        alnum_line = []
        for char in file_line:
            if char in punctuations:
                alnum_line.append(" ")
            else:
                alnum_line.append(char)

        return ''.join(alnum_line)

    file_content = {}
    # open the file for reading data
    with open(file_name, 'r') as file_data:
        """ Convert characters to lowercase (avoid mismatch) and remove spaces from begin and the end of the line """
        for line in file_data:
            line = line.lower().strip()

            _line = remove_punctuations(line)
            # crate a list of words split by spaces
            _line = _line.split(" ")
            # build phones list
            """Go over each word in line, add them as keys if not in the dictionary, if present, count its occurrences"""
            for word in _line:
                if len(word) > 2:
                    if word in file_content:
                        file_content[word] += 1
                    else:
                        file_content[word] = 1

    return file_content

def get_phone_numer(file_name):
    with open(file_name, 'r') as article:
        phones_list = []
        for line in article:
            line = line.strip().split(' ')
            phone = line.pop()
            if phone.isdigit() and len(phone) == 10:
                phones_list.append(phone)

    return phones_list


def get_unique_words(my_dict):
    my_list = extract_data(my_dict)
    count_unique_words = 0
    for word in my_list:
        if my_list[word] == 1:
            count_unique_words += 1
    return count_unique_words


def get_total_words(my_dict):
    result = 0
    dict_values = list(my_dict.values())
    for i in dict_values:
        result += i
    return result


def get_top_five_words(my_dict):
    sorted_list = sorted(my_dict.items(), key=lambda val: val[1], reverse=True)
    count = 0
    for i in sorted_list:
        if count < 5:
            print(i[0], ":", i[1])
            count += 1
    return

def check_article_content():
    file_name = "article.txt"
    word_occur = extract_data(file_name)
    # get the list of keys and print how many times they appear in the article
    print("Word", "\t","|", "Occurrence number")
    for key_word in list(word_occur.keys()):
        print(f"{key_word: ^15} {word_occur[key_word]: ^5}")

    # How many words are there in total?
    total = get_total_words(word_occur)
    print("-"*20,"\nTotal words",total)

    # How many unique words are there?
    unique_words = get_unique_words(file_name)
    print("-"*20,"\nTotal unique words", unique_words)

    # What are the top 5 words that appear in the text ? What are their number of appearances?
    print("-"*20,"\n")
    print("Top 5 words\n","-"*20)
    get_top_five_words(word_occur)

    # Print phone numbers found in the article
    phone_list = get_phone_numer(file_name)
    if not phone_list:
        print("No phone in the article")
    else:
        for phone in phone_list:
            print(f"Phone: {phone}")

check_article_content()