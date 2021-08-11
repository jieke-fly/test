import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import insert
def Get_amplitude_feature(action_max_second,action_min_second,action_ts_percent,faction_ts_per_add,peaks_least_dis,action_number,person_name,action_time,rx):
    '''全局变量'''
    global save_amplitude_fig3
    global save_amplitude_fig4
    global save_amplitude_excel
    global store_amplitude_database
    global data_path
    global date
    global conn
    global amplitude_xlsx_name
    global amplitude_figure_floder
    global amplitude_tabname
    global read_CSI_mode
    global dwt
    global dwt_times
    global sample_frequency


    '''读CSI区'''
    action_name = Action_name(action_number)
    if read_CSI_mode == 1:
        csi_trace = read_bf_file(print("%s%s\\%s_%s_%s_%s.dat"% (data_path,action_name,date,person_name,action_number,action_time)))
        data_30_1_1 = Read_CSI_amplitude(csi_trace,rx)
    elif read_CSI_mode == 2:
        source_CSI_dbname = Db_name_source(date,dwt,dwt_times)
        tabname_source = Tab_name_source(action_number)
        type_change_30_1_1 = py.Database_operation.Find_data_30(source_CSI_dbname,tabname_source,rx,person_name,action_time)
        data_30_1_1 = Change_py_to_mat(type_change_30_1_1)

    
    '''
figure(1);
plot(data_90_1_2');
title('原始数据');
 xlabel('时间');
%% db小波变换区
在读取幅值时，进行小波变换 2021/5/21
data_30_1_1 = data_30_1_1;
 for line = 1 : size(data_30_1_1)
     [C,L] = wavedec(data_30_1_1(line,:),4,"db3");
     data_30_1_2(line,:) = wrcoef('a',C,L,'db3',4);
end
figure(2);
plot(data_90_1_3');
title('db小波变换');
xlabel('时间');
figure(9);
plot(data_90_1_3(number,:)');
title('小波变换一个子载波');
    '''

    '''PCA降维区'''
    data_30_1_2 = np.transpose(PCA_CSI(data_30_1_1,1))
    '''
    [data_90_1_4,ser_number] = Max_var_sub_CSI(data_90_1_3,1);%第二个参数代表输出的主成分个数。
    data_90_1_4 = sgolayfilt(data_90_1_4,order,framelen); % 第二次滤波：不够平滑需要二次滤波
    '''

    
    if save_amplitude_fig3:
        plt.figure(3)
        plt.close()
        plot(data_30_1_2.T)
        plt.title('PCA')
        plt.xlabel('时间')
        plt.draw()
        plt.pause(0.1)


    '''%% 活动提取区
action_start_end = DCWC(data_30_1_2,action_max_second * 100,action_min_second * 100,action_ts_percent,action_ts_per_add);
data_30_1_3 = data_30_1_2(action_start_end(1):action_start_end(2));
% figure(4);
% clf();
% plot(data_90_1_5');
% title(sprintf('活动提取(%s _ %s _ %s _ %s(rx))',action_name,person_name,action_time,rx));
% xlabel('时间');
    action_start_end = DCWC(data_30_1_2,action_max_second*100,action_min_second * 100,action_ts_percent,action_ts_per_add)
    data_30_1_3 = data_30_1_2(action_start_end(1):action_start_end(2))
    '''

    #在pca图像上画出起始点
    if save_amplitude_fig3:
        plt.figure(3)
        plt.scatter(action_start_end[0],data_30_1_3 [0],c='k')
        plt.scatter(action_start_end[1],data_30_1_3[-1],c='k')
        plt.savefig(plt.figure(3),print("%s\%s_%s_%s_f3.jpg" % (amplitude_figure_floder,person_name,action_time,str(rx))))


    '''频域fft'''
    try:
        Get_frequency_feature(data_30_1_3,sample_frequency,action_number,person_name,action_time,rx)
    except:
        print("Get_frequency_feature error!\n")


    action_length = action_start_end[1] - action_start_end[0]
    
    s = pd.Series(data_30_1_3)
    try:
        Kurtosis = s.kurt(s)
    except:
        Kurtosis = 0
    
    try:
        Skewness = s.skew(s)
    except:
        Skewness = 0
    

    if save_amplitude_excel:
        data_line = [action_name,person_name,action_time,rx,Kurtosis,Skewness]
        np.savez("WriteMode","append",data_line,amplitude_xlsx_name)


    if store_amplitude_database:
        data.action_name = action_name
        data.persion = person_name
        data.action_time = action_time
        data.rx  = rx

        data.actioin_length = action_length

        data.kurtosis = Kurtosis
        data.skewness = Skewness

        insert(conn,amplitude_tabname,data_30_1_2)

