from scrapy import Spider

class SimpleSpider(Spider):

    name = 'simple'

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):
        quotes = response.css('div.quote')

        for quote in quotes:
            yield {
                'content': quote.css('span.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').get()
            }

        next_url = response.css('li.next a::atr(href)').get()

        # if next_url is not None:
        #     yield response.follow(next_url,callback=self.parse)

        if next_url is not None:
            next_url = response.urljoin(next_url)
            # http://quotes.toscrape.com/page/2

            yield scrapy.Requests(next_url,callback=self.parse)

