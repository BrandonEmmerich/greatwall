import pandas as pd
import requests

## Get total pages
url = 'http://www.gwamcc.com/Ajax/GetTjieInfo.ashx?pSize=100&pIndex=1'
res = requests.get(url)
total_pages = int(res.json()['pager'][0]['pCount'])


url_base = 'http://www.gwamcc.com/Ajax/GetTjieInfo.ashx?pSize=100&pIndex='
empty_list = []

for i in range(total_pages):
    print i
    res = requests.get(url_base + str(i))
    df = pd.DataFrame(res.json()['ds'])

    empty_list.append(df)

df = pd.concat(empty_list)
df.to_csv("./data/data_raw.csv", encoding = 'utf-8')
