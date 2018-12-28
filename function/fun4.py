def city_temp(**param):
    print(param)
    print(type(param))
    for key, value in param.items():
        print(key, ':', 'value')

city_temp(bj='32', sh='33', sz='34')