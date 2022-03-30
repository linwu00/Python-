# 统计单词频数

import re
import os
import wordcloud
import string
from collections import Counter
import time

def CountWords(pathOrigin, pathResult):
    try:                                   
        if os.path.exists(pathOrigin):          # 1.防止文件操作异常
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            EnglishText = f1.read().split()
            f1.close()
            new_EnglistText = []
            ans = {}
            pun = '[~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：”’；、。，？》《}{]'
            # pun = '[' + string.punctuation + ']'      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            for ele in EnglishText:
                # 2.为防止符号影响，去掉句子中的标点
                new_EnglistText.append(re.sub(pun , '', ele).lower())
            c = Counter(new_EnglistText)        # Counter
            ans = dict(c)        
            word_counts = dict(c.most_common(50))
            ans_order = dict(sorted(ans.items(), key=lambda x:-x[1]))           # 3.sorted进行降序排序
            if not os.path.exists(pathResult):                  # 4.判断文件是否存在
                with open(pathResult,'w') as f2:
                    for k, v in ans_order.items():
                        f2.write(k + ': ' + str(v) + '\n')
            else:
                f3 = open(pathResult, 'w')
                for k, v in ans_order.items():
                    f3.write(k + ': ' + str(v) + '\n')
                f3.close()
            print("已成功统计！")
    except:
        print('发生异常.')
        
    return word_counts

def WordCld(word_counts, file_name):           # 绘制词云
    w = wordcloud.WordCloud(background_color='white', width=800, height=400)       
    w.generate_from_frequencies(word_counts)
    w.to_file(file_name + '.png')
    print('词云已实现.')

if __name__ == '__main__':
    start_time = time.time()
    pathOrigin = 'I_Have_a_Dream.txt'
    # pathOrigin = 'NYTimes.txt'
    pathResult = list(pathOrigin.split('.'))[0] + 'Result_2.txt'
    wordCnts = CountWords(pathOrigin, pathResult)
    print('用时: {}'.format(time.time()-start_time))
    WordCld(wordCnts, list(pathOrigin.split('.'))[0])
