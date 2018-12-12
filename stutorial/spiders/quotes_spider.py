import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        page = response.url.split('/')[-2]

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('samll.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        # # next_page = response.urljoin(next_page)
        # print(next_page)
        # next_page = response.urljoin(next_page)
        # print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
