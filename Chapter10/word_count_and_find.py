#
# Hands on # 3 Try it yourself 10-10
#


def count_and_find(filename):
    myFilename = file_name_formatter(filename)
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:

        print(f'Sorry, the file {myFilename} does not exist.')
    else: 
        words = contents.split()
        numWords = len(words)
        myWordCount = count_words(contents, 'the')
        myNewWordCount = count_words(contents, 'the ')
        print(f'The file {myFilename} has about {numWords} words')
        print(f'The word \'the\' was found \'{myWordCount}\' times in the file \'{myFilename}\'.')
        print(f'If I add a space at the end of \'the \' the count changes to \'{myNewWordCount}\'\n' )

def file_name_formatter(filename):       
    myStr = filename
    size = len(myStr)
    modStr = myStr[10:size-4]
    return modStr

def count_words(myContent, myString):
    ret = myContent.lower().count(myString)
    return ret

def main():
    count_and_find('Chapter10/The_Adventures_of_Sherlock_Holmes.txt')
    count_and_find('Chapter10/A_Tale_of_Two_Cities.txt')
    count_and_find('Chapter10/Dracula.txt')
    
main()
