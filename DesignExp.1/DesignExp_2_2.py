# GUI交互

import datetime
import re
import easygui as es

while True:
    try:
        time = es.enterbox(msg='Time', title='请输入时_分_秒', default=' ', strip=True, image=None, root=None)
        hour, min, sec = (map(int, re.split("[:：' ']", time)))
        datetime.time(hour, min, sec)
        sec = hour * 3600 + min * 60 + sec + 1
        result = datetime.timedelta(-1,sec)
        if(not (es.ccbox(msg=str(result), title='result', choices=('继续', '结束'), image=None))):
            break
        continue
    except:
        if(not (es.ccbox(msg='请输入在正确的时间范围内', title='result', choices=('继续', '结束'), image=None))):
            break
        continue
