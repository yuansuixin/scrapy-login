# -*- coding: utf-8 -*-
import urllib.request

import scrapy


# 需要先发送get请求，到达登录页面，然后登录

class WeiboSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/accounts/login']

    def parse(self, response):
        post_url = 'https://www.douban.com/accounts/login'
        headers = {
            'Referer': 'https://www.douban.com/',
        }
        # 去页面中查找有没有验证码
        image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        print(image_url, '&' * 40)
        # 判断有么有image_url ,说明有没有验证码
        if not image_url:
            data = {
                'source': 'index_nav',
                'form_email': '1090509990@qq.com',
                'form_password': 'lizhibin666',
            }
        else:
            urllib.request.urlretrieve(image_url, 'code.png')
            code = input('请输入验证码：')

            # 获取captcha-id
            cid = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
            # 有验证码的情况
            data = {
                'source': 'None',
                'redir': 'https://www.douban.com',
                'form_email': '1090509990@qq.com',
                'form_password': 'lizhibin666',
                'captcha-solution': code,
                'captcha-id': cid,
                'login': '登录',
            }
        yield scrapy.FormRequest(url=post_url, headers=headers, formdata=data, callback=self.lalal)

    def lalal(self, response):
        print(response.text)






