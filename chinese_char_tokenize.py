'''
tokenizer for chinese at character level mixed with english words and numbers.
this is different from segmentation, where the goal is to combine characters to from words.
author: Lee
'''

from nltk.tokenize import RegexpTokenizer
import read
import string

tokenizer = RegexpTokenizer(u'[\u2E00-\u9fff]|[0-9]+|[a-zA-Z]+|[%s]'% re.escape(string.punctuation))

def zh_char_tokenize(sentence):
    '''
    handeling chinese character is tricky, input format is usually utf8 for linux based systems, never tested but should be gbk for windows systems (not tested)
    :param sentence: sentence to tokenize in utf8 format
    :return tokenized_sentence: tokens of the given sentence in unicode
    '''
    return tokenizer.tokenize(unicode(sentence.decode('utf8')))