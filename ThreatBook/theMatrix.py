# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 3:34 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: heikediguo.py
# @Software: PyCharm
import requests
from lxml import etree
def getList():

    headers = {
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'authority': 'spyhackerz.org',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '__cfduid=d6869bddf7495e8adf8ecdc184c01970f1614323722; cf_chl_prog=a19; cf_clearance=75f70b41928ea9d69c688336281cae4b140b3590-1614323843-0-250; __cf_bm=8b88a164ddee8ec7f4e9c0e169e5aa5e43930c51-1614323845-1800-ARlWarJVQ+XknFR+92h1yl+u4EB8cnkR9dk0nTQ2wc5IuGIphwyU5/5HA1I2RZdog4Jn6MVAc04nTOlJQe6DBQQqtZ7LD1GP0N/uqRHFXtpil9K2RTQLRt3Ye+bGrJQGZg==; xf_csrf=FIoTGH7zY2rNLvyq',
        'origin': 'https://spyhackerz.org',
        'referer': 'https://spyhackerz.org/forum/whats-new/posts/273550/',
        'x-client-data': 'CI22yQEIpLbJAQjEtskBCKmdygEI+MfKAQijzcoBCNzVygEIqJzLAQjGnMsBCOOcywEIqZ3LAQi3n8sB',
    }

    response = requests.get('https://spyhackerz.org/forum',proxies=proxies, headers=headers)
    print(response.text)

    print(response.status_code)

def raidforums():

    headers = {
        # 'authority': 'raidforums.com',
        # 'pragma': 'no-cache',
        # 'cache-control': 'no-cache',
        # 'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        # 'sec-ch-ua-mobile': '?0',
        # 'upgrade-insecure-requests': '1',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.0; rv:55.0) Gecko/20100101 Firefox/55.0',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'sec-fetch-site': 'none',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-user': '?1',
        # 'sec-fetch-dest': 'document',
        # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'cookie': 'cf_clearance=ae6cc26ace160c35640c6bc44dd5632ea80c9468-1614602357-0-250;',
        # 'cookie': 'cf_clearance=30d1dbb987a04acbbd685d16619025cd3b834177-1614842643-0-250;',
    }

    response = requests.get('https://raidforums.com/Forum-Leaks-Market?page=1', headers=headers)

    print(response.text)
    print(response.status_code)
    reponse = etree.HTML(response.text)
    data_lists = reponse.xpath('//a[@class="forum-display__thread-name"]')
    print(len(data_lists))
    for data in data_lists:
        title = data.xpath('span/text()')[0]
        url = data.xpath('@href')[0]
        base_url = 'https://raidforums.com/{}'
        print(title)
        print(base_url.format(url))

def getCF():

    headers = {
        'authority': 'raidforums.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://raidforums.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://raidforums.com/Thread-BUYING-%D0%9A%D1%83%D0%BF%D0%BB%D1%8E-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BC%D0%BF%D1%8B-Buy-Russian-dumps',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '__cfduid=d8f45c36f72a59fc47649764cd8ba8e091614327312; PHPSESSID=19kt2dir8l9lqliju8nk12k9mg; _ga=GA1.2.193086702.1614327314; RFLovesYou_category-tab-preference=tab118; RFLovesYou_mybb[announcements]=0; cf_clearance=b855defb013f484ed05921e629af8fdac38d2c06-1614598532-0-250; RFLovesYou_sid=8e1f944f63ee39cdb0c1432e9ff5ad04; _gid=GA1.2.1533713413.1614598537; RFLovesYou_mybb[lastvisit]=1614600005; RFLovesYou_mybb[lastactive]=1614601717; RFLovesYou_mybb[threadread]=a%3A4%3A%7Bi%3A126919%3Bi%3A1614327661%3Bi%3A116138%3Bi%3A1614598703%3Bi%3A126658%3Bi%3A1614601663%3Bi%3A127306%3Bi%3A1614601717%3B%7D; cf_chl_prog=a31',
    }

    params = (
        ('__cf_chl_captcha_tk__',
         'e57f9c756da658ec339d4d590ef3a170a6649ce0-1614602219-0-AXK5cljk_3KB8xNgP98gQhcjL5R55-AWwgWNd0xMuh4-B5nNmiuSh0ei-l4CKgMZ-C1rBnn7hw6_K1NSh9aBCDYD-HtzgtblwP83FKz-VXebTqJiaS3ilyvdxGBUGaOhxpQHg6vo4p30RQmZ1h-4AGqzLDWEnW9pewbYCBWZFeYFV63wqeawnT_sJd_rjv4I-G6bVrCkYsE5G08zNGNDMN47iBe6yW5VHMypVcP4ztoARuYuKQvPMcqgME4o_s8d5jx1n_4nSUwW6AE6qEijAObtGTKyFllAZncH33NAz67QhI7axGu4VorKZqFHb8RL2H7NzdmHUvqV6vHdLfKCI6hYzRdQeexod4NMqL-sW0lqHCNtysEMSTprUf1_OBl7ndWZXPm_fPN8Jh6HdtXGr-XtyN-wbI51FZkA-zIkSL_Dri3Xd69u0N2AwolsRs2jIRqytt1Ujvgc10GLaNsJPIuOh_6wXJAN_-iXcrdcJgIeVn2yzqJ-82JmznW_qKubpPH7eOxudn7Vj15lFOswzq5lCQxxeV89UckEnLnJTLFaFeWa1e1L92OykUqWT5baxaphclgHiWXyWy5K8jvsUD0hXazXU-Mvc2GpY9MduGjiwkhOm8O1DEUAnib7dzNmB2IDwVd7UopTpzT6gctXqKjwUpj7_T4HFz2NJ-mSBCTkgAMkU9YVwFvozcPh6siXcf-KVFKjR11WhyLaAzGFs5PWbRDfRdN4OfkjcDwzUhJO'),
    )

    data = {
        'r': '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',
        'cf_captcha_kind': 'h',
        'vc': '72459820f7f1b60078bdd2008e290ef1',
        'captcha_vc': '393583cfe048477863d0745190453479',
        'captcha_answer': 'iPsKsnZGoARn-15-62926f1d8b834e26',
        'cf_ch_verify': 'plat',
        'h-captcha-response': 'captchka'
    }

    response = requests.post(
        'https://raidforums.com/Thread-BUYING-%D0%9A%D1%83%D0%BF%D0%BB%D1%8E-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BC%D0%BF%D1%8B-Buy-Russian-dumps',
        headers=headers, params=params, data=data)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.post('https://raidforums.com/Thread-BUYING-%D0%9A%D1%83%D0%BF%D0%BB%D1%8E-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BC%D0%BF%D1%8B-Buy-Russian-dumps?__cf_chl_captcha_tk__=e57f9c756da658ec339d4d590ef3a170a6649ce0-1614602219-0-AXK5cljk_3KB8xNgP98gQhcjL5R55-AWwgWNd0xMuh4-B5nNmiuSh0ei-l4CKgMZ-C1rBnn7hw6_K1NSh9aBCDYD-HtzgtblwP83FKz-VXebTqJiaS3ilyvdxGBUGaOhxpQHg6vo4p30RQmZ1h-4AGqzLDWEnW9pewbYCBWZFeYFV63wqeawnT_sJd_rjv4I-G6bVrCkYsE5G08zNGNDMN47iBe6yW5VHMypVcP4ztoARuYuKQvPMcqgME4o_s8d5jx1n_4nSUwW6AE6qEijAObtGTKyFllAZncH33NAz67QhI7axGu4VorKZqFHb8RL2H7NzdmHUvqV6vHdLfKCI6hYzRdQeexod4NMqL-sW0lqHCNtysEMSTprUf1_OBl7ndWZXPm_fPN8Jh6HdtXGr-XtyN-wbI51FZkA-zIkSL_Dri3Xd69u0N2AwolsRs2jIRqytt1Ujvgc10GLaNsJPIuOh_6wXJAN_-iXcrdcJgIeVn2yzqJ-82JmznW_qKubpPH7eOxudn7Vj15lFOswzq5lCQxxeV89UckEnLnJTLFaFeWa1e1L92OykUqWT5baxaphclgHiWXyWy5K8jvsUD0hXazXU-Mvc2GpY9MduGjiwkhOm8O1DEUAnib7dzNmB2IDwVd7UopTpzT6gctXqKjwUpj7_T4HFz2NJ-mSBCTkgAMkU9YVwFvozcPh6siXcf-KVFKjR11WhyLaAzGFs5PWbRDfRdN4OfkjcDwzUhJO', headers=headers, data=data)


if __name__ == '__main__':
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    # getLogin()
    # getList()
    raidforums()