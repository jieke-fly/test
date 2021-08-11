def Amplitude_feature_name(feature_number):
    a = feature_number
    if a == '1':
        feature_name = 'action_length'
    elif a == '2':
        feature_name = 'kurtosis'
    elif a == '3':
        feature_name = 'skewness'

    return feature_name
