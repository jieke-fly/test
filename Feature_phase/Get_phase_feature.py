import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import insert
import pandas as pd
import pymongo
def Get_phase_feature(action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,action_number,person_name,action_time,rx,tx):
    '''全局变量'''
    global save_phase_fig3
    global save_phase_fig4
    global save_phase_excel
    global store_phase_database
    global data_path
    global date
    global conn
    global phase_xlsx_name
    global phase_figure_floder
    global phase_tabname
    global read_CSI_phase_mode
    global dwt
    global dwt_times

    ''''''
    action_name = Action_name(action_number)
    if read_CSI_phase_mode == 1:
        csi_trace = read_bf_file(print("%s%s\\%s_%s_%s_%s.dat" % (data_path,action_name,date,person_name,action_number,action_time)))
        data_30_1_1 = Read_CSI_phase(csi_trace,tx,rx)
    elif read_CSI_phase_mode == 2:
        source_CSI_dbname = Db_name_source(date,dwt,dwt_times)
        tabname_source = Tab_name_source(action_number)
        type_change_30_1_1 = py.Database_operation.Find_data_30(source_CSI_dbname,tabname_source,rx,person_name,action_time)
        data_30_1_1 = Change_py_to_mat(type_change_30_1_1)
    

    data_30_1_3 = hampel(data_30_1_1,90,0.001)

    data_30_1_4 = PCA_CSI(data_30_1_3,1)

    if save_phase_fig3:
        #画图
        plt.figure(3)
        plt.plot(data_30_1_4.T)
        plt.title('PCA')
        plt.xlabel('time')
        plt.show()

    action_start_end = DCWC(data_30_1_4,action_max_second*100,action_min_second*100,action_ts_percent,action_ts_per_add)
    data_30_1_5 = data_30_1_4(action_start_end[0]:action_start_end[1])

    if save_phase_fig3:
        #画图
        plt.figure(3)
        plt.scatter(action_start_end[0],data_30_1_5[0],c = 'k')
        plt.scatter(action_start_end[1],data_30_1_5[-1],c = 'k')
        plt.axis('off')
        plt.savefig(plt.plot(data_30_1_4_t),print("%s\\%s_%s_%s_f3.jpg" % (phase_figure_floder,person_name,action_time,str(rx))))



    action_length = action_start_end[1] - action_start_end[0]
    s = pd.Series(data_30_1_5)
    try:
        Kurtosis = s.kurt()
    except:
        Kurtosis = 0

    try:
        Skewness = s.skew()
    except:
        Skewness = 0 
    

    if save_phase_excel:
        data_line = [action_name,person_name,action_time,(tx - 1) * 3 + rx,Kurtosis,Skewness]
    


    if store_phase_databese:
        data.action_name = action_name
        data.person = person_name
        data.action_time = action_time
        data.rx = rx
        data.tx = tx
        data.action_length = action_length
        data.kurtosis = Kurtosis
        data.skewness = Skewness
        insert(conn,phase_tabname,data)