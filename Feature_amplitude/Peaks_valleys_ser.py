import numpy as np
def Peaks_valleys_ser(Line_CSI,peaks_distance):
    loc = 2
    n = 1
    [peaks_val,peaks_ser] = Peaks_val(Line_CSI,peaks_distance)

    [valleys_val,valleys_ser] = Peaks_val_ser(-Line_CSI,peaks_distance)
    valleys_val = -(valleys_val)

    Peaks_valleys_ser = [peaks_ser,valleys_ser]
    serial = np.sort(peaks_valleys_ser)
    
    a = np.size(serial,2)
    i = 1
    for 1 in a:
        i = i+1
        if (np.find(peaks_ser == serial(i))) > 0:
            if(loc == 1):
                peak1 = peaks_val(np.find(peaks_ser == serial(i-1)))
                peak2 = peaks_val(np.find(peaks_ser == serial(i)))
                if(peaks_ser < peak2):
                    new_serial(n-1) = serial(i):
            else:
                new_serial(n) = serial(i)
                n = n + 1
                loc = 1
        else:
            if(loc == 0):
                peak1 = valleys_val(np.find(valleys_ser == serial(i-1)))
                peak2 = valleys_val(np.find(valleys_ser == serial(i-1)))
                if(peak1 > peak2):
                    new_serial(n) = serial(i)
            else:
                new_serial(n) = serial(i)
                n = n +1
                loc = 0
    return new_serial





    