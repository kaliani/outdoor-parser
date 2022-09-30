import scrapy


class IdmediaSpyder(scrapy.Spider):

    name = 'itmedia'
    start_urls = ['https://idmedia.ua/billboard/kievskaya-oblast/kiev-trassa']

    def parse(self, response):
        boards = response.css('li.result__item')

        for board in boards:

            yield {
                'id': board.css('span.btn--xsm::text').get(),
                'title': board.css('h5.result__address::text').get(),
                'type': board.css('a.brand::text').getall()[0],
                'city': board.css('a.brand::text').getall()[1],
                'region': board.css('a.brand::text').getall()[2],
                'side': board.css('h6.mark::text').getall()[4],
                'format': board.css('h6.mark::text').getall()[6]
            }
        next_page = response.css('a.pagination__item--next::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
