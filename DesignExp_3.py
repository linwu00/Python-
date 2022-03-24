import os
import time

def HuiWenReverseWords(pathOrigin, sets):
    try:
        if os.path.exists(pathOrigin):
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            words = f1.read().split()
            f1.close()
            length = 0
            for ele in words:
                if ele[::-1] == ele:
                    sets.add(ele)
                    length += 1
        print("回文单词的个数为:", length)
    except:
        print('发生异常.')

def ReverseWords(pathOrigin, sets):
    try:
        if os.path.exists(pathOrigin):
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            words = f1.read().split()
            f1.close()
            length = 0
            for ele in words:
                if ele[::-1] in words:
                    sets.add(ele)
                    length += 1
        print('反序序列总数:',length)
    except:
        print('发生异常.')
def ReverseWordsUpdate(pathOrigin):
    try:
        if os.path.exists(pathOrigin):
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            words = f1.read().split()
            f1.close()
            length = 0
            sets1 = set(); sets2 = set()
            for ele in words:
                sets1.add(ele)
                sets2.add(ele[::-1])
        print('反序序列总数:',len(sets1&sets2))
        return sets1&sets2
    except:
        print('发生异常.')

def main():
    pathOrigin = 'words.txt'
    sets1 = set()
    sets2 = set()
    HuiWenReverseWords(pathOrigin, sets1)
    print('回文单词为:',sets1)

    start = time.time()
    ReverseWords(pathOrigin, sets2)
    print('ReverseWords用时:', time.time()-start)
    print(sets2)

    start = time.time()
    sets = ReverseWordsUpdate(pathOrigin)
    print('ReverseWordsUpdate用时:', time.time()-start)
    # for ele in sets:
    #     print(ele,':',ele[::-1])
    print('回文序列为:',sets)

main()
