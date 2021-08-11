import numpy as np
def Percent_data(Line_CSI,Percent):  #Percent  0-100

    #返回数据的相应百分比位的数
    data_sort = np.sort(Line_CSI)
    value = np.percentile(data_sort,Percent)
    return value