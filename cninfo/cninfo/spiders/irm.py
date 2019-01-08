# -*- coding: utf-8 -*-
import scrapy
import time
from cninfo.items import CninfoItem

class IrmSpider(scrapy.Spider):
    name = 'irm'


    def start_requests(self):
        href_list = []
        for i in range(4*60*30):
            # for pg in range(1, 2):
                # formdata = {
                #     "condition.dateFrom": "2018-12-05",
                #     "condition.dateTo": "2019-01-04",
                #     "condition.searchType": "code",
                #     "condition.marketType": "Z",
                #     "pageNo": str(pg),
                #     "pageSize": "10",
                #     "source": "2",
                #     "requestUri": "%2Fircs%2Finteraction%2FlastRepliesForSzse.do",
                #     "requestMethod": "GET"
                # }
            print(i)
            time.sleep(30)
            yield scrapy.Request(url = 'http://irm.cninfo.com.cn/ircs/interaction/lastRepliesForSzse.do',callback=self.parse,dont_filter=True,meta={'href_list':href_list})


    def parse(self, response):
        print('start')
        href_list= response.meta['href_list']
        pare_list=response.xpath('//div[@class="Tl talkList2"]/div')
        for k,v in enumerate(pare_list):
            if k%2 ==0:
                href = v.xpath('.//a[@class="cntcolor"]/@href').extract_first()
                if href not in href_list:
                    href_list.append(href)
                    yield scrapy.Request(url='http://irm.cninfo.com.cn/ircs/interaction/'+href,
                                         callback=self.parse2, dont_filter=True, meta={'href': href})
                    print(href)
                else:
                    print('5s')



    def parse2(self,response):
        href= response.meta['href']
        item= CninfoItem()
        item['href'] = href
        q = response.xpath('//div[@class="askBoxOuter"]//div[@class="msgCnt cntcolor"]/div/text()').extract()
        q="".join(q).strip()
        item['question'] = q
        item['publish_data'] = response.xpath('//div[@class="askBoxOuter"]//div[@class="pubInfoask2"]/a/text()').extract_first()
        item['questioner'] = response.xpath('//div[@class="askBoxOuter"]//div[@class="msgCnt cntcolor"]//a/text()').extract_first()
        a = response.xpath('//div[@class="answerBox"]/div/text()').extract()
        if a:
            a="".join(a).replace("\r","").replace("\n","").replace(" ","").replace("\t","").strip()
            a = a[1:] if a[0] ==":" else a
            item['answer'] = a

        time = response.xpath('//span[@class="time"]/a/text()').extract_first()
        if time:
            item['replay_data'] = time.replace("年","-").replace("月","-").replace("日"," ")+":00"
        item['company_name'] = response.xpath('//span[@class="comName"]/a/text()').extract_first()
        item['company_code'] = response.xpath('//span[@class="comCode"]/a/text()').extract_first()
        yield  item

