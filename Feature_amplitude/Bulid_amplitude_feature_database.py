import os
def Main_build():
    #函数版  main_build_database

    '''参数区'''
    global action_ts_percent
    global dbname
    global action_max_second
    global action_min_second
    action_number = 9
    all_action_time = 3   #动作总次数
    

    action_max_second = 3.0  #动作最大秒数
    action_min_second = 1.0  #动作最小秒数
    action_ts_percent = 0.5  #阈值
    

    action_ts_per_add = 0.01  #每次增加阈值
    peaks_least_dis = 50      #峰值差值
    person_count = 6          #人数
    all_rx_count = 9          #链路个数


    dbname = 'data0511'     #跑相同的动作需要修改


    '''全局变量区'''
    global save_fig3
    save_fig3 = 0              #1保存文件

    global save_fig4
    save_fig4 = 0              #1保存文件

    global save_excel
    save_excel = 0             #1保存文件

    global file_path_prefix    #保存文件路径
    file_path_prefix = "D:\soft2\Matlab2020a\matlab\drive_csi\0513"
    #global data_path


    '''数据录入区'''
    i = 1
    if save_fig3 or save_fig4:
        for 1 in action_number:
            new_figure_floder = print('%s\\fig\\%s' % (file_path_prefix,Action_name(i))) #new_folder 保存要创建的文件夹，是绝对路径+文件夹名称
            i = i + 1
            os.mkdir("new_figure_floder")  #创建文件夹

    if save_excel:
        new_excel_floder = print('%s\\xls' % (file_path_prefix))  #new_folder 保存要创建的文件夹，是绝对路径+文件夹名称
        os.mkdir('new_excel_floder')       #创建文件夹

    for 1 in 9:
        i = 1
        action_number = str(i)
        Store_amplitude_feature(all_action_time,action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,dbname,action_number,person_count,all_rx_count)
        i = i + 1