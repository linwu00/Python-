import re
import os
import time

def CountWords(pathOrigin, pathResult):
    count = 0
    try:                                   
        if os.path.exists(pathOrigin):          # 1.防止文件操作异常
            f1 = open(pathOrigin, 'r', encoding='utf-8')
            EnglishText = f1.read().split()
            f1.close()
            new_EnglistText = []
            ans = {}
            pun = '[~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：”’；、。，？》《}{]'
            for ele in EnglishText:
                # 2.为防止符号影响，去掉句子中的标点
                new_EnglistText.append(re.sub(pun, '', ele).lower())
            for word in new_EnglistText:
                ans[word] = new_EnglistText.count(word)
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

if __name__ == '__main__':
    start_time = time.time()
    # pathOrigin = 'I_Have_a_Dream.txt'
    pathOrigin = 'NYTimes.txt'
    pathResult = list(pathOrigin.split('.'))[0] + 'Result.txt'
    CountWords(pathOrigin, pathResult)
    print('用时: {}'.format(time.time()-start_time))
