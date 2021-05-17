

try:

    1/0
except ZeroDivisionError as e:
    print("这里是除以零的捕获错误")
    print("错误提醒：",e)

except Exception as e:
    print("这里是其它所有类型错误")
    print("错误提醒：",e)
    
else:
    print("没有错误则执行这里")

finally:
    print("无论对错，都执行")

import pandas as  pd
from pandas.core.frame import DataFrame

df = pd.DataFrame()


