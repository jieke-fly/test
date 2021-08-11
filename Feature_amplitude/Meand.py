import numpy as np
import statistics  #导入这个能使用mean
def Mean(Line_CSI):
    Mean_data = np.mean(Line_CSI,0)
    dif_mean_data = abs(Line_CSI - Mean_data)
    value = np.mean(dif_mean_data,0)
    return value