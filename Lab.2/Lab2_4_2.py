"""Reversed pair
revised from
Think Python by Allen B. Downey
http://thinkpython.com
"""
import time
import bisect

def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    fin.close()
    return word_list

def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def cutable_word(word_list,word):
    for i in range(len(word)):
        word1 = list(word)
        word1.pop(i)
        word1 = ''.join(word1) #单词的子单词
        if in_bisect(word_list, word1) :
            return True
    return False
    
if __name__ == '__main__':
    start = time.time()
    word_list = sorted(make_word_list(),key=len)
    cutable_word_list = ['a', 'i']
    for j in word_list:
        if cutable_word(cutable_word_list, j):
            bisect.insort(cutable_word_list, j)
        
    
    
    print(len(cutable_word_list))
    final_word = max(cutable_word_list, key=len, default = '')
    print(final_word)
    print(time.time() - start)
"""
思路:初始cutable_word_list = ['a','i'],存放满足条件的单词，遍历列表，寻找满足条件的
单词，并添加到列表中，可见，列表的长度是在不断增加的，当长度不再增加的时候，查找完毕
输出列表中长度最长的单词
"""
