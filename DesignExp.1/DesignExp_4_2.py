# 统计单词关键词数

import re
import os
import string

def CountWords(pathOrigin, lists):
    try:                                    # 防止文件操作异常
        if os.path.exists(pathOrigin):
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            EnglishText = f1.read().split()
            f1.close()
            new_EnglistText = []
            ans = {}
            for ele in EnglishText:
                # 为防止符号影响，去掉句子中的标点
                new_EnglistText.append(re.sub('[' + string.punctuation + ']' , '', ele).lower())
            for word in new_EnglistText:
                ans[word] = new_EnglistText.count(word)
            
            for element in lists:
                element0 = element
                element = element.lower()
                if element in ans.keys():
                    print(element0 + ': ' + str(ans[element]))
                else:
                    print(element0 + ': ' + '0')
    except:
        exit(0)
if __name__ == '__main__':
    pathOrigin = 'I_Have_a_Dream.txt'
    objLists = list(input('请输入您所要查找的关键词(以空格分隔): ').split())
    CountWords(pathOrigin, objLists)
