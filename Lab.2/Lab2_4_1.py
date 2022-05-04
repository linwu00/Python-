"""Reversed pair
revised from
Think Python by Allen B. Downey
http://thinkpython.com
"""
from sre_constants import SUCCESS
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

'''
    failed,success分别为失败和成功经验列表
    test测试词
'''

def cutable_word(test,failed,success,word_list):

    if in_bisect(failed, test):      # 先判断词是不是已经验证过的
        return False
    if in_bisect(success, test):
        return True
    
    for i in range(len(test)):       # 求出单词的所有子词 
        word_cut = list(test)
        word_cut.pop(i)
        word_cut = ''.join(word_cut)
        
        if in_bisect(success, word_cut):  # 先判断子词是不是已经验证过的
            break
        if in_bisect(failed, word_cut):
            return False


        '''
            递归处，前提是单词本身在words里，然后cutable_word判断是不是可缩减词
            是就break，包括上面的，退出循环返回True
        '''
        if in_bisect(word_list, word_cut) and cutable_word(word_cut, failed, success, word_list):
            bisect.insort(success, word_cut)
            break
    else:                               # else当循环正常结束，也就是test的所有词都不是可缩减词时，加入failed列表，返回False
        if len(test) > 2:
            bisect.insort(failed, test)
            return False

    return True
    
if __name__ == '__main__':
    start = time.time()
    #word_list = make_word_list()
    word_list = sorted(make_word_list(),key=len)
    # word_list = sorted(make_word_list(),key=len,reverse=True)
    success = ['a', 'i']
    failed = list('bcdefghjklmnopqrstuvwxyz')
    for test in word_list:
        if cutable_word(test, failed, success, word_list):
            bisect.insort(success, test)
        
    
    final_word = max(success, key=len)
    print(final_word,len(final_word))
    print(time.time() - start)
