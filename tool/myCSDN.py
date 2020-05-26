import urllib
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import socket
import http.cookiejar as cookielib

hrefs=[
    'https://august-us.blog.csdn.net/article/details/106210576',  # 激活函数Swish
    'https://august-us.blog.csdn.net/article/details/106211472',  # 亚马逊的一道智力题，悬链线问题
    'https://august-us.blog.csdn.net/article/details/106151534',  # 阿里云服务器上配置ssh反向代理
    'https://august-us.blog.csdn.net/article/details/106103435',  # 视觉问答领域中的常用方法
    'https://blog.csdn.net/m0_38065572/article/details/106079613',  # 视觉问答领域中的数据和评价指标
    'https://blog.csdn.net/m0_38065572/article/details/106078530',  # 二分查找，来一道不是那么复杂的题目
    'https://blog.csdn.net/m0_38065572/article/details/104718500',  # 深度学习中的Normalization
    'https://blog.csdn.net/m0_38065572/article/details/105783418',  # 2020年腾讯实习生算法笔试题目(感触良多)
]

socket.setdefaulttimeout(5000)  # 设置全局超时函数
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        # 'cookie': 'bdshare_firstime=1498729927584; smidV2=20180607101440e922ed7d96b71fe577fa25c76f8977d40048bae4039e1b9c0; dc_session_id=10_1534762107703.131799; __yadk_uid=FZfHZZf0ZGx5AoewQ9NGsiPwvnhDpO0V; uuid_tt_dd=10_19643783640-1580030457608-159990; Hm_ct_62052699443da77047734994abbaed1b=5744*1*m0_38065572!6525*1*10_19643783640-1580030457608-159990; TY_SESSION_ID=c2ea99d8-4e09-415e-96d7-ae122a157473; Hm_lvt_eb5e3324020df43e5f9be265a8beb7fd=1582003345; Hm_lpvt_eb5e3324020df43e5f9be265a8beb7fd=1582003345; Hm_ct_eb5e3324020df43e5f9be265a8beb7fd=5744*1*m0_38065572!6525*1*10_19643783640-1580030457608-159990; Hm_lvt_62052699443da77047734994abbaed1b=1581578483,1581861353,1582004148; Hm_lpvt_62052699443da77047734994abbaed1b=1582004148; searchHistoryArray=%255B%2522August-us%2522%252C%2522luolan9611%2522%252C%2522Python%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%2522%255D; SESSION=36a5c82f-08d6-45c7-b0a3-cac7fe0c93dc; UserName=m0_38065572; UserInfo=ff6919ac07d042c8ba5cc828256560de; UserToken=ff6919ac07d042c8ba5cc828256560de; UserNick=August-us; AU=E10; UN=m0_38065572; BT=1582164346920; _uid=U000000; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19643783640-1580030457608-159990!1788*1*PC_VC!5744*1*m0_38065572; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1582441649,1582460045,1582460105,1582460108; firstDie=1; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; c_adb=1; dc_tos=q67px4; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1582558457',
        # 'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=DyFr9j72srw0PC61clKIOX9fSCBPEoCR3dLLtJN7rLhkfAoGOa7IA-b5czXNkP9t3bYLJ6tltSi1ulk3AzP0Ah2h1i6v442nxgBalH23Sei&wd=&eqid=b7fe06d70000a5b0000000065ea2d6f9; uuid_tt_dd=10_10355772510-1587730171244-708343; dc_session_id=10_1587730171244.493204; TY_SESSION_ID=63507c8d-41b8-4c53-aba2-006285ca6abe; c_first_ref=www.baidu.com; c_first_page=https%3A//blog.csdn.net/m0_38065572/article/details/104195388; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1587730171; dc_sid=a54a2059bd38fccba94c09d8abf34b3e; __gads=ID=46d39c0bfad73c76:T=1587730172:S=ALNI_MbmEsVL3fn7qZp6Wwzd3GpM2n0XGA; SESSION=2edf2a17-3012-4a27-bd55-9f4a186fbd1e; c_ref=https%3A//blog.csdn.net/m0_38065572/article/details/104195388; UserName=August_us1; UserInfo=45d7f8b8487e442291232c768d94e0cc; UserToken=45d7f8b8487e442291232c768d94e0cc; UserNick=August_us1; AU=ECF; UN=August_us1; BT=1587730247831; p_uid=U000000; dc_tos=q9aki2; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1587730251; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_10355772510-1587730171244-708343!5744*1*August_us1; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F105203745%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D'
        # 'cookie':'BAIDU_SSP_lcr=https://www.baidu.com/link?url=peOmVYPfHRFwAeF_Le4Lfp74gX_qsWprxYt0I-6GIxXMtzSRxEO7VYrJ2OmP9iIrTpjjAM-Wm5jXCIBKrbeeBwgmJbzUj3yOS5vQsRZOoqq&wd=&eqid=98da8f0b00147119000000065e7aa6b2; uuid_tt_dd=10_19643781190-1585096373148-744287; dc_session_id=10_1585096373148.971328; TY_SESSION_ID=1baadccf-2766-45ab-9f8a-0674010d1710; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1585096374; __gads=ID=b42f0f43afc32006:T=1585096374:S=ALNI_MaYt_Rogz4PXaGfAqVIKHGAM-YiGQ; c_ref=https%3A//blog.csdn.net/m0_38065572%3Ft%3D1; SESSION=cfdf0a0e-452f-4a80-ac47-2d5076ca7103; UserName=August_us1; UserInfo=39553f7f5c58440fa31d449d54a0f7d1; UserToken=39553f7f5c58440fa31d449d54a0f7d1; UserNick=August_us1; AU=ECF; UN=August_us1; BT=1585096402624; p_uid=U000000; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19643781190-1585096373148-744287!5744*1*August_us1; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; hasSub=true; dc_tos=q7q5n7; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1585098260',
}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 设置代理IP
# 代理IP可以上http://ip.zdaye.com/获取
proxy_handler = urllib.request.ProxyHandler({'post': '127.0.0.1:1080'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
urllib.request.install_opener(opener)
# 得到CSDN博客某一个分页的所有文章的链接
articles = set()
pages = set()
vaild=0


def getArticleLinks(pageUrl):
    # 获取网页信息
    # print(pageUrl)
    global session
    # session.cookies.load()
    html = session.get(pageUrl, headers=headers2).text
    # html = req.decode('utf-8')
    global vaild
    vaild+=int('August-us' not in html)
    time.sleep(20)
    session.cookies.save()


def getPageLinks(bokezhuye):
    # 获取网页信息
    req = request.Request(bokezhuye, headers=headers2)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    # print(bsObj)
    # 获取当前页面(第一页)的所有文章的链接
    # print(bsObj.findAll("a", href=re.compile("(/article)(/details)(/[0-9]+)*$")))
    # 去除重复的链接
    global pages
    # for pagelist in bsObj.findAll("a", href=re.compile("^/([A-Za-z0-9]+)(/article)(/details)(/[0-9]+)*$")):  # 正则表达式匹配分页的链接
    for pagelist in bsObj.findAll("a", href=re.compile("(/article)(/details)(/[0-9]+)*$")):
        if 'href' in pagelist.attrs:
                newPage = pagelist.attrs["href"]
                # print(newPage)
                # 获取接下来的每一个页面上的每一篇文章的链接
                # newPageLink = "http://blog.csdn.net/" + newPage
                # if newPage=="https://blog.csdn.net/m0_38065572/article/details/104009414":
                #     continue
                getArticleLinks(newPage)
                # 爬取每一篇文章的文字内容
                # for articlelist in articles:
                #     newarticlelist = "http://blog.csdn.net/" + articlelist
                #     # print(newarticlelist)
                #     getArticleText(newarticlelist)


def loginPages():
    url = "https://passport.csdn.net/account/login?ref=toolbar"
    # 请求报头
    # 创建session保存cookie
    # 获取响应内容
    html='https://blog.csdn.net/m0_38065572/article/details/104133880'
    html = session.get(html, headers=headers2).text
    # 使用lxml格式
    bs = BeautifulSoup(html, "lxml")

    # 获取lt值
    login = bs.find("input", attrs={"name": "lt"}).get("value")
    lt = bs.find("input", attrs={"name": "lt"}).get("value")
    print(lt)
    # 获取execution值
    ex = bs.find("input", attrs={"name": "execution"}).get("value")
    print(ex)

    # 创建data表单数据
    data = {
        # "username": "你的用户名",
        # "password": "你的密码",
        "lt": lt,
        "execution": ex,
        "_eventId": "submit",
    }
    # 获取登录cookie值
    # session.post(url, data=data, headers=headers2)

    # 获取登录后页面
    # http://write.blog.csdn.net/postlist
    response = session.get("https://blog.csdn.net/m0_38065572/article/details/104133880", headers=headers2).text
    # print response

    # 提取页面博文目录列表信息
    bs2 = BeautifulSoup(response, "lxml")
    links = bs2.find_all("a", attrs={"target": "_blank"})
    print(len(links))

if __name__ == '__main__':
    import time
    while True:
        try:
            # getPageLinks("https://blog.csdn.net/m0_38065572")
            session = requests.Session()
            session.cookies = cookielib.MozillaCookieJar(filename='cookies.txt')
            for href in hrefs:
                getArticleLinks(href)
            session.cookies.clear()
        except Exception as e:
            print(e)
            vaild+=1
        if vaild >100:
            print('Exit' +'-'*30)
            break



