import scrapy
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider):
    name = "login"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):
        # self.logger.info("Working")
        # pass
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall()
            }