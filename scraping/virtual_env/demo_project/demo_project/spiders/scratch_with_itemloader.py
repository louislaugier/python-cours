import scrapy
from scrapy import Spider
from divers.items import QuotesItem
from scrapy.loader import ItemLoader



class QuotesILSpider(Spider):
    name = 'spider_il'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self,response):

        quotes = response.css('div.quote')

        for quote in quotes :
            loader = ItemLoader(item=QuotesItem(),selector=quote)
            loader.add_css('content','span.text::text')
            loader.add_css('author','.author::text')
            loader.add_css('tags','a.tag::text')

            item = loader.load_item()

            yield item
