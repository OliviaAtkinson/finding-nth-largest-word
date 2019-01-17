list_of_strings = ['Olivia', 'Josh', 'Victoria', 'Annie', 'Ryan']

def finding_3rd_largest_word(list_of_strings):
    length = len(list_of_strings)
    sorted_list_of_strings = sorted(list_of_strings, key = len)

    print (sorted_list_of_strings)
    print ("The third largest name is: ", sorted_list_of_strings[ length - 3])

finding_3rd_largest_word(list_of_strings)