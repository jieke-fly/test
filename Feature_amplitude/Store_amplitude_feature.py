import os
def Store_amplitude_feature(all_action_time,action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,action_number,person_count,all_rx_count):
    #存一个动作的全部时域幅值信息
    '''之前已有全局变量区'''
    global conn
    global save_amplitude_excel
    global amplitude_excel_floder
    global save_amplitude_fig3
    global save_amplitude_fig4
    global store_amplitude_database
    global amplitude_feature_floder_prefix

    global save_frequency_excel
    global frequence_excel_folder
    global save_frequence_fft_fig
    global store_frequency_database
    global frequence_figure_floder_prefix

    '''新增全局变量区'''
    global amplitude_figure_floder
    if save_amplitude_fig4 or save_amplitude_fig3:
        amplitude_figure_floder = print('%s\\%s' % (amplitude_figure_floder_prefix,Action_name(action_number))) #new_folder 保存要创建的文件夹，是绝对路径+文件夹名称
        os.mkdir(amplitude_figure_floder)  #os.mkdir()函数创建文件夹

    global amplitude_xlsx_name
    if save_amplitude_excel:
        amplitude_xlsx_name = print('%s\\%s.xlsx',amplitude_excel_folder,Action_name(action_number))
        title_line = ["动作","名字","次数","链路","峰度","偏度"]
        writematrix(title_line,amplitude_xlsx_name,'WriteMode','append')


    global amplitude_tabname
    amplitude_tabname = "no_table"
    if store_amplitude_database:
        #时域幅值数据表
        amplitude_tabname = Tab_name_amplitude(action_number)
        try:
            createCollection(conn, amplitude_tabname)
        except:
            print("%s has been created\n",amplitude_tabname)

    '''频域'''
    global frequency_figure_floder
    if save_frequency_fft_fig:
        frequency_figure_floder = print('%s\\%s' % (frequency_figure_floder_prefix,Action_name(action_number))) # new_folder 保存要创建的文件夹，是绝对路径+文件夹名称
        os.mkdir(frequency_figure_floder)

    global frequency_xlsx_name
    if save_frequency_excel:
        frequency_xlsx_name = print('%s\\%s.xlsx' % (frequency_excel_folder,Action_name(action_number)))
        title_line = ["动作","名字","次数","链路","平均频率","重心频率","频率均方根","频率标准差"]
        writematrix(title_line,frequency_xlsx_name,'WriteMode','append')


    global frequency_tabname
    frequency_tabname = 'no_table'
    if store_frequency_database:
        #时域幅值数据表
        frequency_tabname = Tab_name_frequency(action_number)
        try:
            createColection(conn,frequency_tabname)
        except:
            print("%s has been created\n" % (frequency_tabname))

    person_number = 1
    action_time_num = 1
    rx = 1
    for 1 in person_count:
        person_name = Person_name(str(person_number))
        person_number = person_number + 1
        for 1 in all_action_time:
            action_time_num = action_time_num + 1
            for 1 in all_rx_count:
                try:
                    Get_amplitude_feature(action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,action_number,person_name,str(action_time_num),rx)
                except:
                    print("Get_amplitude_feature error!\n") 
                rx = rx + 1