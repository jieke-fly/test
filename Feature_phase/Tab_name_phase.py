def Tab_name_phase(action_number):
    if action_number == '1':
        train_tab_name = '1.round_right_phase_future'
    
    elif action_number =='2':
        train_tab_name = '2.round_left_phase_future'

    elif action_number == '3':
        train_tab_name = '3.not_look_front_phase_future'
    
    elif action_number == '4':
        train_tab_name = '4.hands_off_phase_future'

    elif action_number == '5':
        train_tab_name = '5.hand_in_gear_phase_future'

    elif action_number == '6':
        train_tab_name = '6.play_phone_phase_future'

    elif action_number == '7':
        train_tab_name = '7.pick_up_phase_future'

    elif action_number == '8':
        train_tab_name = '8.nod_phase_future'

    elif action_number == '9':
        train_tab_name = '9.yawn_phase_future'

    return train_tab_name
