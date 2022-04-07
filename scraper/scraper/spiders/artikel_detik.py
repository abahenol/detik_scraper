# Spider 2
# ArticleScraper.py which scrape article headlies and bodies
# imports
import scrapy
from scrapy.http import Request
from ..items import ScraperItem
import json

class DetikArticlescraperSpiderfix(scrapy.Spider):
    name = 'artikel_detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://www.detik.com/search/searchall?query=bps&siteid=2&sortby=time&page=1']

    def start_requests(self):
        with open('/Users/Salim Satriajati/Documents/Document OJT BPS/scrap_fenomena/scraper/link_detik_serikatpekerja.csv') as f:
            for line in f:
                yield Request(line, callback=self.parse_article_page)
    
    def parse_article_page(self,response):
        items = ScraperItem()
        items['keyword']='serikat pekerja'
        items['link'] = response.request.url 
        
        items['judul'] = response.css('h1.detail__title::text').extract()
        if len(items['judul']) < 1:
            items['judul'] = response.css('h1.mt5::text').extract()

        items['tanggal']= response.css('.detail__date::text').extract()
        if len(items['tanggal']) < 1:
            items['tanggal']= response.css('.date::text').extract()

        items['artikel']= response.css('.itp_bodycontent p::text').extract()
        if len(items['artikel']) < 1:
            items['artikel']= response.css('.itp_bodycontent::text').extract()

        items['artikel'] = ' '.join(items['artikel'])
        items['judul'] = ''.join(items['judul'])
        items['tanggal'] = ''.join(items['tanggal'])
        
        items['judul'] = items['judul'].replace('\n','').strip()
        items['artikel'] = items['artikel'].replace('\n','').replace('\r','').replace('\xa0','').strip().strip("-").strip()
        yield items

    def parse(self, response):
        pass