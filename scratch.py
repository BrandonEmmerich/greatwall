# -*- coding: utf-8 -*-

def get_region(input_string):
    """Map province to region"""
    rust_belt = '天津|河北|陕西|黑龙江|吉林|山西|内蒙古'
    middle = '四川|湖南|江西|重庆|河南|湖北|安徽'
    coast = '北京|山东|福建|海南|江苏|上海|广东|浙江'
    west = '广西|云南|贵州|甘肃|新疆|青海|宁夏'

    if input_string in rust_belt:
        region = 'Rust Belt'
    elif input_string in middle:
        region = 'Populous Middle'
    elif input_string in coast:
        region = "Prosperous Coast"
    elif input_string in west:
        region = "Autonomous West"
    else:
        region = "NA"

    return region
