# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:24:05 2018

@author: CFSS-FS
"""

import scrapy
from urlcrawl.items import UrlcrawlItem
class msp(scrapy.Spider):
    name='msp'
#    start_urls=['http://www.juduoba.com/show/1.html']
    def start_requests(self):
        base_url='http://www.juduoba.com/show/'
        tail_url='.html'
        for i in range(45000):
            self.start_urls.append(base_url+str(i)+tail_url)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
#            yield scrapy.Request(url,callback=self.parse)
    def parse(self,response):
        item=UrlcrawlItem()
        for box in response.xpath('//body'):
            item['name']=box.xpath('//h1[@class="movie-title"]/text()').extract_first()
            item['year']=box.xpath('//h1[@class="movie-title"]/span/text()').extract_first()
            item['ftype']=box.xpath('//ol[@class="breadcrumb"]/li[2]/a/text()').extract_first()
            item['jpg']=box.xpath('//a/img/@src').extract_first()
            yield item
    