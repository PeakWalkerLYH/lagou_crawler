import requests
import pprint
import time
import random

def get_cookie():
    url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    headers1 = {
        #'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        # 'origin': 'https://www.lagou.com',
    }

    response = requests.get(url=url, headers=headers1)
    cookie = response.cookies
    # print(cookie.get_dict())

    return cookie.get_dict()


def get_content(coo, page, position):
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers2 = {
        # 'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        # 'origin': 'https://www.lagou.com',
    }
    if page == 1:
        flag = 'true'
    else:
        flag = 'false'
    data = {
        'first': flag,
        'pn': page,
        'kd': position,
        'sid': '62a7c5fb85bc4ec6be14ea01fb081d29'
    }
    response = requests.post(url, headers=headers2, data=data, cookies=coo)
    # print(response)
    return response.json()


def get_details(js, position, count):
    rs = js['content']['positionResult']['result']
    for r in rs:
        d = {
            'city': r['city'],
            'companyFullName': r['companyFullName'],
            'companySize': r['companySize'],
            'education': r['education'],
            'positionName': r['positionName'],
            'salary': r['salary'],
            'workYear': r['workYear'],
        }
        with open(f'datas/{position}{count}.csv', mode='a', encoding='utf-8')as f:
            values = d.values()
            f.write(','.join(values))
            f.write('\n')


def run(page, position, coo, count):
    json_content = get_content(coo, page, position)
    # print(json_content)

    get_details(json_content, position, count)
    print(f'第{page}页爬取完毕！')


def main(position, start, end, count):

    coo = get_cookie()
    print(coo)
    for i in range(start, end + 1, 1):
        if i % 10 == 0:
            print('正在更改cookie信息....')
            time.sleep(0.2)
            coo = get_cookie()
        run(i, position, coo, count)
        time.sleep(0.2)


if __name__ == "__main__":
    start = 3
    end = 22
    position = 'python'
    main(position, start, end, 0)
