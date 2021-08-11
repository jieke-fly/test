import numpy as np
import statistics
def Mad(Line_CSI):
    # UNTITLED6 此处显示有关函数的摘要
    # 此处显示详细说明
    Median_data = np.median(Line_CSI,axis=0)
    dif_median_data = abs(Line_CSI - Median_data)
    value = np.mean(dif_median_data,0)
    return value