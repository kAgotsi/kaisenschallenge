import re

"""
    This function matches a string that has an a followed by zero or more b's 
    
    Parameters
    ----------
    text : str
        The input text
    Return
    ------
    str: Found a match or not matched
"""
def test_1(text):
    patterns = 'ab*?'
    if re.search(patterns,  text):
        return 'Found a match'
    else:
        return('Not matched!')

"""
    This function find sequences of one upper case letter followed \
     by lower case letters 
     
    Parameters
    ----------
    text : str
        The input text
    Return
    ------
    str: Found a match or not matched
"""
def test_2(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns,  text):
            return 'Found a match!'
    else:
            return('Not matched!')
    
"""
    This function matches a string that has an 'a' followed by anything,\
    ending in 'b'
    
    Parameters
    ----------
    text : str
        The input text
    Return
    ------
    str: Found a match or not matched
"""
def test_3(text):
    patterns = 'a.*?b$'
    if re.search(patterns, text):
        return 'Found a match'
    else:
        return('Not matched')
    
"""
    This function  matches a word containing 'z', not start or end of the word
    
    Parameters
    ----------
    text : str
        The input text
    Return
    ------
    str: Found a match or not matched
"""    
def test_4(text):
    patterns = '\Bz\B'
    if re.findall(patterns,text):
        return 'Found a match'
    else:
        return 'Not matched'
    
"""
    This function split a string with multiple delimiters
    
    Parameters
    ----------
    text : str
        The input text
    Return
    ------
    list: a strings splited
"""
def test_5(text):    
    return re.split('; |, |\*|\n',text)

"""
    This function find all adverbs and their positions in a given sentence \
        (do this exercise for Englishadverbs and French adverbs)
        
    I have only taken into account the general cases where adverbs \
         in English end in ly and in French in amment or emment or ement
        
    Parameters
    ----------
    text : str
        The input sentences
    Return
    ------
    list: adverbs
"""    
def test_6(text):
    patterns = r"(\w+ly|\w+amment|\w+emment|\w+ement)"
    all = re.findall(patterns,text)
    return all
            

""" 
    This function find all Dates in a text (Both French Format and English Format )
    I have taken into account formats such as:
        dd-mm-yyyy ; dd/mm/yyyy ; dd-mm-yy ; dd/mm/yy ; mm-dd-yyyy ; mm/dd/yyyy
        dd Month years ; dd Month (th|rd|nd|st), years; 
        
    Parameters
    ----------
    text : str
        The input sentences
    Return
    ------
    list: dates        
"""
def test_7(text):
    all = re.findall(r'[\d]\w* [ADFJMNOS]\w* [\d]{4} | [\d]{1,2}/[\d]{1,2}/[\d]{4} | [\d]{1,2}-[\d]{1,2}-[\d]{4} | [\d]{1,2} [ADFJMNOS]\w* [\d]{4}|[ADFJMNOS]\w* [(\d)]\w*, [\d]{4}|[\d]{1,2}-[\d]{1,2}-[\d]{2} | [\d]{1,2}/[\d]{1,2}/[\d]{2}', text)
    return all

    
    
"""
    Main function enables you to test the functions by setting parameters with values. \
    In order to test each function, you must call function and put text as paramater \
    and execute
    
"""
def main():
    print(test_1('abbc'))
    print(test_2('aab_Abbbc'))
    print(test_3('atttttffffeeeb'))
    print(test_4('Tazzza'))
    print(test_5('Beautiful, is; better*than\nugly'))
    print(test_6('Clearly, rapidement, méchamment apparemment has no excuse for such behavior.'))
    print(test_7('hello user, today  12th March 2020  12 March Street 12, March 12,2020, On March 12th, 2020 On 10/10/2015 On 10 March 2020 on 10/10/20, On March 1st, 2012 On 10-10-2015 on 10-10-15 on 4 NOv 2018 New York, NY 12345 from'))

if __name__ == '__main__':
    main()
    
    
    
    
    
    

