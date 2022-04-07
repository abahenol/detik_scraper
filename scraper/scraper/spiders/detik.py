# Spider 2
# ArticleScraper.py which scrape article headlies and bodies
# imports
import scrapy
from scrapy.http import Request
from ..items import ScraperItem
import json

class DetikMiniArticlescraperSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://finance.detik.com/berita-ekonomi-bisnis/d-5125057/ancaman-resesi-kian-nyata-masyarakat-mesti-ngapain-nih?single=1']
    
    def parse(self,response):
        items = ScraperItem()
        #items['keyword']='bps'
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