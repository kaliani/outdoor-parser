import scrapy
## id: response.css('span.btn--xsm::text').get()
## response.xpath('//span[@class="btn btn--xsm no-hover result__id"]')
## title: response.css('h5.result__address::text')
## result_info: response.css('div.result__info')
## res.css('a.brand::text')[i].get()
## res.css('a.brand::text')[0].get()


class IdmediaSpyder(scrapy.Spider):

    name = 'itmedia'
    start_url = ['https://idmedia.ua/billboard/kievskaya-oblast/kiev']

    def parse(self, response):
        boards = response.css('ul.result__list')
        # sub_result = boards.css('div.result__info')

        for board in boards:

            yield {
                'id': board.css('span.btn--xsm::text').get(),
                'title': board.css('h5.result__address::text').get()
            }

        for a in response.css('li.next.a'):
            yield response.follow(a, callback=self.parse)
