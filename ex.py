import os
import requests
import bs4
import multiprocessing
requests.packages.urllib3.disable_warnings()
headers={

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
def get_m3u8(url):
    a=requests.get(url,headers=headers,verify=False,timeout=10)
    a.encoding="utf8"
    html=bs4.BeautifulSoup(a.text,"html5lib")
    iframe=html.find("iframe",{"name":"playlist"})
    src=iframe["src"].split("url=")[-1]
    ts_src="/".join(src.split("/")[:-1])+"/"
    a=requests.get(src,headers=headers,verify=False,timeout=10)
    ts_list=[ts_src+ts for ts in a.text.split("\n") if ".ts" in ts]
    return html.title.text,ts_list

def down_url(title,url,path):
    file=path+"/{}.mp4".format(url.split("/")[-1].split(".")[0])
    if os.path.exists(file):
        return True
    while True:
        try:
            a=requests.get(url,headers=headers,verify=False,timeout=90)
            with open(file,"wb") as f:
                f.write(a.content)
            break
        except Exception as e:
            print(e)
def main(url):
    while True:
        try:
            title,ts_urls=get_m3u8(url)
            break
        except Exception as e:
            print(e)
    path="e:video/{}".format(title)
    if not os.path.exists(path):
      os.makedirs(path)
    pool = multiprocessing.Pool(processes = 100)
    for ts_url in ts_urls:
        pool.apply_async(down_url,(title,ts_url,path))
    pool.close()
    pool.join()

    print("下载完毕")

    shiping=b""
    for file in sorted(os.listdir(path),key=lambda pp:int(pp.split("abc")[-1].split(".")[0])):
        file_name=path+"/{}".format(file)
        with open(file_name,"rb") as ff:
            shiping+=ff.read()

    with open(path+".mp4","wb") as f:
        f.write(shiping)
    print("整合完毕")
if __name__ == '__main__':
    uuls=[
    "https://tom682.com/yazhouqingse/2020-07-02/32170.html",
    "https://tom682.com/yazhouqingse/2020-06-07/31326.html",
    "https://tom682.com/yazhouqingse/2020-05-10/30165.html",
    "https://tom682.com/yazhouqingse/2020-05-04/29904.html",
    "https://tom682.com/yazhouqingse/2020-02-01/25496.html",
    "https://tom682.com/yazhouqingse/2020-01-17/24766.html",
    "https://tom682.com/yazhouqingse/2020-01-16/24716.html",
    "https://tom682.com/yazhouqingse/2019-12-30/23811.html",
    ]
    for url in set(uuls):
        main(url)





