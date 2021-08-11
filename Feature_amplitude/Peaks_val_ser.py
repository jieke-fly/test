import numpy as np
import statistics  #导入这个能使用mean
from scipy.signal import find_peaks
def Peaks_val_ser(Line_CSI,peaks_min_distance):
    #返回峰的值与序列号
    OK = 0
    [value_peaks,ser_peaks] = find_peaks(Line_CSI,'minpeakdistance',peaks_min_distance)
    x = [value_peaks,ser_peaks]    
    count_peaks = np.size(x)
    i = 1
    while OK == 0:
        if count_peaks > 1:
            for 1 in (count_peaks-1):
                dis_peaks(i) = ser_peaks(i+1) - ser_peaks(i)
                mean_dis_peaks = statistics.mean(dis_peaks(1,))
                [new_peaks_value,new_ser_peaks] = find_peaks(Line_CSI,'minpeakdistance',mean_dis_peaks)
                new_count_peaks = np.size(ser_peaks,2)
                if new_count_peaks == count_peaks:
                    OK = 1
                else:
                    count_peaks = new_count_peaks
                    ser_peaks = new_ser_peaks
                    peaks_value = new_peaks_value

        else:
            OK = 1
    value = [value_peaks,ser_peaks]
    return value