# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domain= []
    # start_urls = ['http://www.weibo.com/']
    # def parse(self, response):
    #     pass

    def start_requests(self):
        post_url = 'https://passport.weibo.cn/signin/login?'
        data = {
            'username': '17701256561',
            'password': 'lizhibin666',
            'savestate': '1',
            'r': 'http://weibo.cn/',
            'ec': '0',
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': '',
        }
        headers = {
            'Referer': 'https://weibo.cn/'
        }

        yield scrapy.FormRequest(url=post_url,callback=self.parse_info,formdata=data)


    def parse_info(self,response):
        # 接着访问登录之后的页面
        url =  'https://weibo.cn/6388179289/info'
        print('3456789')
        yield scrapy.Request(url=url,callback=self.parse_data)


    def parse_data(self,response):
        print(response.text)
