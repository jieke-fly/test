def Tab_name_amplitude(action_number):
    #输入动作编号，获取训练表的名字
    if action_number == '1':
        tab_name = '1.round_right_amplitude_feature'

    elif action_number == '2':
        tab_name = '2.round_left_amplitude_feature'

    elif action_number == '3':
        tab_name = '3.not_look_front_amplitude_feature'

    elif action_number =='4':
        tab_name = '4.hands_off_amplitude_feature'

    elif action_number == '5':
        tab_name = '5.hand_in_gear_amplitude_feature'

    elif action_number == '6':
        tab_name = '6.play_phone_amplitude_feature'

    elif action_number == '7':
        tab_name = '7.pick_up_amplitude_feature'

    elif action_number == '8':
        tab_name = '8.nod_amplitude_feature'

    elif action_number == '9':
        tab_name = '9.yawn_amplitude_feature'
        

    return tab_name