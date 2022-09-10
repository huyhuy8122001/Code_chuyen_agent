import requests
import re

import vietnamese_dictionary
import numpy

vietnamese_dict = vietnamese_dictionary.vietnamese_dict

def split_string(input):
    output = list(input)

    #print(output)
    return output

pattern = re.compile(r'')

def re_compile(string_pattern):

    return re.compile(r'{}'.format(string_pattern), flags=re.I)

def create_pattern(string_name):
    ls = []
    for pos,char in enumerate(string_name):
        if(char == ' '):
            ls.append(pos)

    array = split_string(string_name)
    #print(array)

    final_pattern = '(' 
    for i in array:  
        for j in vietnamese_dict:  
            pattern = re_compile(j)
            matches = pattern.finditer(i)

            for match in matches:
                index = array.index(i)
                #print(index)
                for k in range(len(ls)):
                    if index == ls[k]+1:
                        #print(index)
                        final_pattern = final_pattern + '[\s|\S]?)?('

                if type(match) == re.Match :
                    final_pattern = final_pattern + '' + j
    final_pattern = final_pattern + ')'
    #print(final_pattern)
    return final_pattern

if __name__ == "__main__":
    print(create_pattern('Nguyễn Văn Đại'))