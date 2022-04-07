import scrapy
from ..items import ScraperItem

class DetikBpsSpider(scrapy.Spider):
    name = 'link_detik'
    page_number = 2
    start_urls = ['https://www.detik.com/search/searchall?query=parpol&siteid=2&sortby=time&page=1']

    def parse(self, response):
        items = ScraperItem()
        news = response.css('article')

        for text in news:
            link = text.css('a::attr(href)').extract_first()
            link = link + '?single=1'

            yield {'': link}
        
        next_page = 'https://www.detik.com/search/searchall?query=parpol&siteid=2&sortby=time&page='+str(DetikBpsSpider.page_number)+'/'
        if DetikBpsSpider.page_number <= 37:
            DetikBpsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)