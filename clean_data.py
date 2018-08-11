# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def _clean_numbers(raw_price):
    """Take raw price as argument and return cleaned float
    Note: this doesn't handle ranges (1000-5000) or equity figures (65万股)
    Note: it also just coerces everything it doesn't understand into NA"""
    pattern = "(人民币|亿|万元|元|,|（.*）|(抵债资产账面值)|：|(以下|以上)|-.+|万股|本金|及|相应利息|以及利息、费用|股权总额|利息|债权总额)"
    stripped = raw_price.str.replace(pattern,"").astype(float, errors = 'ignore')

    return pd.to_numeric(stripped, errors = 'coerce')

def _get_units(raw_price):
    """Take a raw price as the argument and return 1, 10k, or 100 million as a float"""

    conversion_factor = np.where(
        raw_price.str.contains("万") == True, 10000.0,
        np.where(raw_price.str.contains("亿") == True, 100000000.0,1.0))

    return conversion_factor

def clean_price(raw_price):
    """Take a raw price as an argument and return a number, in units of RMB, as
    the clean price"""

    df = pd.DataFrame({
        'price_raw' : raw_price,
        'conversion_factor' : _get_units(raw_price),
        'price_numbers' : _clean_numbers(raw_price),
    })

    df['price_clean'] = df['conversion_factor'] * df['price_numbers']

    return df['price_clean']

df = pd.read_csv("./data/data_raw.csv")
df['price_clean'] = clean_price(df.MoneyTotal)

df.to_csv('./data/data_clean.csv', encoding = 'utf-8')

import ipdb; ipdb.set_trace()
