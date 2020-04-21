import scrapy

class PricesSpider(scrapy.Spider):
    name = "prices"

    start_urls = [
        'https://coinmarketcap.com/'
    ]

    def parse(self,response):
        # self.logger.info("Working")
        # pass
        coins = response.css('tr.cmc-table-row')
        for coin in coins:
            yield {
                'name': coin.css('.cmc-table__column-name>.cmc-link::text').get(),
                'mkt_cap': coin.css('.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--right.cmc-table__cell--sort-by__market-cap>div::text').get(),
                'price': coin.css('.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--right.cmc-table__cell--sort-by__price>.cmc-link::text').get()
            }