import os
def Store_phase_feature(all_action_time,action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,action_number,person_count,all_rx_count):
    #存一个动作的全部时域幅值信息，
    '''之前已有全局变量'''
    global conn
    global save_phase_excel
    global phase_excel_folder
    global save_phase_fig3
    global save_phase_fig4
    global store_phase_database
    global phase_figure_floder_prefix

    '''新增全局变量区'''
    global phase_figure_floder

    if save_phase_fig3 or save_phase_fig4:
        phase_figure_floder = print('%s\\%s' % (phase_figure_floder_prefix,Action_name(action_number))) #new_folder 保存要创建的文件夹，是绝对路径+文件夹名称
        os.mkdir(amplitude_figure_floder)

    global phase_xlsx_name
    if save_phase_excel:
        phase_xlsx_name = print('%s\\%s.xlsx' % (phase_excel_folder,Action_name(action_number)))
        title_Line = ["动作","名字","次数","链路","峰度","偏度"]
        writematrix(title_line,phase_xlsx_name,'WriteMode','append')

    global phase_tabname
    phase_tabname = "no_table"
    if Store_phase_feature:
        #时域相位数据表
        phase_tabname = Tab_name_phase(action_number)
        try:
            createCollection(conn, phase_tabname)
        except:
            print("%s has been created\n" % (phase_tabname))

            
    person_number = 1
    action_time_num = 1
    for 1 in person_count:
        person_name = Person_name(persion_number)
        person_number = person_number + 1
        for 1 in all_action_time:
            for 0 in (all_rx_count-1):
                try:
                    Get_phase_feature(action_max_second,action_min_second,action_ts_percent,action_ts_per_add,peaks_least_dis,action_number,person_name,num2str(action_time_num),rem(antenna,3) + 1,fix(antenna / 3) + 1)
                except:
                    print("get_phase_feature erro!")





