import json
import requests
from gerapy_auto_extractor.extractors.list import extract_list
from gerapy_auto_extractor.extractors import extract_detail

# html = open('list.html', encoding='utf-8').read()
headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
# "Host":"search.ccgp.gov.cn",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}

url="http://www.taihe.gov.cn/opennessContent/iframe/?branch_id=54014be15837eedf9b7dd15a&column_code=250400&page=1"
# url="http://www.taihe.gov.cn/openness/detail/5dbbf2fc7f8b9a17788b4572.html"
a=requests.get(url,headers=headers)
html=a.text


# with open("e:/python/ex.html","rb") as f:
# 	html=f.read().decode("utf8")




bb=extract_list(html)
# print([print(b) for b in bb])
print(len(bb))



# bb=extract_detail(html)
# # print([print(b) for b in bb])
# # print(len(bb))
# print(bb["content"].replace("\\n","\n"))




